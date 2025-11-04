# Blog state management
import reflex as rx
from typing import Optional

from ..models import BlogPost
from ..services import blog_service


class BlogState(rx.State):
    """State management for blog functionality"""

    # All loaded blog posts
    all_posts: list[BlogPost] = []

    # Current post being viewed (for individual post page)
    current_post: Optional[BlogPost] = None

    # Loading state
    posts_loaded: bool = False

    def load_posts(self):
        """Load all blog posts from the blog_content directory"""
        if not self.posts_loaded:
            self.all_posts = blog_service.load_all_posts()
            self.posts_loaded = True

    def load_post_by_slug(self):
        """
        Load a specific blog post by its slug from the route parameters

        Note: For a route like /blog/[slug], the slug parameter is automatically
        available as self.slug (Reflex dynamic routing feature)
        """
        # Get slug from dynamic route parameter (automatically available)
        slug = self.slug

        if not slug:
            return

        # First ensure posts are loaded
        if not self.posts_loaded:
            self.load_posts()

        # Try to find in loaded posts first
        for post in self.all_posts:
            if post.slug == slug:
                self.current_post = post
                return

        # If not found in cache, try loading directly
        self.current_post = blog_service.get_post_by_slug(slug)

    @rx.var
    def sorted_posts(self) -> list[BlogPost]:
        """
        Get all posts sorted by date (newest first)

        Returns:
            List of BlogPost objects sorted by date
        """
        return sorted(self.all_posts, key=lambda p: p.date, reverse=True)

    @rx.var
    def has_posts(self) -> bool:
        """Check if there are any posts available"""
        return len(self.all_posts) > 0
