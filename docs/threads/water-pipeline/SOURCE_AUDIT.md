# Water source audit — W0/W1 initial

## Scope

This document records the first source audit for the water pipeline. It does not define a Water Score and does not approve any CRS indicator.

The audit follows the project rule that acquisition, QC, transformation and indicator design remain separate. Missing data is not converted to zero, and no interpolation is introduced at this stage.

## Verified source families

| source_id | provider | variable | access | current status | main limitation |
|---|---|---|---|---|---|
| `aemet_precipitation` | AEMET | precipitation | OpenData REST API | source verified; acquisition pending | station/period coverage must be measured; API key required |
| `snczi_flood` | MITECO | flood exposure | viewer + downloads/WMS | source verified; reproducible download pending | mapped coverage varies by layer and not all flood-prone areas are mapped |
| `water_bodies_surface` | MITECO | surface water | GIS downloads/WMS | source verified; reproducible download pending | inventory is not a supply-security measure |
| `water_bodies_groundwater` | MITECO | groundwater | GIS downloads/WMS | source verified; reproducible download pending | presence does not imply exploitable or secure supply |
| `drought` | MITECO / basin authorities | drought/scarcity | official plans and basin services | source family verified; indicator audit pending | drought and scarcity are distinct concepts |
| `reservoirs` | MITECO / basin authorities | regulation/storage | GIS + operational basin data | source verified; series audit pending | inventory count must not become a CRS score |
| `supply_systems` | competent providers | supply system | case-by-case | not automated | system boundaries and public data availability vary |

## Benchmark scope

Initial benchmark territories are:

- Valencia — AEMET station `8416`
- Cartagena — AEMET station `7012D`
- Madrid-Retiro — AEMET station `3195`

These are the benchmark locations already used by the climate pipeline.

## Source-specific findings

### AEMET precipitation

AEMET OpenData provides a REST API intended for reusable/programmatic access to the published catalogue. The existing repository already has a daily climatology downloader, so the water pipeline should not duplicate or modify the thermal pipeline unnecessarily.

The immediate W1 task is to acquire/inspect precipitation for the three benchmark stations and report:

- temporal coverage;
- record count;
- nulls;
- explicit zeros;
- positive values;
- monthly totals;
- annual totals;
- basic plausibility checks.

A missing precipitation value remains missing. It is never interpreted as `0`.

### SNCZI

MITECO provides the national flood-cartography system and official downloads. The download catalogue includes flood zones for return periods T=10, T=50, T=100 and T=500 years and ARPSIs. The first implementation should verify one reproducible download path and record its layer/version metadata before any exposure calculation.

MITECO explicitly warns that not all flood-prone areas in Spain are currently mapped. Therefore absence of a mapped polygon cannot be treated as proof of absence of flood hazard.

### Surface and groundwater bodies

MITECO publishes the 2022–2027 hydrological-planning-cycle water-body cartography, including surface and groundwater bodies and status layers. These datasets are useful evidence for resource/system context, but the mere presence of a water body is not a water-security indicator.

### Drought and scarcity

MITECO's current drought-management material distinguishes drought management from scarcity and provides basin-level Special Drought Plans. The implementation must preserve this distinction. No composite drought/scarcity indicator is approved by this audit.

### Reservoirs

MITECO's water-services catalogue exposes national inventory/GIS layers for reservoirs and dams. Operational storage series need a separate basin/source audit. Counting reservoirs is not an accepted proxy for water security.

### Supply systems

The supply-system layer remains intentionally non-automated. The benchmark work should map, for each territory, the actual supply system, sources, infrastructure and external resources before any dependency metric is proposed.

## Provenance

Every acquired dataset must later carry at least:

```text
source_id
provider
dataset
retrieval_date
source_url
access_method
raw_file
transformation
quality_status
limitations
```

The intended data lineage is:

```text
raw -> clean -> derived
```

No derived CRS indicator belongs in this phase.
