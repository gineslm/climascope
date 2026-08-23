# ClimaScope — Manifest del hilo Station / Location / Scope / Evidence

**Versión:** 0.1.0  
**Estado:** ACTIVE  
**Estado del THREAD:** ACTIVE  
**Ciclo:** 1  
**Idioma:** español (España)  
**Repositorio:** `gineslm/climascope`  
**Rama raíz de conocimiento:** `knowledge`  
**Rama de trabajo asociada:** `agent/water-pipeline-audit`

## 1. Identidad

```yaml
thread_id: thread-station-location-evidence
domain: modelo de dominio Station / Location / Scope / Evidence
status: ACTIVE
owner: línea de dominio científico del proyecto
created: 2026-08-23
current_cycle: 1
origin:
  type: USER_DECLARED
  source_id: conversation
repository:
  knowledge_branch: knowledge
  created_from_knowledge_commit: 84d8845ce2475e7d0c860bdc27b5afe4816675b8
  work_branch: agent/water-pipeline-audit   # rama asociada (pipeline W2); el ciclo actual es de diseño documental
```

`created_from_knowledge_commit` es el commit de `knowledge` desde el que se da de alta este THREAD mediante la creación de su MANIFEST; es histórico e inmutable. El estado vigente de `knowledge` se resuelve siempre leyendo la rama.

## 2. Responsabilidad

Diseñar y documentar el modelo de dominio que relaciona estaciones, ubicaciones, alcance/representatividad espacial y evidencia:

```text
Station -> Location -> Scope/Representativeness -> Evidence
```

manteniendo separadas las observaciones directas de estación de los valores relevantes o modelados para una ubicación. Es primero una tarea de diseño; no se implementa interpolación ni Water Score definitivo de forma prematura.

## 3. Dentro de alcance

- modelo canónico `Station`;
- modelo `Location`;
- `Scope / Representativeness`;
- abstracción `Evidence`;
- cardinalidades y relaciones;
- procedencia y trazabilidad;
- estados de adquisición/investigación progresivos;
- requisitos mínimos para el mapa;
- prerrequisitos y aplazamiento explícito de la interpolación;
- plan de implementación/migración compatible con los datos AEMET/W2 existentes.

## 4. Fuera de alcance

- Water Score definitivo;
- implementación de interpolación;
- rediseño del pipeline W2 ya validado;
- ampliación masiva de adquisición AEMET;
- UI final del mapa;
- arquitectura general de hilos (salvo necesidades de integración, que se reportan a la línea correspondiente);
- reinterpretación silenciosa de datos existentes.

## 5. Documentos autoritativos

- `docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md` — requisitos y contexto detallado del modelo de dominio (v0.1.4).

## 6. Dependencias

- `docs/WATER_PIPELINE_AUDIT_REPORT.md` — estado científico/técnico del pipeline W2.
- `docs/THREAD_ARCHITECTURE.md` — arquitectura de hilos.
- `docs/PROJECT_WORKING_RULES.md` — reglas permanentes.
- `docs/PROJECT_AGENT_CONTEXT.md` — integración agente ↔ repositorio.

## 7. Decisiones consolidadas (no reabrir sin evidencia nueva)

1. Una observación de estación no equivale automáticamente al valor de una ubicación cercana.
2. La representatividad espacial debe ser explícita.
3. Deben distinguirse semánticamente: observado en estación, relevante para ubicación y modelado/interpolado.
4. La interpolación queda aplazada; si se introduce, conservará método, trazabilidad e incertidumbre.
5. La adquisición y la investigación son progresivas.
6. `not_assessed` nunca significa ausencia de riesgo.
7. Datos cuantitativos de estación y evidencia cualitativa/documental son tipos de evidencia distintos asociables a una ubicación.
8. Deben preservarse AEMET raw / W2 y su trazabilidad salvo migración deliberada.

Estas decisiones pueden revisarse solo si aparece evidencia o incompatibilidad técnica que justifique elevarlo como conflicto/propuesta.

## 8. Entregables

1. modelo de dominio documentado;
2. estructuras/esquemas propuestos para `Station`, `Location`, `Scope/Representativeness` y `Evidence`;
3. cardinalidades y reglas de relación;
4. reglas de trazabilidad;
5. máquina de estados de adquisición/investigación;
6. requisitos orientados al mapa;
7. decisión documentada sobre interpolación y prerrequisitos;
8. plan de migración/implementación compatible con AEMET/W2;
9. tests/validación cuando exista implementación;
10. actualización versionada del informe correspondiente y handoff siguiente si procede.

## 9. HANDOFF actual e histórico

```yaml
current_handoff: none
handoff_history: []
```

Nota: este THREAD se da de alta directamente por consolidación de coherencia estructural (Lote 2A). El HANDOFF de creación previo (`THREAD_HANDOFF_STATION_LOCATION_EVIDENCE`) se retiró en ese proceso; el contexto que transfería queda incorporado en este MANIFEST y en `THREAD_STATION_LOCATION_EVIDENCE_MODEL.md`.

## 10. Validación

Las propuestas deben comprobarse frente a: reglas permanentes; modelo de dominio vigente; trazabilidad; distinción observado/derivado/modelado; estados explícitos de evaluación (incluido `not_assessed`); y el principio de que el mapa es capa de navegación sobre la evidencia, no sustituto de ella.

## 11. Cuestiones abiertas

- Confirmar si el ciclo produce implementación en `agent/water-pipeline-audit` o permanece documental hasta cerrar el modelo.
- Definir el handoff de salida cuando el modelo esté suficientemente consolidado.

## 12. Referencias Git

- Commit de alta (creación del MANIFEST) = `created_from_knowledge_commit`: `84d8845`.

## 13. Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 0.1.0 | 2026-08-23 | Alta del THREAD vía MANIFEST (`origin.type: USER_DECLARED`) durante la consolidación de coherencia estructural; incorporación del contexto del HANDOFF de creación retirado. |
