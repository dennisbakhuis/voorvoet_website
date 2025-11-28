"""Blog state management for loading and displaying blog posts.

This module contains the BlogState class which manages the state for blog
functionality including loading posts, managing the current post, and
providing computed properties for post display.
"""
import reflex as rx
from typing import Optional
import json

from ..models import BlogPost
from ..services import blog_service
from .website_state import WebsiteState


class BlogState(WebsiteState):
    """
    State manager for blog functionality.

    Handles loading and caching of blog posts from markdown files, manages
    the currently displayed post for individual post pages, and provides
    computed properties for sorted and filtered post lists.

    The state leverages Reflex's dynamic routing to automatically load posts
    based on URL slug parameters (e.g., /blog/[slug]).

    Attributes
    ----------
    all_posts : list[BlogPost]
        Complete list of all loaded blog posts from the blog_content directory
    current_post : Optional[BlogPost]
        The blog post currently being viewed on an individual post page,
        or None if on the blog list page
    posts_loaded : bool
        Flag indicating whether blog posts have been loaded from disk to
        avoid redundant file system operations
    """

    all_posts: list[BlogPost] = []
    current_post: Optional[BlogPost] = None
    posts_loaded: bool = False

    def load_posts(self):
        """
        Load all blog posts from the blog_content directory for the current language.

        Reads markdown files from the blog content directory and parses them
        into BlogPost objects. Reloads when language changes to show correct translations.
        Also detects the current language from the route.
        """
        self.detect_language_from_route()

        blog_service.clear_cache()
        self.all_posts = blog_service.load_all_posts(language=self.current_language)
        self.posts_loaded = True

    def load_post_by_slug(self):
        """
        Load a specific blog post by its slug from the route parameters for the current language.

        Retrieves the slug from Reflex's dynamic routing (automatically
        available as self.slug for routes like /blog/[slug]). First attempts
        to find the post in the cached posts list, then falls back to loading
        directly from the file system if not found. Also detects the current
        language from the route.

        Notes
        -----
        The slug parameter is automatically provided by Reflex's dynamic
        routing system and is accessible as self.slug when this method
        is called from a route with a [slug] parameter.
        """
        self.detect_language_from_route()

        slug = self.slug

        if not slug:
            return

        blog_service.clear_cache()
        self.all_posts = blog_service.load_all_posts(language=self.current_language)
        self.posts_loaded = True

        for post in self.all_posts:
            if post.slug == slug:
                self.current_post = post
                return

        self.current_post = blog_service.get_post_by_slug(slug, language=self.current_language)

    @rx.var
    def sorted_posts(self) -> list[BlogPost]:
        """
        Get all posts sorted by publication date.

        Returns
        -------
        list[BlogPost]
            List of BlogPost objects sorted by date in descending order
            (newest posts first)
        """
        return sorted(self.all_posts, key=lambda p: p.date, reverse=True)

    @rx.var
    def has_posts(self) -> bool:
        """
        Check if any blog posts are available.

        Returns
        -------
        bool
            True if at least one blog post has been loaded, False otherwise
        """
        return len(self.all_posts) > 0

    @rx.var
    def article_schema_json(self) -> str:
        """
        Generate Article JSON-LD structured data for the current blog post.

        Creates schema markup dynamically from current_post data for SEO.
        Returns empty string if no current post is loaded.

        Returns
        -------
        str
            JSON-LD structured data as string, or empty string if no post
        """
        if not self.current_post:
            return ""

        base_url = "https://voorvoet.nl"
        post = self.current_post

        # Construct full canonical URL
        full_url = f"{base_url}/{self.current_language}/blog/{post.slug}/"

        # Image URL - prepend base_url to thumbnail path
        image_url = f"{base_url}{post.thumbnail_url}"

        # Extract article snippet from first 200 words of content
        words = post.content.split()
        snippet_words = words[:200] if len(words) > 200 else words
        article_snippet = ' '.join(snippet_words)
        # Clean up markdown formatting for snippet
        article_snippet = article_snippet.replace('#', '').replace('*', '').replace('!', '').strip()

        # Build article data
        article_data = {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": post.title,
            "description": post.summary,
            "articleBody": article_snippet,
            "image": {
                "@type": "ImageObject",
                "url": image_url,
                "caption": post.thumbnail_alt if post.thumbnail_alt else post.title
            },
            "datePublished": post.date.isoformat(),
            "dateModified": post.date_modified.isoformat() if post.date_modified else post.date.isoformat(),
            "author": {
                "@type": "Person",
                "name": post.author if post.author else "Kim Bakhuis",
                "url": base_url,
                "sameAs": "https://www.linkedin.com/in/kimbakhuis/"
            },
            "publisher": {
                "@type": "Organization",
                "name": "VoorVoet",
                "url": base_url,
                "logo": {
                    "@type": "ImageObject",
                    "url": f"{base_url}/images/shared/podotherapeut_enschede_voorvoet_praktijk_voor_podotherapie_logo.svg"
                }
            },
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": full_url
            },
            "url": full_url,
            "inLanguage": self.current_language,
        }

        # Add word count from content
        word_count = len(post.content.split())
        if word_count > 0:
            article_data["wordCount"] = word_count

        # Add keywords from tags
        if post.tags and len(post.tags) > 0:
            article_data["keywords"] = post.tags

        # Add article section/category
        if post.category:
            article_data["articleSection"] = post.category

        return json.dumps(article_data, ensure_ascii=False, indent=2)
