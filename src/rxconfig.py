import reflex as rx
from reflex.plugins import TailwindV4Plugin

tailwind_config = {
  "content": ["./**/*.py"],
  "theme": {"extend": {"fontFamily": {"sans": ["Lato","ui-sans-serif","system-ui"]}}},
}

config = rx.Config(
    app_name="voorvoet_website",
    plugins=[
        TailwindV4Plugin(config=tailwind_config),  # type: ignore
    ],
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)
