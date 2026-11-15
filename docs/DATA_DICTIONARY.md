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

## Commercial-area and time-series fields (proposed)

| Field | Type | Meaning |
|---|---|---|
| physical_unit_id | string | Stable ID for a physical shop-house unit/site; not a business ID |
| area_id | string | Stable ID for a named commercial area or survey zone |
| unit_label_raw | string/null | Door/unit label exactly as observed; never infer from neighbors |
| business_entity_id | string/null | Stable entity ID only when identity is supported |
| map_listing_id | string/null | Platform listing identifier, if lawfully recorded |
| pin_latitude / pin_longitude | number/null | Coordinates supplied by the map source; keep separate from verified site coordinates |
| pin_status | enum | PIN_MATCH, PIN_OFFSET, PIN_WRONG_LOCATION, PIN_DUPLICATE, PIN_NO_PHYSICAL_EVIDENCE, PIN_UNRESOLVED, PIN_NOT_CHECKED |
| occupancy_status | enum | occupied_observed, apparently_vacant, renovation_observed, demolished_observed, inaccessible, unknown |
| valid_from / valid_to | date/null | Supported interval boundaries; leave null when unknown |
| observed_at | date/time/null | Date the observation was made |
| source_published_at | date/time/null | Publication date of the source, distinct from the event date |
| renovation_status | enum | not_observed, renovation_observed, reported, unknown |
| use_change_status | enum | no_change_observed, change_observed, reported, unknown |
| confidence_note | string | Plain-language evidence limitations; not a fabricated numeric confidence |

These are proposed fields for future normalized tables. They do not imply that the corresponding data have already been collected.

## Controlled values

- `business_model`: `independent`, `chain`, `franchise`, `cooperative`, `public`, `unknown`.
- `operational_status`: `open_observed`, `closed_observed`, `reported_closed`, `unknown`, `not_checked`.
- `verification_status`: `observed`, `partially_verified`, `verified`, `unresolved`, `not_checked`.
- `duplicate_status`: `unique`, `possible_duplicate`, `confirmed_duplicate`, `unresolved`.
- `pin_status`: `PIN_MATCH`, `PIN_OFFSET`, `PIN_WRONG_LOCATION`, `PIN_DUPLICATE`, `PIN_NO_PHYSICAL_EVIDENCE`, `PIN_UNRESOLVED`, `PIN_NOT_CHECKED`.
- `occupancy_status`: `occupied_observed`, `apparently_vacant`, `renovation_observed`, `demolished_observed`, `inaccessible`, `unknown`.

A platform label, star rating, review count, or opening-hours field is not a verification status. A proposed field is not evidence that it has been populated or verified.

## GSV normalized CSV additional fields

| Field | Meaning |
|---|---|
| observation_date_raw | Original date/capture label; retained when it cannot be converted to an exact ISO date |
| rating_raw / review_count_raw / price_range_raw / opening_hours_raw | Source values preserved as text; not treated as current values |
| operational_status_raw / verification_status_raw | Original source status wording |
| mapping_status | `mapped_explicit` or `unmapped_review_required` |

The generated CSV contains 180 source-observation rows, not a unique-business registry. Source categories outside the explicit crosswalk are assigned `UNK-UNK` pending review.
