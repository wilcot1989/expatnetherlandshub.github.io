#!/bin/bash
# Script to submit URLs to Google for indexing via Search Console API
# Requires: google/service-account-key.json + site verified in Search Console
# Usage: ./index-new-urls.sh

SITE_URL="https://expatnetherlandshub.com"

# Key pages to index
URLS=(
  "/"
  "/tools/"
  "/guides/"
  "/cities/"
  "/tools/30-percent-ruling-calculator/"
  "/tools/salary-checker/"
  "/tools/health-insurance-wizard/"
  "/tools/bank-account-chooser/"
  "/tools/visa-permit-finder/"
  "/tools/bsn-planner/"
  "/tools/insurance-chooser/"
  "/tools/housing-budget-checker/"
  "/tools/inburgering-route-builder/"
  "/tools/diploma-evaluator/"
  "/guides/finance/"
  "/guides/health/"
  "/guides/housing/"
  "/guides/legal/"
  "/guides/work/"
  "/guides/integration/"
  "/guides/daily-life/"
  "/guides/finance/30-percent-ruling-netherlands-2026/"
  "/guides/finance/dutch-tax-system-expats-guide-2026/"
  "/guides/health/dutch-health-insurance-guide-expats-2026/"
  "/guides/housing/finding-housing-netherlands-expats-2026/"
  "/guides/housing/cost-of-living-netherlands-2026/"
  "/guides/legal/complete-guide-moving-to-netherlands-2026/"
  "/cities/amsterdam/"
  "/cities/rotterdam/"
  "/cities/the-hague/"
  "/cities/utrecht/"
  "/cities/eindhoven/"
  "/contact/"
  "/disclaimer/"
  "/about/"
)

echo "=== ExpatNetherlandsHub.com — URL Indexing List ==="
echo "Total URLs to submit: ${#URLS[@]}"
echo ""
echo "Submit these URLs in Google Search Console > URL Inspection > Request Indexing:"
echo ""
for url in "${URLS[@]}"; do
  echo "${SITE_URL}${url}"
done
echo ""
echo "Or use the Google Indexing API with your service account key."
echo "Script: python3 ../google/index-urls.py with these URLs"
