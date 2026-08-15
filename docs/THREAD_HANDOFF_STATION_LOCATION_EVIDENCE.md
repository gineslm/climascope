# Handoff — hilo receptor: Station / Location / Scope / Evidence

**Versión:** 0.1.0  
**Estado:** READY_FOR_HANDOFF  
**Receptor único:** `thread-station-location-evidence`  
**Emisor:** `thread-architecture`  
**Ciclo de origen:** 1  
**Proyecto:** ClimaScope  
**Repositorio:** `gineslm/climascope`  
**Rama de origen:** `agent/thread-architecture`

## 1. Propósito de la transferencia

Transferir al hilo `thread-station-location-evidence` la responsabilidad de diseñar el modelo de dominio que relaciona estaciones, ubicaciones, alcance/representatividad espacial y evidencia, manteniendo separadas las observaciones directas de los valores relevantes o modelados para una ubicación.

Este documento es una transferencia de responsabilidad. No sustituye a `docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md`, que contiene el contexto y requisitos detallados del trabajo especializado.

## 2. Estado de partida

El pipeline de agua W2 ha sido auditado y dispone de salidas mensuales/anuales para estaciones AEMET de referencia. La siguiente tarea especializada prevista en el proyecto es precisamente el diseño Station / Location / Scope / Evidence.

El modelo general de trabajo ya establece que una observación de estación no es automáticamente el valor de una ubicación cercana y que la representatividad espacial debe quedar explícita.

## 3. Documentos autoritativos del receptor

El receptor debe leer, como mínimo y en este orden funcional:

1. `docs/PROJECT_WORKING_RULES.md` — versión vigente.
2. `docs/CHATGPT_PROJECT_CONTEXT.md` — versión vigente.
3. `docs/THREAD_ARCHITECTURE.md` — versión vigente.
4. `docs/WATER_PIPELINE_AUDIT_REPORT.md` — estado científico/técnico W2.
5. `docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md` — requisitos específicos de la tarea.
6. Este handoff — transferencia de responsabilidad y estado del ciclo anterior.

## 4. Responsabilidad transferida

### Dentro de alcance

- modelo canónico `Station`;
- modelo `Location`;
- `Scope / Representativeness`;
- abstracción `Evidence`;
- cardinalidades y relaciones;
- procedencia y trazabilidad;
- estados de adquisición/investigación progresivas;
- requisitos mínimos para mapa;
- prerrequisitos y aplazamiento explícito de interpolación;
- plan de implementación/migración compatible con los datos AEMET/W2 existentes.

### Fuera de alcance

- Water Score definitivo;
- implementación de interpolación;
- rediseño del pipeline W2 ya validado;
- ampliación masiva de adquisición AEMET;
- UI final del mapa;
- arquitectura general de hilos, salvo necesidades de integración que deban reportarse al hilo emisor.

## 5. Decisiones que no deben reabrirse sin evidencia nueva

1. La observación de estación no equivale automáticamente al valor de una ubicación.
2. La representatividad espacial debe ser explícita.
3. La interpolación queda aplazada.
4. Los valores observados, derivados y modelados deben distinguirse.
5. La adquisición e investigación deben ser progresivas.
6. La ausencia de investigación no equivale a ausencia de riesgo.
7. Los datos raw AEMET existentes deben preservarse.

Estas decisiones pueden revisarse únicamente si el receptor encuentra evidencia o una incompatibilidad técnica que justifique elevar la cuestión como conflicto/propuesta.

## 6. Entregables

El receptor debe producir:

1. modelo de dominio documentado;
2. estructuras/esquemas propuestos;
3. cardinalidades y reglas de relación;
4. reglas de trazabilidad;
5. máquina de estados de adquisición/investigación;
6. requisitos de mapa;
7. decisión documentada sobre interpolación y prerrequisitos;
8. plan de migración/implementación;
9. tests/reglas de validación cuando corresponda;
10. documentación versionada y handoff siguiente si procede.

## 7. Criterio de aceptación del handoff

El handoff se considera correctamente recibido cuando el nuevo hilo:

- identifica `thread-station-location-evidence` como su `thread_id`;
- confirma su responsabilidad y límites;
- inspecciona el repositorio antes de trabajar;
- confirma las versiones actuales de los documentos autoritativos;
- no depende del historial de esta conversación para reconstruir el objetivo;
- puede iniciar el diseño exclusivamente con el repositorio y este handoff.

## 8. Estado del emisor

El hilo `thread-architecture`, ciclo 1, ha completado la consolidación inicial de la arquitectura documental y deja preparada esta transferencia. No asume la responsabilidad técnica del modelo Station / Location / Scope / Evidence.

**SHA de referencia de la rama emisora:** `593fced2967dd89b53b312c1c53534e2b1875ab4`

## 9. Protocolo de retorno

Al terminar, el receptor debe actualizar su documentación y entregar un handoff al siguiente responsable o devolver explícitamente el resultado al hilo de arquitectura si se detectan necesidades de cambio en el modelo general de hilos.
