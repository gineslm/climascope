# New-thread handoff: Station / Location / Evidence model

**Document version:** 0.1.0  
**Created:** 2026-08-15  
**Project:** ClimaScope  
**Repository:** `gineslm/climascope`  
**Repository URL:** `https://github.com/gineslm/climascope`  
**Working branch:** `agent/water-pipeline-audit`  
**Project root (local):** `C:\Users\User\Downloads\climate_refuge_aemet_v0_4`

## Access requirements

The next thread must work against the central GitHub repository, not an isolated copy.

Required:

- access to repository `gineslm/climascope`;
- ability to read the current branch and its documentation/data;
- ability to create/update files and commit changes on the working branch, or create a dedicated feature branch if agreed first;
- local checkout for running tests and inspecting generated data when required;
- Python environment capable of running the repository test suite with `python -m pytest`.

Do not invent missing project documents. If a referenced document is not present in the repository/current project context, report it and request it from the project owner.

## Source of truth

The repository is the central source of truth. Documentation must be versioned in GitHub and referenced from the relevant report so separate conversation threads can recover the latest project state.

Current audit report: `docs/WATER_PIPELINE_AUDIT_REPORT.md`.

## Objective

Design, document and test the domain model linking:

```text
Station -> Location -> Evidence
```

The model must support the future map application, progressive data acquisition, spatial scope/representativeness, quantitative observations, derived indicators, and qualitative/documentary evidence.

This is a **design task first**. Do not prematurely implement interpolation or the final Water Score.

## Context already established

The current water pipeline has been audited around AEMET stations `8416` (Valencia), `3195` (Madrid), and `7012D` (Cartagena). W2 monthly and annual precipitation outputs are under `data/raw/aemet/`, alongside raw AEMET JSON and `.NO_DATA` acquisition evidence.

The current W2 semantics distinguish observed precipitation, explicit zero precipitation, missing precipitation, expected days, observed days, missing days, coverage and complete periods. The latest aggregation preserves the observed precipitation total even when a period is incomplete and exposes coverage/completeness for downstream eligibility rules.

### Decisions already agreed

1. A station observation must not automatically be treated as the value for every nearby location.
2. The map should show physical stations and an explicit spatial scope/representativeness layer.
3. Interpolation is **not** part of the current implementation. If introduced later, it must be distinguishable from direct observations and carry method, provenance and uncertainty.
4. Acquisition should be progressive: prioritise promising stations/locations rather than downloading all available history at once.
5. Quantitative station data and qualitative/documentary evidence must be modelled as different evidence types that can both attach to a location.
6. Documentary research should also be progressive; lack of research must never mean absence of risk.

## Questions the new thread must resolve

### 1. Station model

Define the minimum canonical station record:

- stable station identifier;
- provider/source;
- name;
- coordinates;
- elevation where available;
- administrative/geographic metadata;
- active/inactive status where available;
- data availability window;
- variables available;
- source/provenance;
- acquisition status and last successful acquisition.

Decide which fields are source facts and which are project-derived metadata.

### 2. Location model

Define what the application means by a `Location`. A location is not necessarily a station; it represents the user-facing place/site evaluated on the map.

Determine:

- stable location ID;
- coordinates/geometry;
- name/label;
- location type;
- administrative hierarchy;
- candidate status;
- relationship to one or more stations;
- relationship to quantitative indicators;
- relationship to documentary evidence.

### 3. Scope / representativeness

Design how the spatial relevance of a station to a location is represented. Consider, without committing prematurely:

- explicit radius;
- station-specific scope;
- terrain/climate regime;
- distance weighting;
- Voronoi/service areas;
- multiple-station coverage;
- uncertainty.

The model must distinguish:

```text
observed at station
relevant to location
modelled/interpolated for location
```

### 4. Evidence model

Design a common evidence abstraction capable of representing:

- quantitative time-series observations;
- derived quantitative indicators;
- official reports;
- planning documents;
- environmental studies;
- local/qualitative assessments;
- source URLs/documents;
- publication date;
- evidence date/period;
- provenance;
- confidence/quality;
- assessment status.

Define how multiple evidence items attach to a location and how conflicts or different time periods are represented.

### 5. Progressive research/acquisition

Design states for a pipeline such as:

```text
candidate -> screened -> quantitative data acquired -> QC passed
-> documentary research prioritised -> assessed -> promoted
```

The model must also represent insufficient evidence and rejected/deprioritised candidates.

### 6. Map requirements

Define the minimum data needed for a map that can:

- display locations;
- display stations;
- show station scope/representativeness;
- show data availability/quality;
- open a location detail view;
- show quantitative indicators;
- show documentary evidence;
- distinguish observed vs derived/modelled values;
- expose provenance.

## Required deliverables

1. documented domain model;
2. proposed schema/data structures for `Station`, `Location`, `Scope/Representativeness`, and `Evidence`;
3. relationship/cardinality rules;
4. provenance rules;
5. status/state machine for progressive acquisition and research;
6. map-facing requirements;
7. explicit decision on whether interpolation is deferred and prerequisites for it;
8. migration/implementation plan that does not unnecessarily disturb existing AEMET raw/W2 data;
9. tests or validation rules where implementation is introduced;
10. updated documentation report with a new version number.

## Constraints

- Preserve current AEMET raw data and W2 outputs unless a deliberate migration is approved.
- Do not silently reinterpret missing data as zero.
- Do not present interpolation/modelled values as station observations.
- Preserve provenance and source identity.
- Avoid broad data acquisition until the prioritisation model is defined.
- Do not calculate the final Water Score as part of this task unless the design explicitly requires a placeholder interface.

## Completion protocol

At the end of the thread:

1. run the repository tests;
2. document the resulting design and decisions;
3. update the relevant report with a new version tag;
4. commit the documentation/code changes to GitHub;
5. record the commit SHA in the final handoff;
6. create the next handoff document if another specialised thread is required.

## Starting instruction for the new thread

> Work from this handoff and the current repository state. First inspect the existing documentation and AEMET/W2 implementation. Then design the Station / Location / Scope / Evidence model before writing production code. Keep the repository as the central source of truth and version every resulting documentation artifact.
