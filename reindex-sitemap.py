#!/usr/bin/env python3
"""
Re-index all URLs from expatnetherlandshub.com sitemap via Google Indexing API.
Uses URL_UPDATED to force Google to re-crawl all pages.
"""

import time
import sys
import os
sys.path.insert(0, '/mnt/c/claude/affiliate/venv/lib/python3.12/site-packages')

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

KEY_FILE = '/mnt/c/claude/affiliate/digitalshieldpro/google/digital-shield-pro-efc885dda41f.json'

SITEMAP_URLS = [
    "https://expatnetherlandshub.com/",
    "https://expatnetherlandshub.com/guides/housing/best-cities-netherlands-expats-2026/",
    "https://expatnetherlandshub.com/guides/finance/dutch-tax-return-checklist-expats-2026/",
    "https://expatnetherlandshub.com/guides/finance/how-to-open-bank-account-netherlands-2026/",
    "https://expatnetherlandshub.com/guides/finance/ing-vs-abn-amro-expats-2026/",
    "https://expatnetherlandshub.com/guides/integration/best-dutch-language-courses-2026/",
    "https://expatnetherlandshub.com/guides/daily-life/best-internet-providers-netherlands-2026/",
    "https://expatnetherlandshub.com/guides/finance/dutch-tax-system-expats-guide-2026/",
    "https://expatnetherlandshub.com/guides/housing/moving-to-amsterdam-guide-2026/",
    "https://expatnetherlandshub.com/guides/housing/moving-to-rotterdam-guide-2026/",
    "https://expatnetherlandshub.com/guides/daily-life/ov-chipkaart-guide-expats-2026/",
    "https://expatnetherlandshub.com/guides/finance/best-international-money-transfer-netherlands-2026/",
    "https://expatnetherlandshub.com/guides/housing/finding-housing-netherlands-expats-2026/",
    "https://expatnetherlandshub.com/guides/finance/30-percent-ruling-netherlands-2026/",
    "https://expatnetherlandshub.com/cities/amsterdam/",
    "https://expatnetherlandshub.com/guides/health/best-expat-insurance-netherlands-2026/",
    "https://expatnetherlandshub.com/contact/",
    "https://expatnetherlandshub.com/guides/daily-life/",
    "https://expatnetherlandshub.com/guides/legal/digid-guide-expats-2026/",
    "https://expatnetherlandshub.com/disclaimer/",
    "https://expatnetherlandshub.com/cities/eindhoven/",
    "https://expatnetherlandshub.com/cities/",
    "https://expatnetherlandshub.com/guides/",
    "https://expatnetherlandshub.com/guides/finance/",
    "https://expatnetherlandshub.com/guides/work/freelancer-zzp-guide-netherlands-2026/",
    "https://expatnetherlandshub.com/cities/groningen/",
    "https://expatnetherlandshub.com/guides/health/",
    "https://expatnetherlandshub.com/guides/legal/highly-skilled-migrant-visa-netherlands-2026/",
    "https://expatnetherlandshub.com/guides/housing/",
    "https://expatnetherlandshub.com/guides/integration/",
    "https://expatnetherlandshub.com/cities/leiden/",
    "https://expatnetherlandshub.com/cities/maastricht/",
    "https://expatnetherlandshub.com/guides/housing/moving-to-eindhoven-guide-2026/",
    "https://expatnetherlandshub.com/guides/housing/moving-to-the-hague-guide-2026/",
    "https://expatnetherlandshub.com/guides/housing/moving-to-utrecht-guide-2026/",
    "https://expatnetherlandshub.com/cities/rotterdam/",
    "https://expatnetherlandshub.com/cities/the-hague/",
    "https://expatnetherlandshub.com/cities/utrecht/",
    "https://expatnetherlandshub.com/guides/legal/",
    "https://expatnetherlandshub.com/guides/work/",
    "https://expatnetherlandshub.com/about/",
    "https://expatnetherlandshub.com/services/",
    "https://expatnetherlandshub.com/privacy/",
    "https://expatnetherlandshub.com/guides/housing/cost-of-living-netherlands-2026/",
    "https://expatnetherlandshub.com/guides/daily-life/best-vpn-netherlands-expats-2026/",
    "https://expatnetherlandshub.com/guides/integration/inburgeringsexamen-preparation-guide-2026/",
    "https://expatnetherlandshub.com/guides/daily-life/best-sim-card-netherlands-expats-2026/",
    "https://expatnetherlandshub.com/guides/integration/best-apps-learn-dutch-2026/",
    "https://expatnetherlandshub.com/guides/finance/best-bank-account-expats-netherlands-2026/",
    "https://expatnetherlandshub.com/guides/legal/complete-guide-moving-to-netherlands-2026/",
    "https://expatnetherlandshub.com/guides/health/dutch-health-insurance-guide-expats-2026/",
    "https://expatnetherlandshub.com/tools/30-percent-ruling-calculator/",
    "https://expatnetherlandshub.com/tools/salary-checker/",
    "https://expatnetherlandshub.com/tools/health-insurance-wizard/",
    "https://expatnetherlandshub.com/tools/bank-account-chooser/",
    "https://expatnetherlandshub.com/tools/visa-permit-finder/",
    "https://expatnetherlandshub.com/tools/bsn-planner/",
    "https://expatnetherlandshub.com/tools/insurance-chooser/",
    "https://expatnetherlandshub.com/tools/housing-budget-checker/",
    "https://expatnetherlandshub.com/tools/inburgering-route-builder/",
    "https://expatnetherlandshub.com/tools/diploma-evaluator/",
    "https://expatnetherlandshub.com/tools/cost-of-living-calculator/",
]


def main():
    print(f"=== ExpatNetherlandsHub — Sitemap Re-indexing ===")
    print(f"Total URLs: {len(SITEMAP_URLS)}\n")

    if not os.path.exists(KEY_FILE):
        print(f"ERROR: Key file not found: {KEY_FILE}")
        sys.exit(1)

    credentials = service_account.Credentials.from_service_account_file(
        KEY_FILE,
        scopes=['https://www.googleapis.com/auth/indexing'],
    )
    service = build('indexing', 'v3', credentials=credentials)

    # Also resubmit sitemap via Search Console
    sc_creds = service_account.Credentials.from_service_account_file(
        KEY_FILE,
        scopes=['https://www.googleapis.com/auth/webmasters'],
    )
    sc_service = build('searchconsole', 'v1', credentials=sc_creds)

    submitted = 0
    failed = 0
    errors = []

    for i, url in enumerate(SITEMAP_URLS, 1):
        short = url.replace("https://expatnetherlandshub.com", "")
        print(f"  [{i:02d}/{len(SITEMAP_URLS)}] {short} ... ", end='', flush=True)
        try:
            result = service.urlNotifications().publish(body={
                'url': url,
                'type': 'URL_UPDATED',
            }).execute()
            notify_time = result.get('urlNotificationMetadata', {}).get('latestUpdate', {}).get('notifyTime', 'ok')
            print(f"OK ({notify_time[:19] if len(notify_time) > 19 else notify_time})")
            submitted += 1
        except HttpError as e:
            if e.resp.status == 429:
                print(f"RATE LIMITED — waiting 60s...")
                time.sleep(60)
                # retry once
                try:
                    service.urlNotifications().publish(body={
                        'url': url,
                        'type': 'URL_UPDATED',
                    }).execute()
                    submitted += 1
                    print(f"  [{i:02d}/{len(SITEMAP_URLS)}] {short} ... OK (after retry)")
                except HttpError as e2:
                    failed += 1
                    errors.append((url, str(e2)))
                    print(f"  [{i:02d}/{len(SITEMAP_URLS)}] {short} ... FAILED: {e2}")
            else:
                failed += 1
                errors.append((url, str(e)))
                print(f"FAILED: {e}")
        time.sleep(1)  # stay under quota (200/day, ~3/sec burst)

    # Resubmit sitemap to Search Console
    print(f"\n--- Resubmitting sitemap to Search Console ---")
    try:
        sc_service.sitemaps().submit(
            siteUrl='sc-domain:expatnetherlandshub.com',
            feedpath='https://expatnetherlandshub.com/sitemap.xml',
        ).execute()
        print(f"  Sitemap resubmitted: OK")
    except HttpError as e:
        print(f"  Sitemap resubmit FAILED: {e}")

    print(f"\n=== SUMMARY ===")
    print(f"  Submitted:  {submitted}/{len(SITEMAP_URLS)}")
    print(f"  Failed:     {failed}")
    if errors:
        print(f"\n  Errors:")
        for url, err in errors:
            print(f"    - {url}: {err}")
    print(f"\nDone.")


if __name__ == '__main__':
    main()
