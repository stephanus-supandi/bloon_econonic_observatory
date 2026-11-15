# Methodology

## 1. Scope

BLOON Economic Observatory (BEO) organizes point-of-interest observations into a transparent local-economic classification system. Its first data layer is derived from BLOON GSV Archaeology survey files. An additional research stream reconstructs commercial-area change over time, initially targeting Taman Galaxy and the Grand Galaxy commercial area from 2003 to the present. This is a target period, not a claim of complete historical coverage.

## 2. Unit of record

The primary unit is an **observation**, not automatically a legal business entity. One business can have multiple observations; one address can contain multiple businesses; one map listing can refer to a different physical frontage. These cases must not be merged without evidence.

For commercial-area history, keep these entities distinct:
- **Physical unit/site**: a shop-house unit, building, parcel, or other stable physical location.
- **Business/entity**: the operator, tenant, owner, brand, or organization, where identity is supported.
- **Map listing/pin**: a platform record and its stated coordinates/name/category.
- **Observation**: a dated record of what was visible, reported, or documented at a point in time.
- **Evidence item**: a dated photo, field note, archived page, official record, directory entry, or other source supporting an observation.

A physical unit may host successive businesses; a business may move between units; a single business may have multiple outlets; and a map pin may persist after a tenant has left. Never treat these as interchangeable IDs.

## 3. Evidence layers

1. **Physical observation** — visible sign, storefront, building feature, vehicle access, or service activity in a dated image/field note.
2. **Platform metadata** — Google Maps name, category, rating, review count, opening hours, or pin location.
3. **Identity match** — a reasoned link between an observation and a business/listing, with supporting evidence.
4. **Classification** — assignment to BEO taxonomy at the narrowest level supported by evidence.
5. **Analysis** — counts, density, clustering, and service coverage under explicit filters.

Do not collapse these layers into a single "verified business" flag.

## 4. Verification vocabulary

- `OBSERVED`: directly visible or explicitly recorded observation.
- `MATCHED`: identity link supported by adequate evidence.
- `PARTIAL`: some attributes supported, other attributes unresolved.
- `HYPOTHESIS`: plausible interpretation requiring further testing.
- `UNKNOWN`: unresolved.
- `NOT_CHECKED`: no verification action performed.

The imported GSV source files use their own legacy status wording. Preserve it in raw snapshots and map it only through a documented crosswalk.

## 5. Classification

Use `data/taxonomy/business_category_taxonomy.csv`. Store both `category_raw` and `category_code`. If the source says "celluler", preserve that spelling in raw data; a normalized classification can be added separately with a note.

Brand and business model are separate dimensions. A familiar brand does not prove the outlet is company-owned or franchised. Record `chain` only when chain affiliation is supported; record `franchise` only when the franchise relationship is evidenced.

### Financial services and institutions

Classify the type of service point or institution that is actually evidenced: commercial bank branch, BPR/BPRS, ATM/CRM, bank agent, cooperative, microfinance, leasing/multifinance, insurer, insurance intermediary, pawn outlet, remittance, money changer, payment service, capital-market office, or digital-finance service.

Keep these distinctions explicit:

- A bank branch, ATM, and bank agent are different observation types.
- A vehicle showroom/dealer is not automatically a leasing or finance company.
- An insurance agent/broker is not the insurance underwriter.
- A payment counter or PPOB outlet is not automatically a bank.
- A pawn outlet should not be described as an official Pegadaian branch unless its identity is supported.
- A fintech app or digital lender may operate without a physical local office; do not invent a storefront.
- A cooperative or microfinance institution is not automatically a bank.
- Do not infer licensing, deposit protection, solvency, loan rates, customer balances, assets, transaction volume, or regulatory status from a sign, map listing, or storefront.

Record the observed service point and the institution/provider separately when evidence allows. Where the exact financial activity is unclear, retain `UNKNOWN` rather than guessing.

### Manufacturing and industrial facilities

Use the manufacturing codes only when production, processing, assembly, or material recovery is supported by direct observation or reliable source evidence. A warehouse, showroom, distributor, workshop, or construction site is not automatically a factory. Record the observable product/process where known; otherwise use `MFG-GEN` only when manufacturing activity itself is established. Map an industrial estate/park as a separate geographic/organizational feature from each tenant facility. Do not assume every address inside an industrial estate is a factory, and do not infer production capacity, workforce, output, pollution level, permits, or operating status from a map pin or building appearance.

### Creative media and content production

Use the creative-media categories for evidenced services or facilities such as video production, filming, editing/post-production, podcast or audio recording, livestream/broadcast, creator-studio rental, equipment rental, talent/creator management, and creator training.

Keep these business models distinct:
- A production house making content for clients is not automatically a creator/influencer agency.
- A podcast room or multipurpose studio may be a rental venue rather than a production company.
- An editing service is not automatically a film-production house.
- A training venue/class is not automatically a continuously operating studio.
- A creator's home or personal channel is not automatically a public commercial studio.
- Equipment visible in a room does not prove that the equipment is rented out or that the business is active.

Do not infer creator income, advertising revenue, subscriber monetization, class enrollment, occupancy, client volume, or profitability from social-media followers, views, equipment, published rates, or promotional claims. Record rates as advertised prices with source/date, not realized revenue.

## 6. Spatial rules and map-pin verification

- Never infer latitude/longitude from house-number sequences, nearby pins, street-name similarity, or adjacency alone.
- Preserve blank coordinates.
- Distinguish a storefront point, map pin, parcel/building, and service area.
- Do not infer a business boundary from a photograph or a single Street View frame.
- Keep capture dates distinct; a later listing does not rewrite an earlier image observation.
- Assess pin accuracy independently from business identity and operating status.

Suggested pin status vocabulary:
- `PIN_MATCH`: pin is supported as matching the relevant physical entrance/site within the stated method and tolerance.
- `PIN_OFFSET`: pin appears displaced from the relevant site; record measured offset only when coordinates and method are available.
- `PIN_WRONG_LOCATION`: evidence supports that the pin points to a different physical location.
- `PIN_DUPLICATE`: duplicate platform listing/pin is supported by comparison; retain both source identifiers.
- `PIN_NO_PHYSICAL_EVIDENCE`: the claimed location could not be physically corroborated in the examined evidence. This does not prove the business is fictitious.
- `PIN_UNRESOLVED`: evidence is insufficient or conflicting.
- `PIN_NOT_CHECKED`: pin accuracy has not been assessed.

Always record the verification date, evidence reference, method, and reviewer/observer where available. A wrong or unsupported pin is a location-data problem, not proof that the named company or business is fictitious.

## 7. Commercial-area change over time

For each physical unit/site, maintain a timeline of dated observations rather than overwriting the current business name. Record, where evidenced:
- business name and category at that date;
- occupancy/use state (occupied, apparently vacant, under renovation, demolished, inaccessible, or unknown);
- visible renovation or facade/use change;
- map listing/pin identity and pin status;
- evidence source, capture/publication date, and confidence/limitations.

Use `docs/COMMERCIAL_AREA_CHANGE.md` for the proposed workflow and record structure. Do not backdate a business start/end date from a single undated image. If evidence only establishes that a business existed by a date, record it as "observed by" that date rather than inventing an opening date. "Vacant" should be used only for the period and view supported by evidence; a closed shutter on one day does not establish long-term vacancy.

## 8. Operational status

"Open now" is time-dependent. A listing marked permanently closed is platform metadata until corroborated. Use `reported_closed` or `unknown` where appropriate; do not silently convert a user report into a verified closure.

## 9. Economic interpretation

Observed co-location can motivate a hypothesis about clustering or competition. It does not by itself establish causation, demand, turnover, profitability, employment, market share, or supplier relationships.

Counts must state:
- geographic boundary,
- observation period,
- inclusion/exclusion criteria,
- verification threshold,
- treatment of duplicates,
- whether count means observations, matched listings, or distinct businesses.

## 10. Source and licensing

Keep source repository, path, blob SHA, row number, and observation date where available. Do not redistribute Google Street View imagery. Store factual notes and lawful references rather than copied imagery.

## 11. GSV normalization pipeline

The current pipeline reads only the three frozen CSV snapshots in `data/raw/`. It verifies each file against a pinned Git blob SHA before transformation. It uses Python's standard library (`csv`, `hashlib`, `pathlib`) and an explicit raw-category crosswalk. Unknown or ambiguous categories map to `UNK-UNK` with `unmapped_review_required`; they are not guessed. Source row IDs, row numbers, blob SHAs, raw date/status labels, and source-row links are retained.

The generated 180 rows represent source records, not distinct businesses. The pipeline does not infer exact dates from month/year labels, does not set all rows to `OBSERVED`, and does not infer current operating status. Rebuild with `python scripts/normalize_gsv_to_beo.py` from the repository root.

## 12. Reproducibility

Every transformation should be repeatable and documented. Raw source snapshots are immutable; corrections belong in a new normalized or correction layer with a reason and provenance.
