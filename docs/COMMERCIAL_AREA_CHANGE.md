# Commercial Area Change Observatory

## Purpose

This document defines a cautious method for reconstructing changes in shop-house rows and other commercial areas over time. Initial target areas are Taman Galaxy and the Grand Galaxy City / Grand Galaxy Park commercial surroundings in Bekasi. The target historical window is **2003–present**.

The start year is a research boundary, not a claim that records exist for every year. Gaps must remain visible. Do not manufacture a continuous timeline from scattered sources.

## What is being tracked

Keep four identities separate:

1. **Area** — a named commercial strip, block, row, or survey zone.
2. **Physical unit/site** — a shop-house unit, building, parcel, or stable physical location.
3. **Business/entity** — an operator, tenant, owner, brand, studio, or organization where supported.
4. **Map listing/pin** — a platform record that may be moved, duplicated, renamed, or left behind.

A fifth record, the **dated observation**, connects evidence to one or more of these identities at a particular time.

A unit can host several successive businesses. A business can relocate. A pin can be wrong or stale. Never use a current listing to rewrite historical occupancy.

## Observation dimensions

For each dated observation, capture only what the source supports:

- business/display name and category;
- physical unit/site identifier and observed unit label;
- occupancy/use: occupied observed, apparently vacant, renovation observed, demolished observed, inaccessible, or unknown;
- visible facade/building changes;
- map listing identity and pin status;
- source type, source URL/reference, capture/publication date, event date if independently known;
- observer/reviewer, method, and limitations.

Record a shuttered storefront as a dated observation only. Do not turn one closed-shutter image into a claim of long-term vacancy. A renovation barrier or scaffolding supports a renovation observation, not necessarily a change of ownership or tenant.

## Historical date rules

Distinguish:
- **event date**: when a move, opening, closure, renovation, or other event actually occurred, if known;
- **observation date**: when a field visit or image captured the condition;
- **publication date**: when a webpage, directory, post, or news item was published;
- **valid interval**: a supported period during which a state is known to apply.

If a source only proves that a business existed by a date, record "observed by" or "documented by" that date. Do not invent an opening date. If two observations bracket a change, retain the interval as uncertain rather than selecting an unsupported exact date.

## Evidence hierarchy and caveats

Potential sources include dated field photographs, dated Street View captures, archived business pages, official company pages, dated directories, permits or official notices, local reporting, and first-hand notes. Record the actual source and what it establishes.

A business directory or Google Maps result can suggest a lead but does not by itself prove historical occupancy, current operation, or exact pin accuracy. Conflicting evidence should remain visible. Preserve the original source wording and avoid silently normalizing ambiguous names.

Do not redistribute Street View imagery. Keep lawful references, dates, and factual observation notes.

## Pin verification

Evaluate map-pin placement independently from the business identity and operating status. Suggested values:
- `PIN_MATCH`
- `PIN_OFFSET`
- `PIN_WRONG_LOCATION`
- `PIN_DUPLICATE`
- `PIN_NO_PHYSICAL_EVIDENCE`
- `PIN_UNRESOLVED`
- `PIN_NOT_CHECKED`

Record map provider/listing ID, pin coordinates as supplied, independently supported site coordinates, verification method/date, and evidence. Never derive a pin coordinate from a street number, nearby pin, or apparent sequence. `PIN_NO_PHYSICAL_EVIDENCE` means the examined evidence did not corroborate the claimed site; it does not prove that the business is fictitious.

## Initial geographic separation

Keep Taman Galaxy and the Grand Galaxy commercial area as separate area records unless a documented boundary definition explicitly combines them. Do not assume the same development history, management, street network, or commercial cycle. Subdivide each area into stable survey zones/rows before assigning physical unit IDs.

## Analysis that may eventually be supported

With adequate dated observations, BEO may calculate:
- number of observed business changes per unit over a stated period;
- observed vacancy or renovation episodes;
- category transitions;
- pin mismatch/duplicate rates among pins actually checked;
- evidence coverage by year and area;
- known versus unknown historical intervals.

Every result must report its denominator, observation period, geographic boundary, evidence threshold, duplicate handling, and missing-data limitations.

## Claims not supported by storefront observations alone

Do not infer rent, property value, sales, profit, business survival rate, employment, foot traffic, demand, ownership, reasons for closure, or causes of area decline from photos or map pins. These require separate evidence.

## Current implementation status

This is a methodology/design document. No unit-level historical tenant timeline for 2003–present is asserted or populated by this update.
