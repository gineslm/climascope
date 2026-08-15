# Climate Refuge / ClimaScope — Water Pipeline Audit Report

**Report version:** 0.3.0  
**Branch:** `agent/water-pipeline-audit`  
**Scope:** AEMET climate and precipitation acquisition, QC, W2 aggregation, data storage, map scope, progressive acquisition, future qualitative layers, and cross-thread documentation.  
**Status:** W2 implemented and locally validated with 13 tests passing after the latest aggregation change.  
**Last updated:** 2026-08-15

---

## 1. Purpose and starting objective

The initial objective of this work was to audit and operationalize the water/climate data pipeline around AEMET station observations, with enough provenance and quality information to support later location-level analysis and a map-based application.

The work deliberately stopped short of defining a final Water Score. The current phase establishes the data foundation and makes data quality explicit before any scoring or ranking is applied.

## 2. Work completed in this phase

### 2.1 Source registry

The water source registry was repaired and validated. A malformed YAML entry was diagnosed and corrected, and the registry test subsequently passed.

### 2.2 AEMET access and acquisition

AEMET API access was verified. A direct daily-data query for station `8416` (Valencia) was validated using `2025-01-01` to `2025-01-07`.

AEMET decimal-comma precipitation values are handled correctly. Explicit `0,0` precipitation is treated as zero precipitation, while missing precipitation remains missing.

### 2.3 Stations audited

| Station | Location/role | Available period used for audit |
|---|---|---|
| `8416` | Valencia | 2011-01-01 → 2025-12-31 |
| `3195` | Madrid | 2011-01-01 → 2025-12-31 |
| `7012D` | Cartagena | 2016-02-22 → 2025-12-31 |

The acquisition layer retains raw JSON data and explicit `.NO_DATA` markers for unavailable query windows. Empty/unavailable windows are therefore evidence, not silent dry periods.

### 2.4 Raw precipitation QC

The station-level QC distinguishes target days, observed days, missing days, coverage, explicit zero precipitation days, positive precipitation days, precipitation-missing days, and first/last observed dates.

Initial audit results:

| Station | Target days | Observed days | Missing days | Coverage |
|---|---:|---:|---:|---:|
| `8416` | 5479 | 5479 | 0 | 100.000% |
| `7012D` | 5479 | 3572 | 1907 | 65.194% |
| `3195` | 5479 | 5478 | 1 | 99.982% |

For `7012D`, the effective observation window starts on `2016-02-22`; within that actual window there are 29 missing days over 3601 expected days (99.195% coverage).

Raw date coverage is separate from `prec` quality: a station can have a date record while precipitation itself is missing.

### 2.5 W2 aggregation

Monthly and annual precipitation aggregation is implemented. Current outputs are:

```text
data/raw/aemet/3195_precip_monthly.csv
data/raw/aemet/3195_precip_annual.csv
data/raw/aemet/7012D_precip_monthly.csv
data/raw/aemet/7012D_precip_annual.csv
data/raw/aemet/8416_precip_monthly.csv
data/raw/aemet/8416_precip_annual.csv
```

The first aggregation semantics discarded an entire period total when one expected day was missing. That was corrected.

Current semantics:

- `prcp_observed_total_mm` = sum of actually observed precipitation values;
- `expected_days` = calendar days expected in the period;
- `observed_prcp_days` = days with usable precipitation;
- `missing_prcp_days` = expected days without usable precipitation;
- `coverage_pct` = observed/expected;
- `complete` = true only when all expected days have usable precipitation.

A missing value is never converted to zero, but it also does not erase precipitation that was actually observed.

### 2.6 Tests

The latest local test run reports:

```text
13 passed
```

Coverage includes source registry loading, precipitation parsing, decimal comma, explicit zero, missing precipitation, precipitation QC, monthly/annual aggregation, incomplete periods and preservation of observed totals.

---

## 3. Changes relative to the initial objective

The architecture is no longer treating a station's raw observations as automatically suitable for scoring.

The current progression is:

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

The Water Score is intentionally not yet defined.

The scope has also expanded from a station-centric pipeline to a location-centric architecture in which stations, locations, spatial representativeness, quantitative indicators and documentary evidence remain distinct.

---

## 4. Station, location and interpolation direction

A station is a physical observation point. A location is the user-facing place/site being evaluated. A station observation must not automatically become the value for every nearby location.

The map should initially show station points, observation periods, coverage and quality. A separate representativeness/scope layer can indicate which locations a station is considered relevant to.

Interpolation is **deferred**. If introduced later, it must be a separate derived product with method, provenance and uncertainty. The application must distinguish:

```text
observed at station
relevant to location
modelled/interpolated for location
```

A future influence model may use a radius, Thiessen/Voronoi-style areas or distance weighting, but climate representativeness may also depend on elevation, terrain, coast/inland position, urban effects and climate regime.

Recommendation: keep raw station observations authoritative and make interpolation an optional derived layer only after its assumptions are validated.

---

## 5. Progressive acquisition strategy

A full historical download for every station is not the preferred operating model. Acquisition should be progressive:

```text
station catalogue
    -> candidate ranking
    -> priority stations
    -> bounded historical acquisition
    -> QC
    -> analytical qualification
    -> promotion
```

Priority should consider historical coverage, completeness, available variables, geographic relevance and source stability. Existing reuse behaviour and `.NO_DATA` evidence should be retained.

A station should move through explicit acquisition/quality states rather than becoming analytically valid merely because data were downloaded.

---

## 6. Data storage

Current AEMET raw and derived data are under:

```text
data/raw/aemet/
```

This includes raw JSON, `.NO_DATA` evidence, QC outputs and W2 CSV products.

The W2 CSV products are derived analytical tables and do not replace the raw observations.

A future separation may evolve toward:

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

The migration should be deliberate and should not disturb the current audit trail unnecessarily.

---

## 7. Quantitative vs documentary evidence

Not every future information layer needs a physical station or numeric time series. The application should support both quantitative and documentary evidence.

Conceptually:

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

Documentary evidence should preserve source title, issuing organisation, publication date, URL/file reference, geographic scope, evidence type, relevance, extraction date and confidence/quality.

Documentary research should be progressive rather than exhaustive. Broad quantitative screening should identify promising candidates before deeper qualitative research. `not_assessed` must never mean `no_risk`.

Suggested documentary assessment states are `not_assessed`, `in_research`, `assessed` and `insufficient_evidence`.

---

## 8. Map architecture direction

The future map should expose two connected layers:

### Station layer

Station marker detail can include:

```text
station_id
coordinates
available period
coverage
precipitation summary
climate summary
QC status
```

### Location layer

A location detail view should be able to expose:

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

The map is therefore a visualization and navigation layer over evidence, not a replacement for the evidence.

---

## 9. Documentation and cross-thread protocol

The repository is the central source of truth for this project. Documentation artifacts must be versioned in GitHub and referenced from the relevant report so different conversation threads can recover the latest state.

Every new-thread handoff document must contain:

- project and repository location;
- working branch;
- access prerequisites;
- current report/documentation version;
- objective and scope;
- established decisions and constraints;
- deliverables;
- validation/tests required;
- files/data that should not be regenerated unnecessarily;
- completion protocol;
- next handoff requirements where applicable.

### Current handoff document

**Version:** 0.1.0  
**File:** `docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md`  
**Commit:** `ddbe309e9e6aacc3016212e3a31e4efcbaae4786`  
**Purpose:** design the `Station → Location → Scope/Representativeness → Evidence` model before broadening acquisition or implementing the Water Score.

The handoff explicitly requires centralised work against `gineslm/climascope`, local validation with `python -m pytest`, preservation of existing AEMET/W2 data, and versioned documentation updates.

---

## 10. Immediate next step

The next engineering/design thread is responsible for designing and documenting the `Station`, `Location`, `Scope/Representativeness` and `Evidence` model, including provenance, relationships, progressive acquisition/research states and map-facing requirements.

Do this before broadening station acquisition, implementing interpolation, or defining the final Water Score.

---

## 11. Version history

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-08-15 | Initial water pipeline audit and W1/W2 documentation. |
| 0.2.0 | 2026-08-15 | Added W2 observed-total semantics, progressive acquisition strategy, spatial/evidence architecture and cross-thread documentation protocol. |
| 0.3.0 | 2026-08-15 | Added the versioned Station/Location/Evidence handoff and made the central documentation/versioning protocol explicit. |
