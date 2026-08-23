# W1 — AEMET precipitation QC

## Scope

Target period: 2011-01-01 to 2025-12-31 (5,479 calendar days).

Benchmark stations: Valencia `8416`, Cartagena `7012D`, Madrid-Retiro `3195`.

## Data semantics

AEMET daily precipitation is supplied in the raw payload as `prec`. The normalized field is `prcp`.

- Explicit `0,0` is a real zero and is never treated as missing.
- Decimal commas are normalized to numeric decimals.
- Missing precipitation values within an observed daily record remain missing.
- A date with no AEMET record is a missing date and is distinct from a record whose precipitation is missing.
- AEMET `.NO_DATA` blocks are retained as acquisition provenance and are not converted to zeros.

## Initial QC result

| Station | First data | Last data | Observed days | Missing dates | Coverage |
|---|---|---|---:|---:|---:|
| Valencia `8416` | 2011-01-01 | 2025-12-31 | 5,479 | 0 | 100.000% |
| Cartagena `7012D` | 2016-02-22 | 2025-12-31 | 3,572 | 1,907 | 65.194% |
| Madrid-Retiro `3195` | 2011-01-01 | 2025-12-31 | 5,478 | 1 | 99.982% |

The Cartagena gap is supported by ten consecutive AEMET `.NO_DATA` blocks covering 2011-01-01 through 2015-12-05. It is therefore an observed source-availability gap, not a precipitation value of zero.

The single Madrid missing date and the precipitation-missing records must be identified separately in the next QC pass.

## Decision status

- Valencia: suitable for the full target period, subject to precipitation-missing handling.
- Madrid-Retiro: suitable for the full target period with one missing date to document.
- Cartagena: partial temporal coverage; do not impute the pre-2016 gap. Final benchmark window remains pending annual/monthly coverage review.

No Water Score or interpolation is calculated from this QC result.
