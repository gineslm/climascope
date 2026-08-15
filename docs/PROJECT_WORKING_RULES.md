# ClimaScope — Reglas de trabajo del proyecto

**Versión del documento:** 1.0.1  
**Creado:** 2026-08-15  
**Repositorio:** `gineslm/climascope`  
**URL del repositorio:** https://github.com/gineslm/climascope  
**Rama de trabajo actual:** `agent/water-pipeline-audit`  
**Raíz local conocida del proyecto:** `C:\Users\User\Downloads\climate_refuge_aemet_v0_4`

> **Idioma oficial del proyecto: español (España).** La documentación, decisiones, handoffs e informes deben redactarse en castellano salvo que exista una razón técnica para conservar un término original.

## 1. Propósito

Este documento es el contrato operativo permanente para el trabajo de ClimaScope entre conversaciones independientes. Existe para que el método del proyecto, la trazabilidad, la práctica documental y las reglas de transferencia no dependan de la memoria de una conversación concreta.

El repositorio Git es la fuente central de verdad. Un hilo nuevo debe recuperar el estado del proyecto desde el repositorio antes de tomar decisiones o realizar cambios.

## 2. Primer paso obligatorio en cada hilo nuevo

Antes de realizar trabajo del proyecto, el hilo debe:

1. leer este documento;
2. inspeccionar la rama actual y el estado de Git;
3. leer el/los informe(s) actual(es) del proyecto;
4. inspeccionar cualquier documento de handoff específico de la tarea;
5. identificar la versión vigente de la documentación y los commits relevantes;
6. inspeccionar la implementación y los tests existentes antes de proponer cambios;
7. informar de cualquier documento referenciado que falte en lugar de inventar su contenido.

El contexto previo de una conversación es útil, pero no constituye el registro autoritativo del proyecto.

## 3. Repositorio y acceso

Todo trabajo debe estar asociado al repositorio `gineslm/climascope`.

Capacidades requeridas para un hilo de implementación:

- leer archivos, ramas y documentación del repositorio;
- crear/actualizar archivos y hacer commits en la rama de trabajo acordada, o crear una rama específica cuando proceda;
- disponer de un checkout local cuando sea necesario ejecutar código o inspeccionar datos generados;
- utilizar el entorno Python del repositorio y ejecutar `python -m pytest` para validar los tests de Python.

No se debe asumir acceso a documentos que existan únicamente en otra conversación. Si no están en el repositorio, deben solicitarse o indicarse como no disponibles.

## 4. Disciplina de ramas y cambios

- No trabajar directamente sobre la rama por defecto salvo petición explícita.
- Preferir una rama específica de tarea como `agent/<tarea>`.
- Mantener los cambios no relacionados fuera del commit de la tarea.
- No sobrescribir ni regenerar datos fuente sin necesidad.
- Antes de hacer commit, inspeccionar `git status` y el diff/estadísticas.
- Una tarea completada debe dejar un estado Git reproducible.

## 5. La documentación es estado versionado del proyecto

Todo documento sustantivo del proyecto debe contener un identificador de versión.

Convención recomendada:

- major: cambio estructural/metodológico;
- minor: nueva capacidad documentada, decisión o sección sustancial;
- patch: aclaración, corrección o actualización editorial.

Los artefactos documentales deben estar comprometidos en GitHub.

El informe correspondiente debe referenciar los documentos importantes y registrar sus versiones actuales. Esto permite que hilos independientes recuperen el estado más reciente.

## 6. Informes y handoffs

El proyecto utiliza tres tipos documentales complementarios:

### Reglas maestras

`docs/PROJECT_WORKING_RULES.md`

Reglas operativas permanentes para todos los hilos.

### Informes de proyecto

Por ejemplo:

`docs/WATER_PIPELINE_AUDIT_REPORT.md`

Los informes registran lo que realmente se ha implementado, probado, medido, decidido y cambiado a lo largo del tiempo.

### Handoffs de hilo

Por ejemplo:

`docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md`

Los handoffs definen el alcance y el contexto de partida para un hilo especializado siguiente. Deben contener repositorio, rama, ruta local cuando se conozca, requisitos de acceso, objetivo, estado actual, restricciones, entregables, validación y protocolo de cierre.

## 7. Protocolo de cierre de cada hilo sustantivo

Antes de declarar completada una tarea:

1. ejecutar los tests relevantes;
2. inspeccionar los resultados generados cuando proceda;
3. actualizar el informe correspondiente;
4. incrementar la versión documental cuando haya cambios sustantivos de documentación;
5. crear/actualizar el siguiente handoff si se necesita otro hilo;
6. hacer commit con un mensaje intencionado;
7. hacer push de la rama acordada;
8. registrar el SHA del commit en el handoff/informe final;
9. indicar cualquier incertidumbre o evidencia que falte.

## 8. Reglas de trazabilidad y evidencia

ClimaScope debe conservar la distinción entre hechos de las fuentes, datos derivados del proyecto, valores modelados y evidencia cualitativa.

Todo dataset o indicador derivado debe poder rastrearse hasta:

- fuente/proveedor;
- dataset o documento de origen;
- periodo de adquisición/observación;
- transformación o cálculo;
- código/versión relevante;
- estado del control de calidad.

Nunca convertir silenciosamente datos missing en cero.

Nunca presentar un valor interpolado o modelado como una observación directa de una estación.

Nunca tratar la ausencia de investigación como evidencia de ausencia de riesgo.

## 9. Datos raw / processed / derived

El proyecto debería converger progresivamente hacia una separación clara como:

```text
data/
├── raw/          # material fuente; preservado y trazable
├── processed/    # representaciones limpiadas/normalizadas
├── derived/      # indicadores, scores, capas de mapa, modelos
└── reports/      # resultados generados o destinados a publicación
```

Las rutas existentes no deben moverse únicamente por razones de estilo. Una migración requiere una decisión deliberada y documentación.

El trabajo AEMET actual está en `data/raw/aemet/`, incluyendo JSON originales, evidencia de adquisición `.NO_DATA`, resultados de QC y CSV mensuales/anuales W2. Tratarlo como estado existente del proyecto salvo que se apruebe una migración documentada.

## 10. Principios Station, Location y Evidence

El modelo de dominio debe distinguir al menos:

```text
Station -> observaciones
Location -> lugar/sitio evaluado por el usuario
Scope/Representativeness -> relevancia espacial entre estaciones y ubicaciones
Evidence -> soporte cuantitativo, derivado o documental
```

Una observación de estación no es automáticamente el valor de cualquier ubicación cercana.

Si posteriormente se introduce interpolación, debe etiquetarse explícitamente como modelada/interpolada y conservar método, trazabilidad e incertidumbre.

Los datos cuantitativos de estaciones y la evidencia cualitativa/documental son tipos de evidencia diferentes, pero ambos pueden asociarse a una ubicación.

## 11. Adquisición e investigación progresivas

No intentar descargar o investigar todas las ubicaciones posibles antes de disponer de un mecanismo de priorización.

El flujo preferido es:

```text
candidata
  -> cribada
  -> datos cuantitativos adquiridos
  -> QC superado
  -> investigación documental priorizada
  -> evaluada
  -> promovida / despriorizada / rechazada
```

El proyecto debe priorizar primero las ubicaciones/estaciones prometedoras y ampliar progresivamente.

La investigación documental también debe ser proporcional al interés y relevancia de una candidata. Una ubicación que todavía no haya sido investigada debe permanecer explícitamente como `not_assessed` o equivalente, nunca como `low risk` o `no risk`.

## 12. Principios del mapa

El futuro mapa debe poder distinguir:

- estaciones físicas;
- ubicaciones evaluadas;
- cobertura/alcance de estaciones;
- observaciones directas;
- indicadores derivados;
- valores modelados/interpolados;
- calidad de los datos;
- evidencia documental;
- trazabilidad.

El alcance espacial es una representación de relevancia, no una prueba de que una estación mida condiciones idénticas en toda el área.

La interpolación se pospone hasta diseñar el modelo Station/Location/Scope y sus requisitos de incertidumbre.

## 13. Estado documentado actual del proyecto

En la versión 1.0.0 de estas reglas:

- el pipeline de agua se ha auditado alrededor de las estaciones AEMET `8416`, `3195` y `7012D`;
- se ha implementado y probado la agregación mensual y anual W2 de precipitación;
- la agregación actual conserva los totales observados de precipitación y expone días missing, cobertura y completitud;
- la suite de tests alcanzó 13 tests después de los últimos cambios de agregación;
- la siguiente tarea especializada prevista es el modelo de dominio Station / Location / Scope / Evidence.

Para el estado detallado actual, leer el último `docs/WATER_PIPELINE_AUDIT_REPORT.md` y el handoff específico de la tarea.

## 14. Inventario documental conocido

Los siguientes documentos del proyecto constan como presentes y relevantes en el contexto actual del repositorio:

| Documento | Función | Versión conocida |
|---|---|---:|
| `docs/PROJECT_WORKING_RULES.md` | Reglas operativas permanentes | 1.0.1 |
| `docs/CHATGPT_PROJECT_CONTEXT.md` | Contexto de integración con ChatGPT | 1.0.1 |
| `docs/WATER_PIPELINE_AUDIT_REPORT.md` | Informe/auditoría del pipeline de agua | 0.3.1 |
| `docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md` | Handoff del siguiente hilo | 0.1.1 |

Este inventario no afirma que sean los únicos documentos creados en otras conversaciones. Un documento forma parte del método del proyecto cuando está comprometido en el repositorio o se incorpora explícitamente al informe.

## 15. Cómo iniciar un hilo nuevo

Un hilo nuevo debe recibir una instrucción breve como:

> Trabaja en ClimaScope desde el repositorio central de GitHub. Primero lee `docs/CHATGPT_PROJECT_CONTEXT.md` y `docs/PROJECT_WORKING_RULES.md`, después el informe de proyecto más reciente y el handoff específico de la tarea. Trata GitHub como fuente de verdad, conserva la trazabilidad, no inventes documentos de proyecto que falten y sigue el protocolo de cierre. Informa de las versiones documentales actuales y de la rama antes de realizar cambios sustantivos.

El handoff específico define el objetivo real.

## 16. Cómo cerrar un hilo

El mensaje de cierre debe indicar:

- qué se ha implementado o decidido;
- tests/validación realizados;
- cambios de versión documental;
- archivos/datos afectados;
- rama y SHA del commit;
- cuestiones no resueltas;
- siguiente documento de handoff, si procede.

Esto mantiene los hilos futuros independientes del histórico del chat y conserva el rastro de decisiones del proyecto en Git.
