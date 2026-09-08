# ClimaScope — MANIFEST · thread-station-location-evidence

**Versión:** 1.0.1  
**Estado del THREAD:** ACTIVE  
**Ciclo:** 1  
**Idioma:** español (España)

## Identidad

```yaml
thread_id: thread-station-location-evidence
domain: modelo de dominio Station / Location / Scope / Evidence
status: ACTIVE
owner: línea de dominio científico del proyecto
current_cycle: 1
origin:
  type: USER_DECLARED
  source_id: conversation
repository:
  knowledge_branch: knowledge
  created_from_knowledge_commit: 84d8845ce2475e7d0c860bdc27b5afe4816675b8
  work_branch: agent/water-pipeline-audit
handoff:
  path: docs/threads/station-location-evidence/HANDOFF.md
  status: ACTIVE
```

## Responsabilidad

Diseñar y documentar el modelo de dominio que relaciona Station, Location, Scope/Representativeness y Evidence, manteniendo separadas las observaciones directas de estación de los valores relevantes o modelados para una ubicación.

## Dentro de alcance

- modelo canónico `Station`;
- modelo `Location`;
- `Scope / Representativeness`;
- abstracción `Evidence`;
- cardinalidades y relaciones;
- procedencia y trazabilidad;
- estados de adquisición/investigación;
- requisitos mínimos para el mapa;
- prerrequisitos de futura interpolación.

## Fuera de alcance

- Water Score definitivo;
- implementación de interpolación;
- rediseño del pipeline W2;
- adquisición AEMET masiva;
- UI final;
- arquitectura general de THREADs.

## Autoridad documental vigente

- `docs/threads/station-location-evidence/MODEL.md`

## Dependencias

- `docs/threads/water-pipeline/AUDIT_REPORT.md`
- documentos core de reglas y arquitectura.

## Decisiones vigentes

1. Una observación de estación no equivale automáticamente al valor de una ubicación cercana.
2. La representatividad espacial debe ser explícita.
3. Deben distinguirse observado en estación, relevante para ubicación y modelado/interpolado.
4. La interpolación queda aplazada hasta disponer de requisitos, trazabilidad e incertidumbre.
5. La adquisición y la investigación son progresivas.
6. `not_assessed` nunca significa ausencia de riesgo.
7. Evidencia cuantitativa y documental son tipos distintos asociables a una ubicación.
8. Debe preservarse la trazabilidad de AEMET raw/W2 salvo migración deliberada.

## HANDOFF

`docs/threads/station-location-evidence/HANDOFF.md` es la única cola persistente de inputs pendientes de este THREAD.

## Cuestiones abiertas

- cerrar el modelo documental antes de implementar;
- decidir cuándo el ciclo pasa de diseño a implementación.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.1 | 2026-09-08 | Se retira `created`: Git ya conserva la fecha de alta del MANIFEST. |
