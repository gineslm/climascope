# Climate Refuge / ClimaScope — Informe de auditoría del pipeline de agua

**Versión del informe:** 0.3.1  
**Rama:** `agent/water-pipeline-audit`  
**Alcance:** adquisición AEMET de clima y precipitación, QC, agregación W2, almacenamiento de datos, alcance del mapa, adquisición progresiva, futuras capas cualitativas y documentación entre hilos.  
**Estado:** W2 implementado y validado localmente con 13 tests superados tras el último cambio de agregación.  
**Última actualización:** 2026-08-15

> **Idioma del proyecto: español (España).** Este informe y la documentación asociada se mantienen en castellano.

---

## 1. Propósito y objetivo inicial

El objetivo inicial de este trabajo era auditar y operacionalizar el pipeline de datos de agua/clima alrededor de observaciones de estaciones AEMET, con suficiente trazabilidad e información de calidad para soportar posteriormente análisis a nivel de ubicación y una aplicación basada en mapa.

El trabajo se detuvo deliberadamente antes de definir un Water Score definitivo. Esta fase establece la base de datos y hace explícita la calidad de los datos antes de aplicar cualquier scoring o ranking.

## 2. Trabajo completado en esta fase

### 2.1 Registro de fuentes

Se reparó y validó el registro de fuentes de agua. Se diagnosticó y corrigió una entrada YAML mal formada y posteriormente el test del registro pasó correctamente.

### 2.2 Acceso y adquisición AEMET

Se verificó el acceso a la API de AEMET. Se validó una consulta directa de datos diarios para la estación `8416` (Valencia) usando el periodo `2025-01-01` a `2025-01-07`.

Los valores de precipitación AEMET con coma decimal se gestionan correctamente. La precipitación explícita `0,0` se trata como cero, mientras que la precipitación missing permanece como missing.

### 2.3 Estaciones auditadas

| Estación | Ubicación/función | Periodo disponible utilizado en la auditoría |
|---|---|---|
| `8416` | Valencia | 2011-01-01 → 2025-12-31 |
| `3195` | Madrid | 2011-01-01 → 2025-12-31 |
| `7012D` | Cartagena | 2016-02-22 → 2025-12-31 |

La capa de adquisición conserva los JSON originales y marcadores `.NO_DATA` explícitos para ventanas de consulta sin disponibilidad. Por tanto, las ventanas vacías/no disponibles son evidencia y no periodos secos silenciosos.

### 2.4 QC de precipitación raw

El QC a nivel de estación distingue días objetivo, días observados, días missing, cobertura, días con precipitación explícitamente cero, días con precipitación positiva, días con precipitación missing y primera/última fecha observada.

Resultados iniciales de auditoría:

| Estación | Días objetivo | Días observados | Días missing | Cobertura |
|---|---:|---:|---:|---:|
| `8416` | 5479 | 5479 | 0 | 100.000% |
| `7012D` | 5479 | 3572 | 1907 | 65.194% |
| `3195` | 5479 | 5478 | 1 | 99.982% |

Para `7012D`, la ventana efectiva de observación comienza el `2016-02-22`; dentro de esa ventana real hay 29 días missing sobre 3601 días esperados (99.195% de cobertura).

La cobertura de fechas se separa de la calidad de `prec`: una estación puede tener un registro de fecha mientras la precipitación de ese registro sea missing.

### 2.5 Agregación W2

Está implementada la agregación mensual y anual de precipitación. Las salidas actuales son:

```text
data/raw/aemet/3195_precip_monthly.csv
data/raw/aemet/3195_precip_annual.csv
data/raw/aemet/7012D_precip_monthly.csv
data/raw/aemet/7012D_precip_annual.csv
data/raw/aemet/8416_precip_monthly.csv
data/raw/aemet/8416_precip_annual.csv
```

La primera semántica de agregación descartaba el total completo de un periodo cuando faltaba un día esperado. Esto se corrigió.

Semántica actual:

- `prcp_observed_total_mm` = suma de los valores de precipitación realmente observados;
- `expected_days` = días naturales esperados en el periodo;
- `observed_prcp_days` = días con precipitación utilizable;
- `missing_prcp_days` = días esperados sin precipitación utilizable;
- `coverage_pct` = observados/esperados;
- `complete` = verdadero únicamente cuando todos los días esperados tienen precipitación utilizable.

Un valor missing nunca se convierte en cero, pero tampoco borra la precipitación que sí se ha observado.

### 2.6 Tests

La última ejecución local de tests informa:

```text
13 passed
```

La cobertura incluye carga del registro de fuentes, parsing de precipitación, coma decimal, cero explícito, precipitación missing, QC de precipitación, agregación mensual/anual, periodos incompletos y conservación de totales observados.

---

## 3. Cambios respecto al objetivo inicial

La arquitectura ya no trata las observaciones raw de una estación como datos automáticamente aptos para scoring.

La progresión actual es:

```text
fuente AEMET
    ↓
observaciones raw de estación
    ↓
QC de adquisición/fechas
    ↓
QC de valores de precipitación
    ↓
agregación mensual / anual
    ↓
entradas analíticas con cobertura explícita
    ↓
Water Score futuro
```

El Water Score todavía no está definido intencionadamente.

El alcance también ha pasado de un pipeline centrado en estaciones a una arquitectura centrada en ubicaciones en la que estaciones, ubicaciones, representatividad espacial, indicadores cuantitativos y evidencia documental permanecen diferenciados.

---

## 4. Dirección Station, Location e interpolación

Una estación es un punto físico de observación. Una ubicación es el lugar/sitio que el usuario evalúa. Una observación de estación no debe convertirse automáticamente en el valor de cualquier ubicación cercana.

Inicialmente, el mapa debería mostrar puntos de estación, periodos de observación, cobertura y calidad. Una capa separada de representatividad/alcance puede indicar qué ubicaciones se consideran relevantes para una estación.

La interpolación queda **aplazada**. Si se introduce posteriormente, debe ser un producto derivado separado con método, trazabilidad e incertidumbre. La aplicación debe distinguir:

```text
observado en estación
relevante para ubicación
modelado/interpolado para ubicación
```

Un futuro modelo de influencia puede utilizar un radio, áreas tipo Thiessen/Voronoi o ponderación por distancia, pero la representatividad climática también puede depender de altitud, terreno, posición litoral/interior, efectos urbanos y régimen climático.

Recomendación: mantener las observaciones raw de estación como autoridad y convertir la interpolación en una capa derivada opcional únicamente después de validar sus supuestos.

---

## 5. Estrategia de adquisición progresiva

No se considera preferible descargar todo el histórico de todas las estaciones. La adquisición debe ser progresiva:

```text
catálogo de estaciones
    -> ranking de candidatas
    -> estaciones prioritarias
    -> adquisición histórica acotada
    -> QC
    -> cualificación analítica
    -> promoción
```

La prioridad debería considerar cobertura histórica, completitud, variables disponibles, relevancia geográfica y estabilidad de la fuente. Deben conservarse el comportamiento de reutilización existente y la evidencia `.NO_DATA`.

Una estación debe pasar por estados explícitos de adquisición/calidad en lugar de considerarse analíticamente válida simplemente porque sus datos se hayan descargado.

---

## 6. Almacenamiento de datos

Los datos raw y derivados actuales de AEMET están en:

```text
data/raw/aemet/
```

Incluye JSON originales, evidencia `.NO_DATA`, resultados de QC y productos W2 CSV.

Los productos CSV W2 son tablas analíticas derivadas y no sustituyen las observaciones raw.

Una separación futura podría evolucionar hacia:

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

La migración debe ser deliberada y no debe alterar innecesariamente el rastro actual de auditoría.

---

## 7. Evidencia cuantitativa frente a documental

No todas las futuras capas de información necesitan una estación física o una serie temporal numérica. La aplicación debe soportar tanto evidencia cuantitativa como documental.

Conceptualmente:

```text
Location
│
├── Observaciones cuantitativas
│   ├── clima
│   ├── precipitación
│   ├── agua
│   └── otras variables medidas
│
├── Indicadores cuantitativos derivados
│   ├── agregados con cobertura
│   ├── tendencias
│   └── scores
│
└── Evidencia documental
    ├── informes oficiales
    ├── documentos de planificación
    ├── evidencia ambiental
    └── evaluaciones cualitativas
```

La evidencia documental debe conservar título de la fuente, organización emisora, fecha de publicación, URL/referencia al archivo, alcance geográfico, tipo de evidencia, relevancia, fecha de extracción y confianza/calidad.

La investigación documental debe ser progresiva y no exhaustiva. El cribado cuantitativo amplio debe identificar candidatas prometedoras antes de realizar una investigación cualitativa más profunda. `not_assessed` nunca debe significar `no_risk`.

Los estados documentales sugeridos son `not_assessed`, `in_research`, `assessed` e `insufficient_evidence`.

---

## 8. Dirección de la arquitectura del mapa

El futuro mapa debería exponer dos capas conectadas:

### Capa de estaciones

El detalle de una estación puede incluir:

```text
station_id
coordenadas
periodo disponible
cobertura
resumen de precipitación
resumen climático
estado QC
```

### Capa de ubicaciones

El detalle de una ubicación debería poder exponer:

```text
ubicación candidata
↓
estaciones relevantes
↓
evidencia de estaciones
↓
indicadores climáticos/de agua derivados
↓
otras capas de evidencia
↓
análisis final de idoneidad
```

Por tanto, el mapa es una capa de visualización y navegación sobre la evidencia, no un sustituto de la evidencia.

---

## 9. Protocolo documental y entre hilos

El repositorio es la fuente central de verdad del proyecto. Los artefactos documentales deben versionarse en GitHub y referenciarse desde el informe correspondiente para que diferentes hilos puedan recuperar el estado más reciente.

Todo documento de handoff para un hilo nuevo debe contener:

- ubicación del proyecto y repositorio;
- rama de trabajo;
- requisitos de acceso;
- versión actual del informe/documentación;
- objetivo y alcance;
- decisiones y restricciones establecidas;
- entregables;
- validaciones/tests requeridos;
- archivos/datos que no deberían regenerarse innecesariamente;
- protocolo de cierre;
- requisitos del siguiente handoff cuando proceda.

### Documentos de contexto y reglas

**`docs/CHATGPT_PROJECT_CONTEXT.md` — versión 1.0.1**  
Puente entre el Proyecto de ChatGPT y el repositorio; define el arranque de conversaciones nuevas y la reincorporación de conversaciones existentes.

**`docs/PROJECT_WORKING_RULES.md` — versión 1.0.1**  
Reglas operativas permanentes del proyecto e idioma oficial: español (España).

### Handoff actual

**Versión:** 0.1.1  
**Archivo:** `docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md`  
**Propósito:** diseñar el modelo `Station → Location → Scope/Representativeness → Evidence` antes de ampliar la adquisición o implementar el Water Score.

El handoff exige explícitamente trabajo centralizado contra `gineslm/climascope`, validación local con `python -m pytest`, conservación de los datos AEMET/W2 existentes y actualización de documentación versionada.

---

## 10. Siguiente paso inmediato

El siguiente hilo de ingeniería/diseño es responsable de diseñar y documentar el modelo `Station`, `Location`, `Scope/Representativeness` y `Evidence`, incluyendo trazabilidad, relaciones, estados de adquisición/investigación progresivos y requisitos orientados al mapa.

Esto debe hacerse antes de ampliar la adquisición de estaciones, implementar interpolación o definir el Water Score definitivo.

---

## 11. Historial de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 0.1.0 | 2026-08-15 | Auditoría inicial del pipeline de agua y documentación W1/W2. |
| 0.2.0 | 2026-08-15 | Añadida la semántica de totales observados W2, estrategia de adquisición progresiva, arquitectura espacial/evidencial y protocolo documental entre hilos. |
| 0.3.0 | 2026-08-15 | Añadido el handoff versionado Station/Location/Evidence y explicitado el protocolo central de documentación/versionado. |
| 0.3.1 | 2026-08-15 | Traducción y normalización de la documentación del proyecto al castellano (España); incorporado el contexto ChatGPT y las reglas maestras al inventario documental. |
