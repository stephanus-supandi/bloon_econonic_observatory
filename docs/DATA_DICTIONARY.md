# Data Dictionary

## Design rule

Keep the original source fields intact. Normalized BEO fields are additional interpretation, never replacements for source observations.

## Core normalized observation fields

| Field | Type | Meaning |
|---|---|---|
| observation_id | string | Stable unique ID for this observation record |
| source_repository | string | Repository that supplied the source record |
| source_file | string | Original source file path |
| source_blob_sha | string | Git blob SHA of imported source file |
| source_record_id | string | Original record ID or row number |
| source_row_number | integer | 1-based data row number, excluding header |
| name_raw | string | Name exactly as supplied by source |
| category_raw | string | Original category exactly as supplied |
| category_code | string | BEO taxonomy code; may remain UNKNOWN |
| brand_raw | string | Brand string only when explicitly observed |
| business_model | string | independent, chain, franchise, cooperative, public, unknown |
| location_raw | string | Original address/location note |
| latitude | number/null | Coordinate only when sourced and verified |
| longitude | number/null | Coordinate only when sourced and verified |
| observation_date | string/null | Date of observation, not assumed current status |
| operational_status | string | open_observed, closed_observed, reported_closed, unknown, not_checked |
| verification_status | string | observed, partially_verified, verified, unresolved, not_checked |
| evidence_type | string | signage, storefront, street_view, map_listing, user_note, official_source, field_visit, other |
| evidence_reference | string/null | URL or stable reference to supporting evidence |
| duplicate_status | string | unique, possible_duplicate, confirmed_duplicate, unresolved |
| notes | string | Explicit limitations and context |

## Controlled values

- `business_model`: `independent`, `chain`, `franchise`, `cooperative`, `public`, `unknown`.
- `operational_status`: `open_observed`, `closed_observed`, `reported_closed`, `unknown`, `not_checked`.
- `verification_status`: `observed`, `partially_verified`, `verified`, `unresolved`, `not_checked`.
- `duplicate_status`: `unique`, `possible_duplicate`, `confirmed_duplicate`, `unresolved`.

A platform label, star rating, review count, or opening-hours field is not a verification status.
