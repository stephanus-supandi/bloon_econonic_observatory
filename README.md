# BLOON Economic Observatory

**Local Business & Economic Activity Mapping**  
A data-first observatory derived from the field-survey discipline of [BLOON GSV Archaeology](https://github.com/stephanus-supandi/bloon_gsv_survey).

> **GOBLOK BOLEH. NGARANG JANGAN.**

## Purpose

BLOON Economic Observatory (BEO) organizes observed business and service locations into a consistent local-economic taxonomy. It starts from the existing GSV survey records, preserves their provenance, and adds a controlled classification layer for retail, food and beverage, automotive, logistics, manufacturing and industry, financial services, property, creative media, professional services, infrastructure, and other activities.

BEO also aims to reconstruct changes in commercial areas over time: business turnover, vacancies, renovations, changes of use, and map-pin accuracy. The initial historical research window for Taman Galaxy and the Grand Galaxy commercial area is **2003–present**. This is a target period for reconstruction, not a claim that continuous historical records already exist.

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
│   ├── taxonomy/
│   │   └── business_category_taxonomy.csv
│   └── normalized/
│       ├── gsv_normalized_observations.csv
│       └── gsv_normalization_report.md
├── docs/
│   ├── DATA_DICTIONARY.md
│   ├── METHODOLOGY.md
│   └── COMMERCIAL_AREA_CHANGE.md
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
| Manufacturing & industry | food processing, textiles, chemicals, plastics, metals, machinery, electronics, automotive assembly, recycling |
| Industrial areas & support | industrial estates, shared utilities, industrial maintenance, testing and calibration |
| Personal services | barber, salon, laundry, fitness, repair |
| Health & care | clinic, doctor, pharmacy, laboratory, veterinary |
| Education | school, tutoring, course, music studio, creator training |
| Financial services | commercial banks, BPR/BPRS, ATMs, bank agents, cooperatives, microfinance, leasing, multifinance, insurance, pawnshops, remittance, money changers, payment services, capital markets, fintech |
| Finance & administration | payment counters, bill payment and administrative services (retain only where not better classified as a financial service) |
| Property & construction | property agent, developer, contractor, building materials, home services |
| Creative media & production | video production, editing, podcast/recording studio, livestream, creator studio, equipment rental, creator services |
| Professional services | legal, notary, accounting, consulting |
| Hospitality & recreation | hotel, lodging, sports venue, entertainment |
| Public & community | public facilities, worship, community organizations |
| Infrastructure & utilities | fuel station, water refill, energy, telecom infrastructure |
| Unknown / unresolved | visible location whose business identity or activity is not established |

The taxonomy is a controlled vocabulary, not a claim that every observed location has been independently verified.

## Commercial-area change research

The commercial-area timeline treats a **physical unit/site**, a **business/entity**, a **map listing/pin**, and an **observation at a particular date** as separate records. A shop-house unit may host several businesses over time; one business may move; one pin may be misplaced, duplicated, or left behind after a tenant changes.

Initial research focus:
- Taman Galaxy commercial strips and shop-house rows.
- Grand Galaxy City / Grand Galaxy Park surrounding commercial areas, recorded as a distinct geographic area where appropriate.
- Historical window: 2003–present, with gaps explicitly retained.

Track business/category changes, vacancy, renovation, physical-use changes, pin-location checks, and evidence dates. See [Commercial Area Change Method](docs/COMMERCIAL_AREA_CHANGE.md).

## Evidence and status rules

BEO inherits the GSV project's evidence discipline:

1. **OBSERVED** — a visible sign, storefront, facility, or other directly recorded feature.
2. **MATCHED** — a location/entity link supported by adequate identity evidence.
3. **INFERRED** — an analytical interpretation; never silently promoted to fact.
4. **UNKNOWN** — unresolved identity, activity, address, or status remains unresolved.
5. **NOT_CHECKED** — no verification action has been performed.

Business listing labels and map pins are metadata, not ground truth. A sign or a listing alone does not prove legal ownership, current operation, turnover, employee count, or corporate affiliation.

Do not infer coordinates from street names, nearby pins, sequence numbers, or visual adjacency. Keep missing latitude/longitude blank. Record pin accuracy separately from business identity and operational status.

## Initial scope

The first import preserves existing survey material covering Blok M, Ancol, Taman Galaxy, and Kranji. The initial project focus can expand geographically only when new observations and provenance are supplied.

## GSV ingestion and normalization

Run from the BEO repository root with Python 3.10+ (standard library only):

\`\`\`powershell
python scripts/normalize_gsv_to_beo.py
\`\`\`

The script checks the three frozen source Git blob SHAs before producing the normalized CSV. It uses an explicit category crosswalk, preserves source row IDs and raw date/status labels, and leaves ambiguous categories as `UNK-UNK`. See [normalization report](data/normalized/gsv_normalization_report.md).

## Planned workflow

1. Preserve raw GSV source snapshots.
2. Validate file structure and source provenance.
3. Map source categories to BEO taxonomy without overwriting raw categories.
4. Create normalized observation records with source-row references.
5. Separate physical observations, map metadata, business identity, and analytical hypotheses.
6. Reconstruct commercial-unit timelines only where dated evidence supports them.
7. Produce descriptive summaries only from records whose inclusion criteria are explicit.

## Important limitations

- Google Maps / Street View coverage is incomplete and changes over time.
- A listing is not proof that a business is currently open or that its pin is physically accurate.
- A visible sign is not proof of ownership or legal entity identity.
- Co-location does not establish a supply-chain relationship or causal economic effect.
- Counts are counts of records under a stated filter, not automatically counts of active businesses.
- Ratings, review counts, hours, and price ranges are platform/user-supplied observations with their own timestamps and provenance.
- Do not redistribute Street View imagery. Store observation notes and lawful references instead.
- Do not infer revenue, profit, class size, creator income, or business success from social-media presence, equipment, or asking prices.

## Status

**v0.1 — foundation scaffold and source-data import, with expanded taxonomy and commercial-area research method.** No live business verification, automated map scraping, historical census, or financial estimation is claimed.

## Citation

BLOON Economic Observatory — Local Business & Economic Activity Mapping, 2026.  
Derived from BLOON GSV Archaeology survey material, with source lineage retained.
