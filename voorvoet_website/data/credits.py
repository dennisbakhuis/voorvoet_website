"""Credits data for Python packages and images used on the website."""

from typing import TypedDict


class PythonPackage(TypedDict):
    name: str
    url: str
    desc: dict[str, str]


class ImageCredit(TypedDict):
    category: str
    desc: dict[str, str]
    image_path: str
    author: str | None
    author_url: str | None
    source: str
    source_url: str | None


PYTHON_PACKAGES: list[PythonPackage] = [
    {
        "name": "Python",
        "url": "https://www.python.org",
        "desc": {
            "nl": "Programmeertaal voor (bijna) alles",
            "de": "Programmiersprache für (fast) alles",
            "en": "Programming language for (almost) everything",
        },
    },
    {
        "name": "Reflex",
        "url": "https://reflex.dev",
        "desc": {
            "nl": "Full-stack web framework voor Python",
            "de": "Full-Stack-Webframework für Python",
            "en": "Full-stack web framework for Python",
        },
    },
    {
        "name": "Mistletoe",
        "url": "https://github.com/miyuchina/mistletoe",
        "desc": {
            "nl": "Snelle en uitbreidbare Markdown parser",
            "de": "Schneller und erweiterbarer Markdown-Parser",
            "en": "Fast and extensible Markdown parser",
        },
    },
    {
        "name": "Pydantic Settings",
        "url": "https://docs.pydantic.dev/latest/concepts/pydantic_settings/",
        "desc": {
            "nl": "Settings management met Pydantic",
            "de": "Einstellungsverwaltung mit Pydantic",
            "en": "Settings management using Pydantic",
        },
    },
    {
        "name": "Python Frontmatter",
        "url": "https://github.com/eyeseast/python-frontmatter",
        "desc": {
            "nl": "Parsen van posts met YAML frontmatter",
            "de": "Parsen von Posts mit YAML-Frontmatter",
            "en": "Parse and manage posts with YAML frontmatter",
        },
    },
]

IMAGES: list[ImageCredit] = [
    {
        "category": "blog",
        "desc": {
            "nl": "Blog standaard thumbnail",
            "de": "Blog Standard-Thumbnail",
            "en": "Blog default thumbnail",
        },
        "image_path": "/images/page_blog/default_thumbnail.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "blog",
        "desc": {
            "nl": "Blog standaard opvulling",
            "de": "Blog Standard-Füller",
            "en": "Blog default filler",
        },
        "image_path": "/images/page_blog/default_image_filler.webp",
        "author": "Nino Liverani",
        "author_url": "https://unsplash.com/@ninoliverani",
        "source": "Unsplash",
        "source_url": "https://unsplash.com/photos/brown-and-white-skeleton-foot-EayqAlQiFeQ",
    },
    {
        "category": "blog",
        "desc": {
            "nl": "Sandalen afbeelding",
            "de": "Sandalen Bild",
            "en": "Sandals image",
        },
        "image_path": "/images/page_blog/voorvoet_praktijk_voor_podotherapie_Sandalen_Durea_modern_uitneembaar_voetbed_steunzolen_op_maat_gezonde_blote_voeten_bij_zwembad.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "blog",
        "desc": {
            "nl": "Blog post 001: Thumbnail",
            "de": "Blog-Post 001: Thumbnail",
            "en": "Blog post 001: Thumbnail",
        },
        "image_path": "/images/page_blog/001_podotherapeut_of_podoloog/thumbnail.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "blog",
        "desc": {
            "nl": "Blog post 001: Hero",
            "de": "Blog-Post 001: Hero",
            "en": "Blog post 001: Hero",
        },
        "image_path": "/images/page_blog/001_podotherapeut_of_podoloog/Podotherapeut_podoloog_VoorVoet_Enschede_voetklachten_podotherapeut_legt_uit.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "blog",
        "desc": {
            "nl": "Blog post 002: Thumbnail",
            "de": "Blog-Post 002: Thumbnail",
            "en": "Blog post 002: Thumbnail",
        },
        "image_path": "/images/page_blog/002_alles_over_steunzolen_of_podotherapeutische_zolen/thumbnail.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "blog",
        "desc": {
            "nl": "Blog post 002: Hero",
            "de": "Blog-Post 002: Hero",
            "en": "Blog post 002: Hero",
        },
        "image_path": "/images/page_blog/002_alles_over_steunzolen_of_podotherapeutische_zolen/VoorVoet_steunzolen_op_maat_gemaakt_podotherapeut_Enschede.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "blog",
        "desc": {
            "nl": "Blog post 003: Thumbnail",
            "de": "Blog-Post 003: Thumbnail",
            "en": "Blog post 003: Thumbnail",
        },
        "image_path": "/images/page_blog/003_zonder_voetklachten_het_nieuwe_jaar_in/thumbnail.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "blog",
        "desc": {
            "nl": "Blog post 003: Hero 1",
            "de": "Blog-Post 003: Hero 1",
            "en": "Blog post 003: Hero 1",
        },
        "image_path": "/images/page_blog/003_zonder_voetklachten_het_nieuwe_jaar_in/Podotherapeut_Enschede_wat_je_ambities_ook_zijn_oostenrijk.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "blog",
        "desc": {
            "nl": "Blog post 003: Hero 2",
            "de": "Blog-Post 003: Hero 2",
            "en": "Blog post 003: Hero 2",
        },
        "image_path": "/images/page_blog/003_zonder_voetklachten_het_nieuwe_jaar_in/Podotherapie_Enschede_Wandelen_blessure_oostenrijk.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_contact",
        "desc": {
            "nl": "Contact hero banner",
            "de": "Kontakt Hero-Banner",
            "en": "Contact hero banner",
        },
        "image_path": "/images/page_contact/voetklachten_enschede_zere_voeten_voorvoet_contact.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_credits",
        "desc": {
            "nl": "Credits hero banner",
            "de": "Credits Hero-Banner",
            "en": "Credits hero banner",
        },
        "image_path": "/images/page_credits/credits_hero_banner.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_credits",
        "desc": {
            "nl": "Dennis Bakhuis portret",
            "de": "Dennis Bakhuis Porträt",
            "en": "Dennis Bakhuis portrait",
        },
        "image_path": "/images/page_credits/dennis_bakhuis_data_scientist_voorvoet_website_developer.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_home",
        "desc": {
            "nl": "Hero: Kim Bakhuis op strand",
            "de": "Hero: Kim Bakhuis am Strand",
            "en": "Hero: Kim Bakhuis on beach",
        },
        "image_path": "/images/page_home/podotherapeut_enschede_kim_bakhuis_loopt_op_strand_voorvoet_praktijk_voor_podotherapie.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_home",
        "desc": {
            "nl": "Wie is VoorVoet: Kim Bakhuis portret",
            "de": "Wer ist VoorVoet: Kim Bakhuis Porträt",
            "en": "Who is VoorVoet: Kim Bakhuis portrait",
        },
        "image_path": "/images/page_home/podotherapeut_enschede_kim_bakhuis_van_voorvoet_praktijk_voor_podotherapie.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_home",
        "desc": {
            "nl": "Outdoor schoenen",
            "de": "Outdoor-Schuhe",
            "en": "Outdoor shoes",
        },
        "image_path": "/images/page_home/podoloog_enschede_outdoor_schoenen_voorvoet_praktijk_voor_podotherapie.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_home",
        "desc": {
            "nl": "Voeten in bed",
            "de": "Füße im Bett",
            "en": "Feet in bed",
        },
        "image_path": "/images/page_home/podotherapeut_enschede_voeten_in_bed_podotherapie_helpt.webp",
        "author": "Simon Berger",
        "author_url": "https://unsplash.com/@simon_berger",
        "source": "Unsplash",
        "source_url": "https://unsplash.com/photos/three-people-underneath-yellow-bed-blanket-HSy0QXIRafg",
    },
    {
        "category": "page_information",
        "desc": {
            "nl": "Voet anatomie",
            "de": "Fuß Anatomie",
            "en": "Foot anatomy",
        },
        "image_path": "/images/page_information/anatomie-voet-hielpijn_voorvoet_podotherapie_enschede.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_information",
        "desc": {
            "nl": "Bedrijfs podotherapie",
            "de": "Betriebliche Podotherapie",
            "en": "Business podotherapy",
        },
        "image_path": "/images/page_information/bedrijfs_podotherapie_pijnlijke_voeten_hielpijn_voorvoet_podotherapie_enschede.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_information",
        "desc": {
            "nl": "Nagelbeugel behandeling",
            "de": "Nagelspangen-Behandlung",
            "en": "Nail bracket treatment",
        },
        "image_path": "/images/page_information/nagelbeugel_nagelproblemen_voorvoet_podotherapie_enschede.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_information",
        "desc": {
            "nl": "Behandelaar met patiënt",
            "de": "Behandler mit Patient",
            "en": "Practitioner with patient",
        },
        "image_path": "/images/page_information/podotherapeut_enschede_kim_bakhuis_legt_het_met_een_lach_uit-VoorVoet_podotherapie_enschede.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_information",
        "desc": {
            "nl": "Wandeling in het bos",
            "de": "Waldspaziergang",
            "en": "Forest walk",
        },
        "image_path": "/images/page_information/podotherapie_enschede_wandeling_in_het_bos_zonder_hielpijn_voorvoet_podotherapie_enschede.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_information",
        "desc": {
            "nl": "Voet skelet",
            "de": "Fuß Skelett",
            "en": "Foot skeleton",
        },
        "image_path": "/images/page_information/skelet_botjes_voet_voorvoet_praktijk_voor_podotherapie_enschede.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_information",
        "desc": {
            "nl": "Sport voetklachten",
            "de": "Sport Fußbeschwerden",
            "en": "Sports foot complaints",
        },
        "image_path": "/images/page_information/voetklachten_hielpijn_sport_voorvoet_podotherapie_enschede.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_information",
        "desc": {
            "nl": "Wandelen zonder pijn",
            "de": "Schmerzfrei gehen",
            "en": "Walking without pain",
        },
        "image_path": "/images/page_information/wandelen_zonder_pijn_in_de_voeten_voorvoet_podotherapie_enschede.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_not_found",
        "desc": {
            "nl": "404 pagina achtergrond",
            "de": "404-Seite Hintergrund",
            "en": "404 page background",
        },
        "image_path": "/images/page_not_found/404_not_found_voorvoet.webp",
        "author": "Daniel Jensen",
        "author_url": "https://unsplash.com/@dallehj",
        "source": "Unsplash",
        "source_url": "https://unsplash.com/photos/persons-hand-over-brown-floral-field-during-daytime-UDleHDOhBZ8",
    },
    {
        "category": "page_order_insoles",
        "desc": {
            "nl": "Zolen bestellen hero",
            "de": "Einlagen bestellen Hero",
            "en": "Order insoles hero",
        },
        "image_path": "/images/page_order_insoles/hiking_shoes.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "page_reimbursements",
        "desc": {
            "nl": "Vergoedingen hero",
            "de": "Erstattungen Hero",
            "en": "Reimbursements hero",
        },
        "image_path": "/images/page_reimbursements/Hielpijn_hielspoor_plantaire_fasciits_tarieven.webp",
        "author": "Dennis Bakhuis",
        "author_url": "https://unsplash.com/@dennisbakhuis",
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
    },
    {
        "category": "shared",
        "desc": {
            "nl": "VoorVoet Logo",
            "de": "VoorVoet Logo",
            "en": "VoorVoet Logo",
        },
        "image_path": "/images/shared/podotherapeut_enschede_voorvoet_praktijk_voor_podotherapie_logo.svg",
        "author": None,
        "author_url": None,
        "source": "VoorVoet",
        "source_url": None,
    },
    {
        "category": "shared",
        "desc": {
            "nl": "NVVP Lidmaatschap Badge",
            "de": "NVVP Mitgliedschaftsabzeichen",
            "en": "NVVP Membership Badge",
        },
        "image_path": "/images/shared/podotherapeut_enschede_nederlandse_vereniging_van_podotherapeuten_voorvoet.webp",
        "author": None,
        "author_url": None,
        "source": "VoorVoet",
        "source_url": None,
    },
    {
        "category": "shared",
        "desc": {
            "nl": "Register Paramedici Certificering",
            "de": "Register Paramedici Zertifizierung",
            "en": "Register Paramedici Certification",
        },
        "image_path": "/images/shared/podotherapeut_enschede_kwaliteit_register_paramedici_kim_bakhuis_geregistreerd.webp",
        "author": None,
        "author_url": None,
        "source": "VoorVoet",
        "source_url": None,
    },
    {
        "category": "shared",
        "desc": {
            "nl": "NVVP Kwaliteitskeurmerk",
            "de": "NVVP Qualitätszeichen",
            "en": "NVVP Quality Mark",
        },
        "image_path": "/images/shared/podotherapie_enschede_kwaliteit_keurmerk_nvvp_vooervoet.webp",
        "author": "Kim Bakhuis",
        "author_url": "https://voorvoet.nl",
        "source": "VoorVoet",
        "source_url": "https://voorvoet.nl",
    },
]
