"""Structured data components for SEO optimization."""

import reflex as rx
from typing import Any
import json

from ..models.blog_post import BlogPostDict


def organization_brand_schema() -> rx.Component:
    """
    Generate Organization JSON-LD structured data for brand identity.

    Returns
    -------
    rx.Component
        A script tag containing JSON-LD structured data.
    """
    org_data: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "VoorVoet",
        "alternateName": "Praktijk voor podotherapie",
        "url": "https://voorvoet.nl",
        "logo": "https://voorvoet.nl/images/shared/podotherapeut_enschede_voorvoet_praktijk_voor_podotherapie_logo.svg",
        "description": "VoorVoet is een moderne podotherapiepraktijk in Enschede gespecialiseerd in voetzorg, podotherapie en orthopedische schoentechniek.",
        "telephone": "+31657750997",
        "email": "info@voorvoet.nl",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Eeftinksweg 13",
            "addressLocality": "Enschede",
            "postalCode": "7541 WE",
            "addressCountry": "NL",
        },
        "founder": {
            "@type": "Person",
            "name": "Kim Bakhuis",
            "jobTitle": "Founder/Podiatrist",
            "sameAs": "https://www.linkedin.com/in/kimbakhuis/",
        },
        "sameAs": [
            "https://www.linkedin.com/company/voorvoet/",
        ],
    }

    json_ld = json.dumps(org_data, ensure_ascii=False, indent=2)

    return rx.el.script(
        json_ld,
        type="application/ld+json",
    )


def organization_schema() -> rx.Component:
    """
    Generate Organization/Podiatrist JSON-LD structured data.

    Returns
    -------
    rx.Component
        A script tag containing JSON-LD structured data.
    """

    org_data: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "Podiatrist",
        "name": "VoorVoet",
        "alternateName": "Praktijk voor podotherapie",
        "url": "https://voorvoet.nl",
        "logo": "https://voorvoet.nl/images/shared/podotherapeut_enschede_voorvoet_praktijk_voor_podotherapie_logo.svg",
        "image": "https://voorvoet.nl/images/shared/podotherapeut_enschede_voorvoet_praktijk_voor_podotherapie_logo.svg",
        "telephone": "+31657750997",
        "email": "info@voorvoet.nl",
        "address": [
            {
                "@type": "PostalAddress",
                "name": "Locatie Eeftinksweg",
                "streetAddress": "Eeftinksweg 13",
                "addressLocality": "Enschede",
                "postalCode": "7541 WE",
                "addressCountry": "NL",
            },
            {
                "@type": "PostalAddress",
                "name": "Locatie Beethovenlaan",
                "streetAddress": "Beethovenlaan 10",
                "addressLocality": "Enschede",
                "postalCode": "7522 HJ",
                "addressCountry": "NL",
            },
        ],
        "geo": [
            {
                "@type": "GeoCoordinates",
                "latitude": "52.20872",
                "longitude": "6.89328",
                "name": "Locatie Eeftinksweg",
            },
            {
                "@type": "GeoCoordinates",
                "latitude": "52.22145",
                "longitude": "6.88534",
                "name": "Locatie Beethovenlaan",
            },
        ],
        "areaServed": [
            {"@type": "City", "name": "Enschede"},
            {"@type": "City", "name": "Hengelo"},
            {"@type": "City", "name": "Wierden"},
            {"@type": "City", "name": "Glanerbrug"},
            {"@type": "City", "name": "Haaksbergen"},
            {"@type": "City", "name": "Boekelo"},
            {"@type": "City", "name": "Lonneker"},
            {"@type": "City", "name": "Losser"},
            {"@type": "City", "name": "Oldenzaal"},
            {"@type": "City", "name": "Gronau"},
            {"@type": "AdministrativeArea", "name": "Overijssel"},
        ],
        "hasMap": [
            "https://maps.google.com/?q=Eeftinksweg+13,+7541+WE+Enschede",
            "https://maps.google.com/?q=Beethovenlaan+10,+7522+HJ+Enschede",
        ],
        "paymentAccepted": "Cash, Debit Card, Bank Transfer",
        "priceRange": "€€",
        "medicalSpecialty": "Podiatry",
        "knowsAbout": [
            "Podotherapie",
            "Orthopedische schoentechniek",
            "Zolen op maat",
            "Voetklachten",
            "Diabetes voetzorg",
        ],
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": "Monday",
                "opens": "08:00",
                "closes": "17:00",
            },
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": "Tuesday",
                "opens": "09:30",
                "closes": "19:30",
            },
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": "Wednesday",
                "opens": "08:30",
                "closes": "17:00",
            },
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": "Thursday",
                "opens": "08:00",
                "closes": "17:00",
            },
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": "Friday",
                "opens": "08:00",
                "closes": "13:00",
            },
        ],
        "availableLanguage": ["nl", "de", "en"],
        "identifier": {
            "@type": "PropertyValue",
            "propertyID": "KvK",
            "value": "87984814",
        },
        "taxID": "87984814",
        "sameAs": [
            "https://www.linkedin.com/company/voorvoet/",
            "https://www.linkedin.com/in/dennisbakhuis/",
        ],
        "founder": {
            "@type": "Person",
            "name": "Kim Bakhuis",
            "jobTitle": "Founder/Podiatrist",
            "sameAs": "https://www.linkedin.com/in/kimbakhuis/",
        },
        "employee": {
            "@type": "Person",
            "name": "Dennis Bakhuis",
            "jobTitle": "Head of Data Science",
            "sameAs": "https://www.linkedin.com/in/dennisbakhuis/",
        },
    }

    json_ld = json.dumps(org_data, ensure_ascii=False, indent=2)

    return rx.el.script(
        json_ld,
        type="application/ld+json",
    )


def article_schema(post: BlogPostDict, language: str) -> rx.Component:
    """
    Generate Article JSON-LD structured data for blog posts.

    Parameters
    ----------
    post : dict
        The blog post dictionary to generate schema for
    language : str
        Language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A script tag containing JSON-LD Article structured data
    """
    base_url = "https://voorvoet.nl"

    full_url = f"{base_url}/{language}/blog/{post['slug']}/"
    image_url = f"{base_url}{post['thumbnail_fallback']}"
    words = post["content"].split()
    snippet_words = words[:200] if len(words) > 200 else words
    article_snippet = " ".join(snippet_words)
    article_snippet = (
        article_snippet.replace("#", "").replace("*", "").replace("!", "").strip()
    )

    article_data: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": post["title"],
        "description": post["summary"],
        "articleBody": article_snippet,
        "image": {
            "@type": "ImageObject",
            "url": image_url,
            "caption": post["thumbnail_alt"],
        },
        "datePublished": post["datetime_iso"],
        "dateModified": post["datetime_iso"],
        "author": {
            "@type": "Person",
            "name": post.get("author", "Kim Bakhuis") or "Kim Bakhuis",
            "url": base_url,
            "sameAs": "https://www.linkedin.com/in/kimbakhuis/",
        },
        "publisher": {
            "@type": "Organization",
            "name": "VoorVoet",
            "url": base_url,
            "logo": {
                "@type": "ImageObject",
                "url": f"{base_url}/images/shared/podotherapeut_enschede_voorvoet_praktijk_voor_podotherapie_logo.svg",
            },
        },
        "mainEntityOfPage": {"@type": "WebPage", "@id": full_url},
        "url": full_url,
        "inLanguage": language,
    }

    word_count = len(post["content"].split())
    if word_count > 0:
        article_data["wordCount"] = word_count

    if post.get("category"):
        article_data["articleSection"] = post["category"]

    json_ld = json.dumps(article_data, ensure_ascii=False, indent=2)

    return rx.el.script(
        json_ld,
        type="application/ld+json",
    )


def breadcrumb_schema(items: list[dict[str, str]]) -> rx.Component:
    """Generate BreadcrumbList JSON-LD structured data for navigation hierarchy.

    Parameters
    ----------
    items : list[dict[str, str]]
        List of breadcrumb items, each with 'name' and 'url' keys.
        Items should be in order from root to current page.

    Returns
    -------
    rx.Component
        A script tag containing JSON-LD BreadcrumbList structured data.
    """
    breadcrumb_data: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": idx + 1,
                "name": item["name"],
                "item": item["url"],
            }
            for idx, item in enumerate(items)
        ],
    }

    json_ld = json.dumps(breadcrumb_data, ensure_ascii=False, indent=2)

    return rx.el.script(
        json_ld,
        type="application/ld+json",
    )
