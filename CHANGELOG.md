# Changelog

## 2026-11-16 — v0.1 foundation

- Initialized BLOON Economic Observatory from BLOON GSV Archaeology.
- Imported three raw source CSV snapshots without modifying their contents.
- Added an initial business-category taxonomy, methodology, data dictionary, and JSON Schema.
- Explicitly separated observations, business identity, classification, and economic analysis.
- No current-business verification, coordinate enrichment, or economic estimates performed.

## 2026-11-16 — taxonomy expansion: manufacturing & industry

- Added manufacturing categories for food, beverages, textiles, leather, wood, paper, chemicals, pharmaceuticals, rubber/plastics, minerals, metals, machinery, electronics, transport equipment, and recycling.
- Added industrial estate/park, industrial support facilities, and industrial services as distinct categories.
- Clarified that warehouses, workshops, distributors, and industrial-estate tenants are not automatically manufacturers.

## 2026-11-16 — taxonomy expansion: financial services

- Expanded the former broad bank/payment/insurance/pawn grouping into distinct financial-service categories.
- Added commercial banks, BPR/BPRS, ATMs/CRM, bank agents, cooperatives, microfinance, leasing/multifinance, factoring, life/general insurance, insurance intermediaries, pawn services, remittance, money changers, payment services, capital-market services, digital lending/fintech, and unresolved financial institutions.
- Added safeguards against confusing an ATM with a bank branch, dealer with finance company, agent with insurer, or payment counter with bank.

## 2026-11-16 — creative media and commercial-area change research

- Added creative-media categories for video production, editing/post-production, podcast and recording studios, livestream/broadcast, multipurpose creator studios, equipment rental, creator-service agencies, and creator education.
- Added a commercial-area change research method for Taman Galaxy and the Grand Galaxy commercial area, with a target reconstruction window of 2003–present.
- Separated physical commercial units/sites, businesses/entities, map listings/pins, and dated observations.
- Added distinct pin-location status values and vacancy/renovation/change-of-use observations.
- Clarified that 2003–present is a research window, not evidence of continuous historical coverage.
- No historical tenant timeline, current occupancy, revenue, or profitability is asserted by this documentation update.

## 2026-11-16 — GSV normalization pipeline

- Verified the three BEO raw snapshots against the source repository by Git blob SHA.
- Added a Python standard-library ingestion/normalization script with pinned source SHA checks.
- Generated 180 normalized source-observation rows in a separate CSV; these are not unique-business counts.
- Added explicit category crosswalk; 37 rows remain `UNK-UNK` for review.
- Preserved source row identity, source blob SHA, raw date/status labels, and row-level source links.
- Avoided automatic `OBSERVED` or open-status promotion; unknown dates and ambiguous categories remain unresolved.
