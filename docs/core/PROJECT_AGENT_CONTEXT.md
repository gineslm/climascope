# ClimaScope — Contexto del proyecto para agentes

**Versión:** 2.0.0  
**Estado:** Activo  
**Idioma:** español (España)  
**Repositorio:** `gineslm/climascope`  
**Rama raíz de conocimiento:** `knowledge`

## 1. Función

Este documento es el punto de integración mínimo entre cualquier agente de IA y el repositorio. No redefine la arquitectura: remite a las fuentes canónicas y establece cómo comenzar una sesión de trabajo.

La conversación es una instancia temporal. El repositorio es la memoria duradera.

## 2. Fuentes canónicas

- Arquitectura de THREADs: `docs/core/THREAD_ARCHITECTURE.md`.
- Reglas permanentes: `docs/core/PROJECT_WORKING_RULES.md`.
- Bootstrap operativo: `docs/core/THREAD_CONTEXT_BOOTSTRAP.md`.
- Estrategia Git: `docs/core/GIT_COMMIT_RULES.md`.
- Índice de THREADs: `docs/core/THREAD_INDEX.md`.
- Índice documental: `docs/core/DOCUMENT_INDEX.md`.
- Plantilla del índice de THREADs: `docs/core/THREAD_INDEX_TEMPLATE.md`.
- Plantilla del índice documental: `docs/core/DOCUMENT_INDEX_TEMPLATE.md`.

## 3. Regla de entrada

Toda sesión comienza conceptualmente en `knowledge`.

Orden mínimo:

```text
knowledge
  ↓
reglas + arquitectura
  ↓
THREAD_INDEX / DOCUMENT_INDEX
  ↓
MANIFEST del THREAD
  ↓
HANDOFF del THREAD
  ↓
corpus relevante
  ↓
rama de trabajo, si procede
```

El agente se incorpora a un THREAD **mediante su MANIFEST**. El HANDOFF no es memoria de sesión ni mecanismo de reincorporación: es la cola persistente de inputs todavía no resueltos.

## 4. Comandos de entrada

### «Conecta con el hilo `<thread_id>`»

1. localizar el THREAD en `THREAD_INDEX.md`;
2. leer su MANIFEST;
3. comprobar responsabilidad, estado y autoridad documental;
4. leer su único HANDOFF persistente;
5. consultar el corpus relevante mediante `DOCUMENT_INDEX.md` y referencias del MANIFEST;
6. operar sólo dentro de la responsabilidad resuelta.

### «Parte del handoff `<id>`»

El HANDOFF se utiliza como referencia de descubrimiento. Debe localizarse el THREAD receptor y después incorporarse mediante su MANIFEST. Si existe un HANDOFF provisional para una responsabilidad aún sin MANIFEST, el THREAD todavía no existe y debe darse de alta antes de operar como tal.

### «Declaro una responsabilidad nueva»

Comprobar primero `THREAD_INDEX.md`. Si no existe THREAD compatible, crear simultáneamente el MANIFEST y su único HANDOFF persistente conforme a `THREAD_ARCHITECTURE.md`.

### «Reincorpórate al contexto del proyecto»

Reconstruir el estado desde `knowledge`, comparar el trabajo de la conversación con el repositorio y hacer explícitas las discrepancias antes de modificar conocimiento autoritativo.

## 5. Autoridad documental

El corpus es común para lectura. `DOCUMENT_INDEX.md` permite descubrir qué THREAD tiene autoridad de evolución sobre cada documento.

Un THREAD nunca modifica directamente un documento bajo autoridad de otro THREAD. Registra una propuesta en el HANDOFF del THREAD responsable.

La autoridad de un documento es única. Si varias responsabilidades confluyen de forma estable, debe existir un THREAD gestor que centralice su evolución.

## 6. Regla de cierre de una sesión

Una sesión no genera un HANDOFF nuevo. Antes de terminar:

- consolidar conocimiento vigente dentro de la autoridad del THREAD;
- registrar propuestas fuera de alcance en los HANDOFFs receptores;
- mantener en el HANDOFF propio sólo lo que siga pendiente;
- retirar una entrada resuelta en el mismo commit que aplica o registra su decisión;
- usar Git como historial de lo resuelto.

## 7. Bloque compacto

> Repositorio: `gineslm/climascope`. Fuente de verdad: `knowledge`.
>
> Lee `PROJECT_WORKING_RULES.md`, `THREAD_ARCHITECTURE.md`, `THREAD_INDEX.md` y `DOCUMENT_INDEX.md`. Localiza el THREAD objetivo y conéctate mediante su MANIFEST. Después consulta su HANDOFF únicamente como cola de pendientes y el corpus relevante. El corpus es global para lectura; sólo modifica documentos bajo autoridad de tu THREAD. Para cambios fuera de alcance, registra una propuesta en el HANDOFF del THREAD responsable. Git conserva el historial de decisiones resueltas.

## 8. Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 2.0.0 | 2026-09-08 | Consolidación del contexto de agente conforme a Arquitectura 1.0.0, HANDOFF persistente, índices separados y autoridad documental única. |
