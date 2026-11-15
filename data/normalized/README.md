# Normalized data layer

Reserved for BEO-derived tables. The raw GSV snapshots remain unchanged.

Planned tables:
- `observations.csv` — one row per source observation, retaining source file and row identity.
- `business_entities.csv` — entities only when identity evidence supports a stable match.
- `observation_entity_links.csv` — explicit, reviewable links between observations and entities.
- `classification_decisions.csv` — raw category, assigned taxonomy code, decision status, rationale, reviewer, and date.

Do not create a distinct-business count until duplicate and identity rules are documented.
