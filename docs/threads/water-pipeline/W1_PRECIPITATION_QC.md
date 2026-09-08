# ClimaScope — W1 · QC de precipitación AEMET

**Versión:** 1.0.0  
**Estado:** Activo  
**Idioma:** español (España)  
**THREAD responsable:** `thread-water-pipeline`

## 1. Alcance

Periodo objetivo: 2011-01-01 a 2025-12-31 (5.479 días naturales).

Estaciones benchmark: Valencia `8416`, Cartagena `7012D`, Madrid-Retiro `3195`.

## 2. Semántica de datos

La precipitación diaria de AEMET llega en el payload raw como `prec`. El campo normalizado es `prcp`.

- `0,0` explícito es un cero real y nunca se trata como missing.
- Las comas decimales se normalizan a valores numéricos.
- Los valores de precipitación missing dentro de un registro diario observado permanecen missing.
- Una fecha sin registro AEMET es una fecha missing y se distingue de un registro cuya precipitación sea missing.
- Los bloques `.NO_DATA` se conservan como procedencia de adquisición y no se convierten en ceros.

## 3. Resultado inicial de QC

| Estación | Primer dato | Último dato | Días observados | Fechas missing | Cobertura |
|---|---|---|---:|---:|---:|
| Valencia `8416` | 2011-01-01 | 2025-12-31 | 5.479 | 0 | 100.000% |
| Cartagena `7012D` | 2016-02-22 | 2025-12-31 | 3.572 | 1.907 | 65.194% |
| Madrid-Retiro `3195` | 2011-01-01 | 2025-12-31 | 5.478 | 1 | 99.982% |

La laguna de Cartagena está respaldada por diez bloques consecutivos `.NO_DATA` de AEMET que cubren desde 2011-01-01 hasta 2015-12-05. Por tanto, es una ausencia observada de disponibilidad de la fuente, no un valor de precipitación cero.

La única fecha missing de Madrid y los registros con precipitación missing deben identificarse por separado en el siguiente pase de QC.

## 4. Estado de decisión

- Valencia: apta para el periodo objetivo completo, sujeta al tratamiento explícito de precipitación missing.
- Madrid-Retiro: apta para el periodo completo con una fecha missing que debe documentarse.
- Cartagena: cobertura temporal parcial; no imputar la laguna anterior a 2016. La ventana benchmark final queda pendiente de revisión mensual/anual de cobertura.

No se calcula ningún Water Score ni interpolación a partir de este resultado de QC.

## 5. Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 2026-09-08 | Normalización al castellano y al formato documental vigente, sin cambiar resultados ni decisiones de QC. |
