# BLOON Economic Observatory

**Local Business & Economic Activity Mapping**  
A data-first observatory derived from the field-survey discipline of [BLOON GSV Archaeology](https://github.com/stephanus-supandi/bloon_gsv_survey).

> **GOBLOK BOLEH. NGARANG JANGAN.**

## Purpose

BLOON Economic Observatory (BEO) organizes observed business and service locations into a consistent local-economic taxonomy. It starts from the existing GSV survey records, preserves their provenance, and adds a controlled classification layer for retail, food and beverage, automotive, logistics, health, education, property, professional services, infrastructure, and other activities.

This repository is a research dataset and methodology scaffold, not a census, business registry, legal property map, or proof of commercial activity.

## Relationship to BLOON GSV Survey

The initial data lineage is:

- Source repository: `stephanus-supandi/bloon_gsv_survey`
- Source branch: `master`
- Source files: `BLOON_MAP_Taman_Galaxy_master.csv`, `survey_log.csv`, and `kranji_master_41_poi.csv`
- Source snapshots are copied into `data/raw/` without silently rewriting their original rows.
- New BEO classifications belong in separate normalized datasets. The source GSV records remain the historical observation layer.

## Repository layout

```
.
├── README.md
├── CHANGELOG.md
├── data/
│   ├── README.md
│   ├── raw/
│   │   ├── BLOON_MAP_Taman_Galaxy_master.csv
│   │   ├── survey_log.csv
│   │   └── kranji_master_41_poi.csv
│   ├── taxonomy/
│   │   └── business_category_taxonomy.csv
│   └── normalized/
│       └── README.md
├── docs/
│   ├── DATA_DICTIONARY.md
│   └── METHODOLOGY.md
└── schema/
    └── business_observation.schema.json
```

## Core classification domains

| Domain | Examples |
|---|---|
| Retail & trade | minimarket, grocery, clothing, hardware, phone shop |
| Food & beverage | restaurant, warung, cafe, bakery, catering |
| Automotive & mobility | workshop, tire shop, detailing, fuel retail, rental |
| Logistics & supply chain | courier, postal, freight, drop point, warehouse, fulfillment, distribution, cold chain |
| Personal services | barber, salon, laundry, fitness, repair |
| Health & care | clinic, doctor, pharmacy, laboratory, veterinary |
| Education | school, tutoring, course, music studio |
| Finance & administration | bank, ATM, pawn, money transfer, insurance |
| Property & construction | property agent, contractor, building materials, home services |
| Professional services | legal, notary, accounting, consulting |
| Hospitality & recreation | hotel, lodging, sports venue, entertainment |
| Public & community | public facilities, worship, community organizations |
| Infrastructure & utilities | fuel station, water refill, energy, telecom infrastructure |
| Unknown / unresolved | visible location whose business identity or activity is not established |

The taxonomy is a controlled vocabulary, not a claim that every observed location has been independently verified.

## Evidence and status rules

BEO inherits the GSV project's evidence discipline:

1. **OBSERVED** — a visible sign, storefront, facility, or other directly recorded feature.
2. **MATCHED** — a location/entity link supported by adequate identity evidence.
3. **INFERRED** — an analytical interpretation; never silently promoted to fact.
4. **UNKNOWN** — unresolved identity, activity, address, or status remains unresolved.
5. **NOT_CHECKED** — no verification action has been performed.

Business listing labels and map pins are metadata, not ground truth. A sign or a listing alone does not prove legal ownership, current operation, turnover, employee count, or corporate affiliation.

Do not infer coordinates from street names, nearby pins, sequence numbers, or visual adjacency. Keep missing latitude/longitude blank.

## Initial scope

The first import preserves existing survey material covering Blok M, Ancol, Taman Galaxy, and Kranji. The initial project focus can expand geographically only when new observations and provenance are supplied.

## Planned workflow

1. Preserve raw GSV source snapshots.
2. Validate file structure and source provenance.
3. Map source categories to BEO taxonomy without overwriting raw categories.
4. Create normalized observation records with source-row references.
5. Separate physical observations, map metadata, business identity, and analytical hypotheses.
6. Produce descriptive summaries only from records whose inclusion criteria are explicit.

## Important limitations

- Google Maps / Street View coverage is incomplete and changes over time.
- A listing is not proof that a business is currently open.
- A visible sign is not proof of ownership or legal entity identity.
- Co-location does not establish a supply-chain relationship or causal economic effect.
- Counts are counts of records under a stated filter, not automatically counts of active businesses.
- Ratings, review counts, hours, and price ranges are platform/user-supplied observations with their own timestamps and provenance.
- Do not redistribute Street View imagery. Store observation notes and lawful references instead.

## Status

**v0.1 — foundation scaffold and source-data import.** No live business verification, automated map scraping, economic census, or financial estimation is claimed.

## Citation

BLOON Economic Observatory — Local Business & Economic Activity Mapping, 2026.  
Derived from BLOON GSV Archaeology survey material, with source lineage retained.
