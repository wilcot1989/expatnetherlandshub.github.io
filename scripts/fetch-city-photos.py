#!/usr/bin/env python3
"""
Fetch city photos from Wikimedia Commons for Expat Netherlands Hub.
Downloads the best skyline/panorama photo per city, resizes to 1200x800 WebP.
"""

import os
import json
import requests
from PIL import Image
from io import BytesIO

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_DIR, "static", "images", "cities")
ATTR_FILE = os.path.join(OUTPUT_DIR, "ATTRIBUTIONS.md")

TARGET_WIDTH = 1200
TARGET_HEIGHT = 800
WEBP_QUALITY = 80

# Curated search terms per city — specific enough to get good skyline/panorama shots
CITIES = {
    "amsterdam": "Amsterdam skyline Centraal panorama",
    "rotterdam": "Rotterdam skyline Erasmusbrug",
    "the-hague": "The Hague Binnenhof panorama",
    "utrecht": "Utrecht Dom Tower canal",
    "eindhoven": "Eindhoven city centre",
    "leiden": "Leiden canals panorama",
    "groningen": "Groningen Martinitoren city",
    "maastricht": "Maastricht Vrijthof panorama",
    "delft": "Delft canal Nieuwe Kerk",
    "haarlem": "Haarlem Grote Markt panorama",
    "den-bosch": "s-Hertogenbosch Sint-Janskathedraal",
    "breda": "Breda Grote Kerk city",
}

API_URL = "https://commons.wikimedia.org/w/api.php"
USER_AGENT = "ExpatNetherlandsHub/1.0 (https://expatnetherlandshub.com; city-photos)"


def search_commons(query, limit=5):
    """Search Wikimedia Commons for images matching query."""
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": f"filetype:bitmap {query}",
        "gsrnamespace": 6,  # File namespace
        "gsrlimit": limit,
        "prop": "imageinfo",
        "iiprop": "url|size|extmetadata|mime",
        "iiurlwidth": 1200,
    }
    headers = {"User-Agent": USER_AGENT}
    resp = requests.get(API_URL, params=params, headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    pages = data.get("query", {}).get("pages", {})
    results = []
    for page_id, page in pages.items():
        info = page.get("imageinfo", [{}])[0]
        width = info.get("width", 0)
        height = info.get("height", 0)
        mime = info.get("mime", "")

        # Filter: must be a photo (JPEG/PNG), landscape, and reasonably large
        if mime not in ("image/jpeg", "image/png"):
            continue
        if width < 1200 or height < 600:
            continue
        if width <= height:  # Skip portrait
            continue

        ext = info.get("extmetadata", {})
        license_short = ext.get("LicenseShortName", {}).get("value", "")
        artist = ext.get("Artist", {}).get("value", "Unknown")
        title = page.get("title", "")

        # Only CC licenses or public domain
        allowed = ["CC BY-SA", "CC BY", "CC0", "Public domain", "pd"]
        if not any(lic.lower() in license_short.lower() for lic in allowed):
            continue

        # Prefer the thumbnail URL at 1200px width if available
        thumb_url = info.get("thumburl", info.get("url", ""))
        original_url = info.get("url", "")

        results.append({
            "title": title,
            "url": thumb_url or original_url,
            "original_url": original_url,
            "width": width,
            "height": height,
            "license": license_short,
            "artist": artist,
            "score": width * height,  # Prefer larger images
        })

    # Sort by resolution (largest first)
    results.sort(key=lambda x: x["score"], reverse=True)
    return results


def download_and_resize(url, output_path):
    """Download image, resize to TARGET dimensions, save as WebP."""
    headers = {"User-Agent": USER_AGENT}
    resp = requests.get(url, headers=headers, timeout=60)
    resp.raise_for_status()

    img = Image.open(BytesIO(resp.content))
    img = img.convert("RGB")

    # Crop to target aspect ratio (3:2) then resize
    target_ratio = TARGET_WIDTH / TARGET_HEIGHT
    img_ratio = img.width / img.height

    if img_ratio > target_ratio:
        # Too wide — crop sides
        new_width = int(img.height * target_ratio)
        left = (img.width - new_width) // 2
        img = img.crop((left, 0, left + new_width, img.height))
    elif img_ratio < target_ratio:
        # Too tall — crop top/bottom
        new_height = int(img.width / target_ratio)
        top = (img.height - new_height) // 2
        img = img.crop((0, top, img.width, top + new_height))

    img = img.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.LANCZOS)
    img.save(output_path, "WEBP", quality=WEBP_QUALITY)
    return os.path.getsize(output_path)


def strip_html(text):
    """Remove HTML tags from attribution text."""
    import re
    return re.sub(r"<[^>]+>", "", text).strip()


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    attributions = []
    downloaded = 0
    errors = 0

    for slug, query in CITIES.items():
        print(f"\n  Searching: {slug} ({query})...")
        try:
            results = search_commons(query)
            if not results:
                print(f"  [WARN] No suitable images found for {slug}")
                errors += 1
                continue

            best = results[0]
            output_path = os.path.join(OUTPUT_DIR, f"{slug}.webp")
            size = download_and_resize(best["url"], output_path)

            artist_clean = strip_html(best["artist"])
            attributions.append({
                "city": slug,
                "file": best["title"],
                "license": best["license"],
                "artist": artist_clean,
                "source": best["original_url"],
            })

            downloaded += 1
            size_kb = size // 1024
            print(f"  [OK] {slug}.webp ({size_kb} KB) — {best['license']} by {artist_clean[:50]}")

        except Exception as e:
            errors += 1
            print(f"  [ERR] {slug}: {e}")

    # Write attributions file
    with open(ATTR_FILE, "w") as f:
        f.write("# City Photo Attributions\n\n")
        f.write("All photos sourced from Wikimedia Commons under Creative Commons licenses.\n\n")
        for attr in attributions:
            f.write(f"## {attr['city'].replace('-', ' ').title()}\n")
            f.write(f"- **File:** {attr['file']}\n")
            f.write(f"- **License:** {attr['license']}\n")
            f.write(f"- **Artist:** {attr['artist']}\n")
            f.write(f"- **Source:** {attr['source']}\n\n")

    print(f"\nDone: {downloaded} photos downloaded, {errors} errors")
    print(f"Attributions: {ATTR_FILE}")


if __name__ == "__main__":
    main()
