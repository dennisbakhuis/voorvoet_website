import reflex as rx


config = rx.Config(
    app_name="voorvoet_website",
    deploy_url="https://voorvoet.nl",
    plugins=[
        rx.plugins.SitemapPlugin(),
    ],
    show_built_with_reflex=False,
)
