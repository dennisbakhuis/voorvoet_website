"""Blog state management for loading and displaying blog posts.

This module contains the BlogState class which manages the state for blog
functionality including loading posts, managing the current post, and
providing computed properties for post display.
"""
import reflex as rx
from typing import Optional

from ..models import BlogPost
from ..services import blog_service


class BlogState(rx.State):
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
        Load all blog posts from the blog_content directory.

        Reads markdown files from the blog content directory and parses them
        into BlogPost objects. Only loads once per session to improve performance.
        """
        if not self.posts_loaded:
            self.all_posts = blog_service.load_all_posts()
            self.posts_loaded = True

    def load_post_by_slug(self):
        """
        Load a specific blog post by its slug from the route parameters.

        Retrieves the slug from Reflex's dynamic routing (automatically
        available as self.slug for routes like /blog/[slug]). First attempts
        to find the post in the cached posts list, then falls back to loading
        directly from the file system if not found.

        Notes
        -----
        The slug parameter is automatically provided by Reflex's dynamic
        routing system and is accessible as self.slug when this method
        is called from a route with a [slug] parameter.
        """
        slug = self.slug

        if not slug:
            return

        if not self.posts_loaded:
            self.load_posts()

        for post in self.all_posts:
            if post.slug == slug:
                self.current_post = post
                return

        self.current_post = blog_service.get_post_by_slug(slug)

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
