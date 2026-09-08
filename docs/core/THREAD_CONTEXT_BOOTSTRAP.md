# ClimaScope — Bootstrap de contexto de THREADs

**Versión:** 2.0.0  
**Estado:** Activo  
**Idioma:** español (España)  
**Repositorio:** `gineslm/climascope`  
**Rama raíz de conocimiento:** `knowledge`

## 1. Propósito

Este documento define la secuencia operativa reutilizable para incorporar una conversación/agente a ClimaScope. El modelo subyacente vive en `docs/core/THREAD_ARCHITECTURE.md`.

La conversación es temporal; el THREAD y el corpus viven en el repositorio.

## 2. Secuencia obligatoria

```text
knowledge
  ↓
PROJECT_WORKING_RULES.md
  ↓
THREAD_ARCHITECTURE.md
  ↓
THREAD_INDEX.md + DOCUMENT_INDEX.md
  ↓
MANIFEST del THREAD
  ↓
HANDOFF del THREAD
  ↓
corpus relevante
  ↓
rama de trabajo, si procede
```

Nunca reconstruir el estado global desde una rama de trabajo ni desde el histórico de una conversación.

## 3. Resolver el THREAD

### THREAD existente

1. localizarlo en `docs/core/THREAD_INDEX.md`;
2. leer su MANIFEST;
3. verificar estado, responsabilidad y autoridad documental;
4. leer su único HANDOFF persistente;
5. descubrir documentos relevantes mediante `docs/core/DOCUMENT_INDEX.md` y las dependencias del MANIFEST.

### Responsabilidad nueva

Si no existe un THREAD compatible:

1. crear su MANIFEST;
2. crear simultáneamente su único HANDOFF persistente;
3. declarar responsabilidad, alcance, autoridad documental y dependencias;
4. registrar `origin.type` y, cuando corresponda, `created_from_knowledge_commit`;
5. consolidar ambos artefactos en `knowledge`.

Un HANDOFF provisional puede preceder al MANIFEST cuando una responsabilidad nueva sea propuesta por otro THREAD. No existe THREAD hasta que se crea su MANIFEST.

## 4. Incorporación del agente

El agente se incorpora **mediante el MANIFEST**.

El HANDOFF no es un resumen de sesión ni una vía alternativa de incorporación. Se consulta después del MANIFEST para conocer únicamente inputs todavía no resueltos.

## 5. Corpus documental

El corpus es común para lectura. `DOCUMENT_INDEX.md` permite descubrir documentos, ámbito y autoridad de evolución.

Un THREAD puede leer cualquier documento necesario, pero sólo puede modificar directamente los que estén bajo su autoridad. Si necesita cambiar otro documento, registra una propuesta en el HANDOFF del THREAD responsable.

La autoridad de un documento es única. Los documentos transversales se gobiernan mediante un THREAD gestor cuando sea necesario.

## 6. Contrato de trabajo de la sesión

Antes de trabajo sustantivo, la conversación debe poder identificar:

```text
THREAD:
Responsabilidad:
Estado:
Dentro de alcance:
Fuera de alcance:
Documentos bajo autoridad directa:
Corpus/dependencias relevantes:
HANDOFF:
Rama de trabajo, si procede:
Validación requerida:
```

## 7. Propuestas fuera de alcance

Cuando aparezca una necesidad fuera de la autoridad del THREAD:

```text
PROPUESTA
Origen:
THREAD receptor:
Necesidad:
Contexto:
Evidencia:
¿Bloquea?: sí/no
```

Registrar la propuesta en el HANDOFF del receptor. La entrada no implica aceptación ni dependencia automática.

## 8. Resolución de una entrada HANDOFF

Mientras está abierta, la entrada permanece en el HANDOFF.

Cuando el THREAD receptor adopta una decisión terminal:

```text
entrada pendiente
      ↓
decisión
      ↓
cambio real o rechazo
      ↓
retirar entrada
      ↓
MISMO COMMIT
```

Git conserva el historial; el HANDOFF vuelve a representar sólo el presente pendiente.

## 9. Disciplina Git

Aplicar `docs/core/GIT_COMMIT_RULES.md`:

- un commit = una decisión;
- el mensaje explica el porqué;
- no duplicar metadatos que Git ya conserva;
- conservar SHAs explícitos sólo cuando tengan significado semántico o reproducible.

## 10. Cierre de una sesión

Antes de finalizar:

```text
Trabajo completado:
Documentos modificados:
Propuestas registradas en otros HANDOFFs:
Pendientes que permanecen en el HANDOFF propio:
Validación/tests:
Decisiones consolidadas:
Incertidumbre restante:
```

Finalizar una conversación no crea ni reemplaza el HANDOFF del THREAD.

## 11. Versión compacta

> Trabaja contra `gineslm/climascope`. Entra por `knowledge`; lee `PROJECT_WORKING_RULES.md`, `THREAD_ARCHITECTURE.md`, `THREAD_INDEX.md` y `DOCUMENT_INDEX.md`. Localiza el THREAD y conéctate mediante su MANIFEST. Después consulta su HANDOFF sólo como cola de pendientes y lee el corpus necesario. Todos los THREADs pueden leer el corpus; sólo editan documentos bajo su autoridad. Para cambios externos, registra una propuesta en el HANDOFF responsable. Una entrada resuelta sale del HANDOFF en el mismo commit que aplica o registra la decisión; Git conserva el historial.

## 12. Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 2.0.0 | 2026-09-08 | Bootstrap consolidado conforme a Arquitectura 1.0.0 e índices materializados separados. |
