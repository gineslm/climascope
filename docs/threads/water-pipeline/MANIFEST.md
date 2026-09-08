# ClimaScope — MANIFEST · thread-water-pipeline

**Versión:** 1.0.1  
**Estado del THREAD:** ACTIVE  
**Ciclo:** 1  
**Idioma:** español (España)

## Identidad

```yaml
thread_id: thread-water-pipeline
domain: adquisición, QC y agregación de datos de agua/precipitación
status: ACTIVE
owner: línea de dominio de datos de agua
current_cycle: 1
origin:
  type: USER_DECLARED
  source_id: conversation
repository:
  knowledge_branch: knowledge
  created_from_knowledge_commit: a496358306e6a346aee6a4614f37cf7b8a4b7e0b
  work_branch: agent/water-pipeline-audit
handoff:
  path: docs/threads/water-pipeline/HANDOFF.md
  status: ACTIVE
```

## Responsabilidad

Adquirir, controlar la calidad y agregar datos de agua/precipitación, preservando trazabilidad y la distinción entre observado, derivado y modelado, sin convertir datos faltantes en cero.

## Dentro de alcance

- adquisición AEMET de clima y precipitación;
- QC de precipitación;
- agregación mensual/anual W2;
- auditoría de fuentes de agua;
- almacenamiento y trazabilidad raw/processed/derived;
- documentación técnica y científica del pipeline.

## Fuera de alcance

- Water Score definitivo;
- interpolación de producción;
- modelo Station / Location / Scope / Evidence;
- UI / mapa;
- adquisición indiscriminada sin priorización.

## Autoridad documental vigente

- `docs/threads/water-pipeline/AUDIT_REPORT.md`
- `docs/threads/water-pipeline/SOURCE_AUDIT.md`
- `docs/threads/water-pipeline/W1_PRECIPITATION_QC.md`

## Dependencias

- documentos core de reglas y arquitectura;
- `thread-station-location-evidence` consume resultados W2, sin transferir autoridad sobre estos documentos.

## Estado actual

W2 está implementado y validado localmente. La adquisición e investigación se amplían de forma progresiva y priorizada.

## HANDOFF

`docs/threads/water-pipeline/HANDOFF.md` es la única cola persistente de inputs pendientes de este THREAD.

## Cuestiones abiertas

- decidir si el ciclo continúa con nuevas fuentes/variables o entra en mantenimiento;
- proponer cambios a scoring/indicadores cuando exista un THREAD responsable de esa línea.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.1 | 2026-09-08 | Se retira `created`: Git ya conserva la fecha de alta del MANIFEST. |
