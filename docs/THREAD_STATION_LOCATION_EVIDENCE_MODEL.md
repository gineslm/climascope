# Handoff de nuevo hilo: modelo Station / Location / Evidence

**Versión del documento:** 0.1.1  
**Creado:** 2026-08-15  
**Proyecto:** ClimaScope  
**Repositorio:** `gineslm/climascope`  
**URL del repositorio:** `https://github.com/gineslm/climascope`  
**Rama de trabajo:** `agent/water-pipeline-audit`  
**Raíz local del proyecto:** `C:\Users\User\Downloads\climate_refuge_aemet_v0_4`

> **Idioma del proyecto: español (España).** El trabajo y la documentación de este hilo deben realizarse en castellano.

## Requisitos de acceso

El siguiente hilo debe trabajar contra el repositorio central de GitHub, no contra una copia aislada.

Requisitos:

- acceso al repositorio `gineslm/climascope`;
- capacidad para leer la rama actual y su documentación/datos;
- capacidad para crear/actualizar archivos y hacer commits en la rama de trabajo, o crear una rama específica si se acuerda previamente;
- checkout local para ejecutar tests e inspeccionar datos generados cuando sea necesario;
- entorno Python capaz de ejecutar la suite con `python -m pytest`.

No inventar documentos de proyecto que falten. Si un documento referenciado no está presente en el repositorio/contexto actual, comunicarlo y solicitarlo al propietario del proyecto.

## Fuente de verdad

El repositorio es la fuente central de verdad. La documentación debe versionarse en GitHub y referenciarse desde el informe correspondiente para que hilos independientes puedan recuperar el estado más reciente del proyecto.

Informe de auditoría actual: `docs/WATER_PIPELINE_AUDIT_REPORT.md`.

## Objetivo

Diseñar, documentar y probar el modelo de dominio que relaciona:

```text
Station -> Location -> Evidence
```

El modelo debe soportar la futura aplicación de mapa, la adquisición progresiva de datos, el alcance/representatividad espacial, las observaciones cuantitativas, los indicadores derivados y la evidencia cualitativa/documental.

Esta es **primero una tarea de diseño**. No implementar prematuramente la interpolación ni el Water Score definitivo.

## Contexto ya establecido

El pipeline actual de agua se ha auditado alrededor de las estaciones AEMET `8416` (Valencia), `3195` (Madrid) y `7012D` (Cartagena). Las salidas W2 mensuales y anuales están en `data/raw/aemet/`, junto con JSON AEMET originales y evidencia de adquisición `.NO_DATA`.

La semántica actual de W2 distingue precipitación observada, cero explícito, precipitación missing, días esperados, días observados, días missing, cobertura y periodos completos. La última agregación conserva el total observado de precipitación aunque el periodo sea incompleto y expone cobertura/completitud para las reglas de elegibilidad posteriores.

### Decisiones ya acordadas

1. Una observación de estación no debe tratarse automáticamente como el valor de toda ubicación cercana.
2. El mapa debe mostrar estaciones físicas y una capa espacial explícita de alcance/representatividad.
3. La interpolación **no** forma parte de la implementación actual. Si se introduce posteriormente, debe distinguirse de las observaciones directas y llevar método, trazabilidad e incertidumbre.
4. La adquisición debe ser progresiva: priorizar estaciones/ubicaciones prometedoras en lugar de descargar todo el histórico disponible de una vez.
5. Los datos cuantitativos de estaciones y la evidencia cualitativa/documental deben modelarse como tipos de evidencia diferentes que puedan asociarse ambos a una ubicación.
6. La investigación documental también debe ser progresiva; la falta de investigación nunca debe significar ausencia de riesgo.

## Preguntas que debe resolver el nuevo hilo

### 1. Modelo Station

Definir el registro canónico mínimo de una estación:

- identificador estable de estación;
- proveedor/fuente;
- nombre;
- coordenadas;
- altitud cuando esté disponible;
- metadatos administrativos/geográficos;
- estado activa/inactiva cuando esté disponible;
- ventana de disponibilidad de datos;
- variables disponibles;
- fuente/trazabilidad;
- estado de adquisición y última adquisición correcta.

Decidir qué campos son hechos de la fuente y cuáles son metadatos derivados del proyecto.

### 2. Modelo Location

Definir qué significa `Location` en la aplicación. Una ubicación no es necesariamente una estación; representa el lugar/sitio evaluado por el usuario en el mapa.

Determinar:

- ID estable de ubicación;
- coordenadas/geometría;
- nombre/etiqueta;
- tipo de ubicación;
- jerarquía administrativa;
- estado de candidata;
- relación con una o varias estaciones;
- relación con indicadores cuantitativos;
- relación con evidencia documental.

### 3. Scope / Representativeness

Diseñar cómo se representa la relevancia espacial de una estación para una ubicación. Considerar, sin comprometerse prematuramente:

- radio explícito;
- alcance específico de cada estación;
- régimen de terreno/clima;
- ponderación por distancia;
- polígonos de Voronoi/Thiessen o áreas de servicio;
- cobertura de varias estaciones;
- incertidumbre.

El modelo debe distinguir:

```text
observado en estación
relevante para ubicación
modelado/interpolado para ubicación
```

### 4. Modelo Evidence

Diseñar una abstracción de evidencia común capaz de representar:

- observaciones cuantitativas de series temporales;
- indicadores cuantitativos derivados;
- informes oficiales;
- documentos de planificación;
- estudios ambientales;
- evaluaciones locales/cualitativas;
- URLs/documentos fuente;
- fecha de publicación;
- fecha/periodo de la evidencia;
- trazabilidad;
- confianza/calidad;
- estado de evaluación.

Definir cómo se asocian múltiples evidencias a una ubicación y cómo se representan conflictos o periodos temporales diferentes.

### 5. Investigación/adquisición progresivas

Diseñar estados para un pipeline como:

```text
candidata -> cribada -> datos cuantitativos adquiridos -> QC superado
-> investigación documental priorizada -> evaluada -> promovida
```

El modelo debe representar también evidencia insuficiente y candidatas rechazadas/despriorizadas.

### 6. Requisitos del mapa

Definir los datos mínimos necesarios para un mapa que pueda:

- mostrar ubicaciones;
- mostrar estaciones;
- mostrar alcance/representatividad de las estaciones;
- mostrar disponibilidad/calidad de datos;
- abrir el detalle de una ubicación;
- mostrar indicadores cuantitativos;
- mostrar evidencia documental;
- distinguir valores observados de derivados/modelados;
- exponer la trazabilidad.

## Entregables requeridos

1. modelo de dominio documentado;
2. esquema/estructuras de datos propuestas para `Station`, `Location`, `Scope/Representativeness` y `Evidence`;
3. reglas de relación/cardinalidad;
4. reglas de trazabilidad;
5. máquina de estados para adquisición e investigación progresivas;
6. requisitos orientados al mapa;
7. decisión explícita sobre el aplazamiento de la interpolación y sus prerrequisitos;
8. plan de migración/implementación que no altere innecesariamente los datos AEMET raw/W2 existentes;
9. tests o reglas de validación cuando se introduzca implementación;
10. informe de documentación actualizado con un nuevo número de versión.

## Restricciones

- Preservar los datos AEMET raw actuales y las salidas W2 salvo que se apruebe una migración deliberada.
- No reinterpretar silenciosamente datos missing como cero.
- No presentar valores interpolados/modelados como observaciones de estación.
- Preservar trazabilidad e identidad de la fuente.
- Evitar ampliar la adquisición de datos hasta definir el modelo de priorización.
- No calcular el Water Score definitivo como parte de esta tarea salvo que el diseño requiera explícitamente una interfaz provisional.

## Protocolo de cierre

Al terminar el hilo:

1. ejecutar los tests del repositorio;
2. documentar el diseño y las decisiones resultantes;
3. actualizar el informe correspondiente con una nueva etiqueta de versión;
4. hacer commit de los cambios documentales/de código en GitHub;
5. registrar el SHA del commit en el handoff final;
6. crear el siguiente handoff si se necesita otro hilo especializado.

## Instrucción de inicio del nuevo hilo

> Trabaja desde este handoff y el estado actual del repositorio. Primero inspecciona la documentación existente y la implementación AEMET/W2. Después diseña el modelo Station / Location / Scope / Evidence antes de escribir código de producción. Mantén el repositorio como fuente central de verdad y versiona cada nuevo artefacto documental.
