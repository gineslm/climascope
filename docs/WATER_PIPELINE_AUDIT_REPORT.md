# Climate Refuge / ClimaScope — Water Pipeline Audit Report

**Branch:** `agent/water-pipeline-audit`  
**Scope:** AEMET climate and precipitation acquisition, QC, W2 aggregation, data storage, map scope, progressive acquisition and future qualitative layers.  
**Status:** W2 implemented and locally validated with 13 tests passing after the latest aggregation change.

---

## 1. Purpose and starting objective

The initial objective of this work was to audit and operationalize the water/climate data pipeline around AEMET station observations, with enough provenance and quality information to support later location-level analysis and a map-based application.

The work deliberately stopped short of defining a final Water Score. The current phase establishes the data foundation and makes data quality explicit before any scoring or ranking is applied.

---

## 2. What was done in this conversation

### 2.1 Source registry

The water source registry was repaired and validated. The registry now loads successfully and contains at least the required set of water-related sources.

A malformed YAML entry was diagnosed and corrected. The registry test subsequently passed.

### 2.2 AEMET access and acquisition

AEMET API access was verified with the configured key. A direct daily-data query for station `8416` (Valencia) was validated using the period `2025-01-01` to `2025-01-07`.

The returned AEMET records contain fields such as:

- `fecha`
- `indicativo`
- `tmed`
- `prec`
- `tmin`
- `tmax`
- `sol`

AEMET decimal-comma precipitation values were handled correctly. Explicit `0,0` precipitation is treated as zero precipitation, while missing precipitation remains missing.

### 2.3 Stations audited

Three stations were used as the initial operational sample:

| Station | Location/role | Available period used for audit |
|---|---|---|
| `8416` | Valencia | 2011-01-01 → 2025-12-31 |
| `3195` | Madrid | 2011-01-01 → 2025-12-31 |
| `7012D` | Cartagena | 2016-02-22 → 2025-12-31 |

The acquisition layer produced the expected raw JSON data and explicit `.NO_DATA` markers for unavailable AEMET query windows. This is important because a failed/empty query must not be silently interpreted as a dry period.

### 2.4 Raw precipitation QC

A station-level QC layer was added and exercised. The QC distinguishes:

- target days;
- observed days;
- missing days;
- coverage percentage;
- explicit zero precipitation days;
- positive precipitation days;
- precipitation-missing days;
- first and last observed dates.

The audited results included:

| Station | Target days | Observed days | Missing days | Coverage |
|---|---:|---:|---:|---:|
| `8416` | 5479 | 5479 | 0 | 100.000% |
| `7012D` | 5479 | 3572 | 1907 | 65.194% |
| `3195` | 5479 | 5478 | 1 | 99.982% |

For `7012D`, the effective observation window starts on `2016-02-22`. Within that actual window, the audit showed 29 missing days over 3601 expected days, or 99.195% coverage.

The raw `prec` quality is separate from date coverage. For example, a station can have a date record but a missing precipitation value. These two types of missingness are therefore not collapsed into one metric.

### 2.5 W2 aggregation

A monthly and annual precipitation aggregation layer was implemented.

Outputs are generated as:

```text
data/raw/aemet/3195_precip_monthly.csv
data/raw/aemet/3195_precip_annual.csv

data/raw/aemet/7012D_precip_monthly.csv
data/raw/aemet/7012D_precip_annual.csv

data/raw/aemet/8416_precip_monthly.csv
data/raw/aemet/8416_precip_annual.csv
```

The first implementation incorrectly discarded the whole period total whenever one expected day was missing. This was deliberately changed.

The current semantics are:

- `prcp_observed_total_mm` = sum of precipitation values that are actually observed;
- `expected_days` = calendar days expected in the period;
- `observed_prcp_days` = days with usable precipitation;
- `missing_prcp_days` = expected days without usable precipitation;
- `coverage_pct` = observed/expected;
- `complete` = true only when all expected days have usable precipitation.

Therefore a missing value is **never converted to zero**, but it also does not erase the accumulated precipitation that was actually observed.

This distinction is essential for downstream scoring: the application can use the observed total together with a coverage threshold rather than pretending incomplete data are complete.

### 2.6 Tests

The pipeline now has tests covering:

- source registry loading;
- precipitation parsing;
- decimal comma;
- explicit zero;
- missing precipitation;
- precipitation QC;
- monthly/annual aggregation;
- incomplete periods;
- preservation of observed totals.

The latest local run reported:

```text
13 passed
```

---

## 3. What changed relative to the initial objective

The important architectural change is that the project is no longer treating a station's raw observations as if they were automatically suitable for scoring.

The pipeline now has an explicit progression:

```text
AEMET source
    ↓
raw station observations
    ↓
acquisition/date QC
    ↓
precipitation value QC
    ↓
monthly / annual aggregation
    ↓
coverage-aware analytical inputs
    ↓
future Water Score
```

The Water Score is intentionally **not yet defined**. It should consume the audited W2 products rather than bypassing them.

---

## 4. Should the application interpolate between stations?

### Short answer

**Not at this stage, and not as a default replacement for station observations.**

AEMET stations are point observations. A map can display each station at its geographic coordinates and expose its temporal scope, coverage and data quality. That is the safest first representation.

For a future location-level map, however, there are two different concepts that should remain separate:

1. **Station scope / representativeness** — which locations a station is considered relevant to.
2. **Spatial interpolation** — estimating a climate variable at locations where no station exists.

They should not be conflated.

### Recommended evolution

#### Phase A — station-native map

Show:

- station location;
- station identifier;
- observation period;
- data coverage;
- precipitation/climate summaries;
- data-quality status.

A location query can initially identify the nearest or most relevant stations rather than inventing a value between them.

#### Phase B — station influence area

For visual scope, use an explicit geographic influence model. A simple first version could use a radius, but a more defensible model can use Thiessen/Voronoi-style areas or a distance-weighted influence model.

The scope should eventually consider more than distance because climate representativeness can change strongly with:

- elevation;
- coast vs inland position;
- terrain;
- urban effects;
- mountain barriers;
- prevailing climate regime.

#### Phase C — interpolation, only where justified

Interpolation can later be introduced for selected variables and time scales, but it should be a separate derived product with its own uncertainty/quality metadata.

For example:

```text
station observations
        ↓
validated spatial model
        ↓
estimated grid / location value
        ↓
uncertainty + station support
```

The application should never present an interpolated estimate as if it were a direct station observation.

**Recommendation:** keep raw station observations authoritative and make interpolation an optional derived layer later.

---

## 5. Should all historical data be downloaded in one session?

**No. A progressive acquisition programme is preferable.**

The current experiment already demonstrates why: different stations have different temporal availability and different data quality. Downloading everything for every station before knowing whether a location is analytically promising would create unnecessary volume and work.

### Recommended acquisition strategy

Use a staged pipeline:

#### Stage 1 — candidate discovery

Maintain a registry of candidate stations with:

- station ID;
- coordinates;
- altitude;
- province/region;
- available date range;
- variables available;
- source/provider;
- initial quality indicators.

#### Stage 2 — promising stations

Prioritize stations that have:

- long historical coverage;
- good completeness;
- useful precipitation and temperature variables;
- geographic relevance to promising locations;
- stable source availability.

#### Stage 3 — progressive historical acquisition

Download in bounded windows rather than attempting the entire universe at once.

The existing reuse behaviour is valuable here: already downloaded windows can be reused and `.NO_DATA` windows can be recorded explicitly.

#### Stage 4 — QC before promotion

A station should not automatically become an analytical station merely because data were downloaded. It should move through a state such as:

```text
candidate
  ↓
partially acquired
  ↓
QC complete
  ↓
analytically usable
  ↓
priority / promoted
```

This makes the system scalable and avoids doing expensive work for locations that will never enter the shortlist.

---

## 6. Where are the data stored?

The current implementation stores the AEMET raw and derived data under:

```text
data/raw/aemet/
```

The important products are:

### Raw station data

JSON files contain the downloaded AEMET station observations. They are the source-level evidence from which later products are derived.

### No-data evidence

Files ending in:

```text
.NO_DATA
```

record query windows for which usable data were not returned. These should be retained as provenance rather than deleting them.

### QC products

The precipitation QC products are stored under the same AEMET data area, including station-level and annual QC outputs produced by the audit tooling.

### W2 products

The current W2 CSV products are:

```text
data/raw/aemet/<station>_precip_monthly.csv
data/raw/aemet/<station>_precip_annual.csv
```

These are **derived analytical tables**, not replacements for the raw observations.

### Recommended future separation

As the application grows, the repository should evolve toward a clearer separation such as:

```text
data/
  raw/
    aemet/
  processed/
    climate/
    water/
  derived/
    map_layers/
    scores/
  reports/
```

The exact migration should be done deliberately rather than prematurely. The current `data/raw/aemet/` layout is useful for the audit stage because it keeps source evidence close to the station acquisition process.

For the eventual web application, large raw datasets should not necessarily be loaded directly by the frontend. A backend/database or precomputed analytical store should serve the map and detail views.

---

## 7. How should the map use the data?

The future map should have at least two layers of information.

### Station layer

Each station marker can expose:

```text
station_id
coordinates
available period
coverage
precipitation summary
climate summary
QC status
```

### Location/area layer

A location can then expose:

```text
candidate location
↓
relevant stations
↓
station evidence
↓
derived climate/water indicators
↓
other evidence layers
↓
final suitability analysis
```

This is preferable to storing only one opaque score because it keeps the analysis explainable.

---

## 8. What about future layers that are not station-based?

This is an important distinction.

Not every future analytical layer needs to come from a physical observation station or a numeric time series.

Some future evidence may be:

- official reports;
- planning documents;
- environmental assessments;
- infrastructure plans;
- drought/water-management documents;
- local or regional administrative information;
- qualitative evidence about constraints or risks.

These should be treated as a **separate evidence class**, rather than forcing them into the AEMET station model.

### Recommended evidence architecture

A location could eventually have:

```text
Location
│
├── Quantitative observations
│   ├── climate
│   ├── precipitation
│   ├── water
│   └── other measured variables
│
├── Derived quantitative indicators
│   ├── coverage-aware aggregates
│   ├── trends
│   └── scores
│
└── Documentary evidence
    ├── official reports
    ├── planning documents
    ├── environmental evidence
    └── qualitative assessments
```

Documentary evidence should have its own provenance fields, for example:

- source title;
- issuing organisation;
- publication date;
- URL/file reference;
- geographic scope;
- evidence type;
- relevance to the location;
- extraction date;
- confidence/quality;
- analyst note.

The application should be able to distinguish **measured fact**, **derived metric** and **documentary assessment**.

---

## 9. Should qualitative research be performed for every location?

**No. It should be progressive and priority-driven.**

The proposed workflow is:

```text
broad quantitative screening
        ↓
identify promising candidates
        ↓
deeper quantitative QC
        ↓
documentary / qualitative research
        ↓
final shortlist
```

This avoids spending significant research time on every location before the quantitative layers have identified whether a location is worth deeper investigation.

However, the system should record the **absence of research** explicitly. “No documentary assessment yet” is different from “no risk found.”

A useful state model would be:

```text
not_assessed
in_research
assessed
insufficient_evidence
```

That prevents a missing report from accidentally becoming a positive signal.

---

## 10. Proposed future data model

A useful conceptual model is:

```text
Station
  ├── Source
  ├── Location
  ├── Observation series
  ├── Acquisition windows
  └── QC

Location / Candidate
  ├── Geographic scope
  ├── Relevant stations
  ├── Quantitative indicators
  ├── Documentary evidence
  └── Final assessment

Evidence
  ├── quantitative_observation
  ├── derived_metric
  └── documentary_source
```

This structure allows the eventual application to answer both:

> “What does the map say about this location?”

and:

> “Why does the map say that?”

---

## 11. Recommended next implementation steps

### Immediate

1. Keep W2 as the validated precipitation foundation.
2. Commit/version the regenerated W2 outputs according to the repository data policy.
3. Define the coverage thresholds that downstream indicators will use.
4. Do not interpolate yet.

### Next engineering phase

5. Build a station catalogue/index suitable for the map.
6. Add station coordinates and metadata to the analytical view.
7. Implement a first station influence/scope model without pretending it is interpolation.
8. Create a progressive acquisition job that prioritises promising stations and downloads bounded time windows.

### Analytical phase

9. Define the Water Score from coverage-aware inputs.
10. Add other quantitative environmental layers.
11. Add a documentary evidence model for qualitative/official sources.
12. Trigger deeper documentary research only for shortlisted/promising locations.

### Application phase

13. Expose station and location evidence through a backend/API.
14. Build the map as a visualization of evidence rather than as a replacement for the evidence.
15. Make every derived score traceable back to source observations or documents.

---

## 12. Current conclusion

The current phase should be considered a **data foundation and audit phase**, not yet a final suitability-ranking system.

The most important decisions made are:

- raw station observations remain authoritative;
- missing precipitation is not converted into zero;
- observed totals are preserved even when coverage is incomplete;
- data quality travels with the aggregate;
- interpolation is deferred until its assumptions can be validated;
- acquisition should be progressive rather than exhaustive;
- qualitative/documentary evidence is a separate evidence class;
- deeper documentary research should be prioritised for promising locations;
- no evidence should be interpreted as positive evidence merely because research has not yet been performed.

This gives the future ClimaScope application a defensible progression from raw observations to map, indicators and ultimately location-level assessment.
