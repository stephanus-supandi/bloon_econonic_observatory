# Methodology

## 1. Scope

BLOON Economic Observatory (BEO) organizes point-of-interest observations into a transparent local-economic classification system. Its first data layer is derived from BLOON GSV Archaeology survey files.

## 2. Unit of record

The primary unit is an **observation**, not automatically a legal business entity. One business can have multiple observations; one address can contain multiple businesses; one map listing can refer to a different physical frontage. These cases must not be merged without evidence.

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

### Manufacturing and industrial facilities

Use the manufacturing codes only when production, processing, assembly, or material recovery is supported by direct observation or reliable source evidence. A warehouse, showroom, distributor, workshop, or construction site is not automatically a factory. Record the observable product/process where known; otherwise use `MFG-GEN` only when manufacturing activity itself is established. Map an industrial estate/park as a separate geographic/organizational feature from each tenant facility. Do not assume every address inside an industrial estate is a factory, and do not infer production capacity, workforce, output, pollution level, permits, or operating status from a map pin or building appearance.

## 6. Spatial rules

- Never infer latitude/longitude from house-number sequences, nearby pins, street-name similarity, or adjacency alone.
- Preserve blank coordinates.
- Distinguish a storefront point, map pin, parcel/building, and service area.
- Do not infer a business boundary from a photograph or a single Street View frame.
- Keep capture dates distinct; a later listing does not rewrite an earlier image observation.

## 7. Operational status

"Open now" is time-dependent. A listing marked permanently closed is platform metadata until corroborated. Use `reported_closed` or `unknown` where appropriate; do not silently convert a user report into a verified closure.

## 8. Economic interpretation

Observed co-location can motivate a hypothesis about clustering or competition. It does not by itself establish causation, demand, turnover, profitability, employment, market share, or supplier relationships.

Counts must state:
- geographic boundary,
- observation period,
- inclusion/exclusion criteria,
- verification threshold,
- treatment of duplicates,
- whether count means observations, matched listings, or distinct businesses.

## 9. Source and licensing

Keep source repository, path, blob SHA, row number, and observation date where available. Do not redistribute Google Street View imagery. Store factual notes and lawful references rather than copied imagery.

## 10. Reproducibility

Every transformation should be repeatable and documented. Raw source snapshots are immutable; corrections belong in a new normalized or correction layer with a reason and provenance.
