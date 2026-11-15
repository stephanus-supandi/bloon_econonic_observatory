# Normalized data layer

The raw GSV snapshots remain unchanged. Derived rows retain source repository, file, blob SHA, row number, and source-row URL.

## Current generated dataset

- `gsv_normalized_observations.csv` — 180 normalized source rows from the three frozen GSV CSV snapshots.
- `gsv_normalization_report.md` — input provenance, category crosswalk summary, and limitations.

The 180 rows are **not** a count of unique businesses. Identity resolution and duplicate handling remain separate tasks. Ambiguous categories are retained as `UNK-UNK` for review. No automatic current-open or verified status is assigned.

## Rebuild

From the BEO repository root:

```powershell
python scripts/normalize_gsv_to_beo.py
```

The script uses only the Python standard library and refuses to run if an input snapshot's Git blob SHA differs from the pinned source version.

## Future tables

- `business_entities.csv` — entities only when identity evidence supports a stable match.
- `observation_entity_links.csv` — explicit, reviewable links between observations and entities.
- `classification_decisions.csv` — raw category, assigned taxonomy code, decision status, rationale, reviewer, and date.

Do not create a distinct-business count until duplicate and identity rules are documented.
