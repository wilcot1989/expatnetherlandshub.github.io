---
title: "Free Expat Data API — Netherlands 2026"
date: 2026-03-17T10:00:00+01:00
lastmod: 2026-03-17T10:00:00+01:00
description: "Free JSON API with Dutch salary and cost of living data for developers building expat tools, relocation apps, and salary calculators."
categories: ["tools", "finance"]
tags: ["netherlands salary api", "cost of living api", "expat data api", "dutch salary data", "netherlands cost of living json", "developer api netherlands"]
keywords: ["netherlands salary api", "cost of living netherlands json", "expat data api free", "dutch salary data 2026", "netherlands housing costs developer", "free attribution api netherlands"]
author: "Sarah van den Berg"
author_bio: "Expat coach and relocation specialist. Half Dutch, half British, living in the Netherlands for over 10 years."
featured_image: "/images/categories/finance.svg"
---

If you are building a relocation tool, salary calculator, or cost-of-living comparison app and you need clean data on the Netherlands, you can use the endpoints below for free. No API key required. No rate limits. Just link back to us as your source.

---

## Available Endpoints

Both endpoints return static JSON hosted at `expatnetherlandshub.com`. They are updated when underlying figures change (tax brackets, minimum wage, market rents).

### Salaries

```
GET https://expatnetherlandshub.com/api/v1/salaries.json
```

Returns:

- Average gross and estimated net salary **by city** (Amsterdam, Rotterdam, Den Haag, Utrecht, Eindhoven, Groningen)
- Salary ranges by **seniority level** for 6 sectors (Software Engineering, Data Science, Finance/Banking, Consulting, Marketing, Engineering)
- **Minimum wage** 2026 (monthly, age 21+)
- **30% ruling** income threshold
- **Tax brackets** with rates

Source page: [Netherlands Salary Comparison](/salary-comparison/)

---

### Cost of Living

```
GET https://expatnetherlandshub.com/api/v1/cost-of-living.json
```

Returns per city (Amsterdam, Rotterdam, Utrecht, Eindhoven, Groningen):

- Rent ranges for 1-bedroom and 2-bedroom apartments (EUR/month)
- Monthly grocery costs for a single person
- Monthly public transport pass cost
- Monthly health insurance cost

Source page: [Expat Statistics Netherlands](/statistics/)

---

## Usage Examples

### JavaScript (fetch)

```javascript
// Salary data
fetch('https://expatnetherlandshub.com/api/v1/salaries.json')
  .then(res => res.json())
  .then(data => {
    const cities = data.data.by_city;
    cities.forEach(c => {
      console.log(`${c.city}: €${c.avg_gross.toLocaleString()} gross`);
    });
  });

// Cost of living data
fetch('https://expatnetherlandshub.com/api/v1/cost-of-living.json')
  .then(res => res.json())
  .then(data => {
    const amsterdam = data.data.by_city.find(c => c.city === 'Amsterdam');
    console.log(`Amsterdam 1-bed rent: €${amsterdam.rent_1bed.min}–€${amsterdam.rent_1bed.max}/month`);
  });
```

### Python (requests)

```python
import requests

# Salary data
r = requests.get('https://expatnetherlandshub.com/api/v1/salaries.json')
data = r.json()

for city in data['data']['by_city']:
    print(f"{city['city']}: €{city['avg_gross']:,} gross / €{city['avg_net_est']:,} net (est.)")

# Cost of living
r = requests.get('https://expatnetherlandshub.com/api/v1/cost-of-living.json')
col = r.json()

for city in col['data']['by_city']:
    rent = city['rent_1bed']
    print(f"{city['city']}: 1-bed €{rent['min']}–€{rent['max']}/month")
```

---

## Response Format

Each response includes top-level metadata alongside the data:

```json
{
  "source": "ExpatNetherlandsHub.com",
  "source_url": "https://expatnetherlandshub.com/salary-comparison/",
  "last_updated": "2026-03-17",
  "license": "Free to use with attribution link to source_url",
  "data": { ... }
}
```

The `source_url` field points directly to the page where the data originates — this is the URL you should use for your attribution link.

---

## Attribution Requirement

The data is free to use. The one requirement is that you include a visible link to ExpatNetherlandsHub.com as your data source — either to the homepage or to the specific `source_url` returned in the response.

Example attribution:

```html
Data source: <a href="https://expatnetherlandshub.com/salary-comparison/">ExpatNetherlandsHub.com</a>
```

That is it. No registration, no API key, no licence fee.

---

## Data Notes

- **Salary figures** are gross annual amounts in EUR. Net estimates assume a standard employee without the 30% ruling. Actual net pay varies based on personal deductions, housing benefit, and other factors.
- **Rent ranges** reflect the private rental market in each city as of early 2026. They exclude social housing (which has long waiting lists for most expats).
- **Health insurance** costs are for basic mandatory Dutch health insurance (basisverzekering). Expats on certain visa types may have different requirements.
- All amounts are in **EUR**.
- Data is updated when official figures change (typically January each year for tax brackets and minimum wage; quarterly for housing markets).

---

## Questions or Corrections

If you spot an error in the data or want to request additional fields, contact us via the [contact page](/contact/). We will consider adding new endpoints (e.g., 30% ruling calculator output, housing by neighbourhood) if there is demand.
