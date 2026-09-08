# ClimaScope — Contexto del proyecto para el agente asistente

**Versión:** 1.5.1  
**Estado:** Activo  
**Repositorio:** `gineslm/climascope`  
**Rama de consolidación documental:** `knowledge`

> **Idioma oficial del proyecto: español (España).** Las conversaciones y la documentación deben desarrollarse en castellano, salvo términos técnicos que convenga conservar en su forma original.

## Propósito y rol de este documento

Este documento es el **punto de integración entre el agente asistente y el repositorio**. Es agnóstico respecto a qué agente se utilice. No redefine el método del proyecto: lo referencia. Su contenido propio son los *comandos de entrada* con los que el usuario abre una conversación y el *bloque compacto* que se pega en el contexto permanente del agente.

Fuentes canónicas (no se reproducen aquí):

- **Modelo de bootstrap** (entrada, alta vía MANIFEST, reincorporación): `docs/core/THREAD_ARCHITECTURE.md` §9.
- **Secuencia operativa de arranque**: `docs/core/THREAD_CONTEXT_BOOTSTRAP.md`.
- **Reglas permanentes** (ramas, consolidación, trazabilidad, alcance, cierre): `docs/core/PROJECT_WORKING_RULES.md`.
- **Forma canónica del índice materializado de THREADs**: `docs/core/THREAD_INDEX_TEMPLATE.md`.
- **Forma canónica del índice materializado del corpus documental**: `docs/core/DOCUMENT_INDEX_TEMPLATE.md`.

El repositorio es la memoria duradera; una conversación es una sesión de trabajo acotada, no la fuente de verdad. `knowledge` es el punto de entrada para descubrir el estado consolidado; `develop` y `main` son el ciclo del software.

## Comandos de entrada del proyecto

Disparadores con los que el usuario abre una conversación. En todos, el estado vigente se resuelve desde `knowledge` según `docs/core/THREAD_ARCHITECTURE.md` §9.

- **«Parte del handoff `<id>`»** — localizar el HANDOFF en `knowledge`. Si declara un THREAD receptor inexistente, darlo de alta creando su MANIFEST como primera tarea (con `origin.type: THREAD_DERIVED`; el HANDOFF es el vehículo de transferencia, no el origen). El MANIFEST determina después el estado vigente.
- **«Conecta con el hilo `<thread_id>`»** — localizar su MANIFEST en `knowledge` y usar su estado vigente, HANDOFF actual y referencia Git.
- **«Declaro una responsabilidad nueva»** — comprobar en `knowledge` si existe un THREAD compatible; si no, darlo de alta creando su MANIFEST con `origin.type: USER_DECLARED`.
- **«Reincorpórate al contexto del proyecto»** — para una conversación iniciada antes de instalar este contexto: leer las reglas, la arquitectura y la documentación vigente desde `knowledge`; comparar el trabajo ya hecho con el repositorio; clasificar las discrepancias (`NUEVO`, `OBSOLETO`, `CONFLICTO`, `DUPLICADO`, `FUERA DE ALCANCE`) y proponer sincronización sin sobrescribir el repositorio en caso de conflicto.

El detalle del contrato de responsabilidad, la disciplina de alcance, la sincronización, la distinción propuesta/decisión, la jerarquía documental y el protocolo de cierre están en `docs/core/PROJECT_WORKING_RULES.md` y `docs/core/THREAD_CONTEXT_BOOTSTRAP.md`; no se repiten aquí.

Cuando exista un índice materializado de THREADs o documentos, debe interpretarse y regenerarse según `docs/core/THREAD_INDEX_TEMPLATE.md` y `docs/core/DOCUMENT_INDEX_TEMPLATE.md`, respectivamente. Los índices son mecanismos de descubrimiento y no sustituyen a las fuentes autoritativas que referencian.

## Bloque compacto para el agente asistente

> **Espejo de `docs/core/THREAD_CONTEXT_BOOTSTRAP.md` §12.** Esta es la única duplicación tolerada del proyecto: se conserva por comodidad de pegado en el contexto permanente del agente. **No editar aquí**; editar en el canónico y regenerar esta copia.

> **ClimaScope — bootstrap de conversación**
>
> Repositorio: `gineslm/climascope`  
> Fuente de verdad: GitHub  
> Raíz de conocimiento: `knowledge`
>
> Antes de trabajar, entra conceptualmente en `knowledge`, lee `docs/core/PROJECT_WORKING_RULES.md` y `docs/core/THREAD_ARCHITECTURE.md`, y después el informe, MANIFEST o HANDOFF aplicable. No inventes documentos ausentes.
>
> Si se identifica una responsabilidad nueva y no existe THREAD compatible, da de alta el THREAD creando su MANIFEST con `origin.type: USER_DECLARED` (no hay un artefacto de declaración aparte). El MANIFEST debe registrar `created_from_knowledge_commit` con el commit de `knowledge` desde el que se da de alta el THREAD; es histórico e inmutable y el estado vigente se resuelve siempre desde `knowledge`.
>
> Mantén esta conversación acotada. Si aparece una dependencia adyacente, regístrala como fuera de alcance. Al terminar, informa de archivos, tests, versiones documentales, rama, SHA de trabajo y SHA de consolidación en `knowledge` cuando corresponda.

## Mantenimiento

Este documento es el punto de integración con el agente y un **espejo** del bloque operativo canónico. Cuando cambie el método de arranque, editar los canónicos (`docs/core/THREAD_ARCHITECTURE.md` §9 y `docs/core/THREAD_CONTEXT_BOOTSTRAP.md`) y regenerar desde ellos el bloque compacto de arriba. La copia colocada en el contexto permanente del agente debe actualizarse entonces a partir de este documento.

Las plantillas `docs/core/THREAD_INDEX_TEMPLATE.md` y `docs/core/DOCUMENT_INDEX_TEMPLATE.md` son las referencias canónicas para interpretar o regenerar los índices materializados y deben mantenerse enlazadas desde este contexto de agente.

## Historial de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1.3.0 | 2026-08-17 | Alineación con Arquitectura 0.5.0 (Alt 1): alta = crear el MANIFEST; retirada de la «declaración» de THREAD; `origin.type` sin `HANDOFF`. |
| 1.4.0 | 2026-08-23 | Consolidación del bootstrap (M1) y renombrado a `PROJECT_AGENT_CONTEXT.md`, agnóstico respecto al agente: el documento se reduce a comandos de entrada y bloque compacto (espejo de `THREAD_CONTEXT_BOOTSTRAP.md` §12); el protocolo detallado se remite a los canónicos. |
| 1.5.0 | 2026-08-23 | Reorganización 2C: todas las rutas actualizadas a `docs/core/…`; bloque espejo regenerado desde `THREAD_CONTEXT_BOOTSTRAP.md` §12. |
| 1.5.1 | 2026-09-08 | Se referencian las plantillas canónicas de índice de THREADs y de corpus documental como fuentes de descubrimiento. |
