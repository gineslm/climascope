# ClimaScope — Manifest del hilo Water Pipeline

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
thread_id: thread-water-pipeline
domain: adquisición, QC y agregación de datos de agua/precipitación (pipeline W)
status: ACTIVE
owner: línea de dominio de datos de agua del proyecto
created: 2026-08-23
current_cycle: 1
origin:
  type: USER_DECLARED
  source_id: conversation
repository:
  knowledge_branch: knowledge
  created_from_knowledge_commit: a496358306e6a346aee6a4614f37cf7b8a4b7e0b
  work_branch: agent/water-pipeline-audit
```

`created_from_knowledge_commit` es el commit de `knowledge` desde el que se da de alta este THREAD mediante la creación de su MANIFEST; es histórico e inmutable. El trabajo previo de este hilo (auditoría de fuentes y pipeline W0–W2) queda documentado en sus informes; esta alta formaliza su identidad en el registro.

## 2. Responsabilidad

Adquirir, controlar la calidad y agregar datos de agua/precipitación (AEMET y otras fuentes), preservando la trazabilidad y la distinción entre observado, derivado y modelado, sin convertir datos faltantes en cero.

## 3. Dentro de alcance

- adquisición AEMET de clima y precipitación;
- control de calidad (QC) de precipitación;
- agregación W2 (mensual/anual) y sus métricas de cobertura/completitud;
- auditoría de fuentes de agua (AEMET, MITECO/SNCZI, masas de agua, sequía, embalses);
- almacenamiento raw/processed/derived con trazabilidad;
- documentación versionada del pipeline.

## 4. Fuera de alcance

- Water Score / CRS definitivo;
- interpolación de producción;
- modelo de dominio Station / Location / Scope / Evidence (responsabilidad de `thread-station-location-evidence`);
- UI / mapa;
- ampliación indiscriminada de adquisición sin priorización.

## 5. Documentos autoritativos

- `docs/threads/water-pipeline/AUDIT_REPORT.md` — informe de auditoría del pipeline de agua (W2 implementado y validado; v0.3.1).
- `docs/threads/water-pipeline/SOURCE_AUDIT.md` — auditoría inicial de fuentes (W0/W1).
- `docs/threads/water-pipeline/W1_PRECIPITATION_QC.md` — semántica y QC de precipitación (W1).

## 6. Dependencias

- `docs/core/PROJECT_WORKING_RULES.md` — reglas permanentes (trazabilidad, datos, dominio).
- `docs/core/THREAD_ARCHITECTURE.md` — arquitectura de hilos.
- `thread-station-location-evidence` — consume las salidas W2 para el modelo de dominio (dependencia entre líneas, sin transferencia de responsabilidad).

## 7. Estado actual

W2 (agregación mensual/anual de precipitación) implementado y validado localmente (13 tests superados tras el último cambio de agregación). La auditoría se realizó alrededor de las estaciones AEMET `8416`, `3195` y `7012D`. La adquisición e investigación se amplían de forma progresiva y priorizada.

## 8. HANDOFF actual e histórico

```yaml
current_handoff: none
handoff_history: []
```

## 9. Validación

Las salidas deben conservar totales observados, exponer días faltantes/cobertura/completitud, no convertir missing en cero, y mantener la trazabilidad a fuente, periodo, transformación y estado de QC.

## 10. Cuestiones abiertas

- Confirmar si el ciclo actual continúa con nuevas fuentes/variables o queda en mantenimiento tras W2.
- Definir el handoff de salida hacia scoring/indicadores cuando exista esa línea.

## 11. Referencias Git

- Commit de alta (creación del MANIFEST) = `created_from_knowledge_commit`: `a496358`.
- Rama de trabajo asociada: `agent/water-pipeline-audit`.

## 12. Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 0.1.0 | 2026-08-23 | Alta del THREAD vía MANIFEST (`origin.type: USER_DECLARED`) durante la reorganización 2C; formaliza la línea de datos de agua que ya había producido la auditoría W0–W2. |
