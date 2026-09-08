# ClimaScope — Reglas de trabajo del proyecto

**Versión:** 2.0.0  
**Estado:** Activo  
**Idioma:** español (España)  
**Repositorio:** `gineslm/climascope`  
**Rama raíz de conocimiento:** `knowledge`

## 1. Propósito

Estas reglas son el contrato operativo permanente de ClimaScope. Existen para que el método, la trazabilidad, la coordinación entre THREADs y la producción de conocimiento no dependan de la memoria de una conversación.

La arquitectura detallada vive en `docs/core/THREAD_ARCHITECTURE.md`.

## 2. Fuente de verdad y ramas

```text
knowledge → conocimiento y estructura consolidados
develop   → integración del software
main      → software estable/desplegable
```

Toda conversación nueva entra conceptualmente por `knowledge` antes de usar una rama de trabajo.

Las ramas `agent/*`, `feature/*` u otras ramas temporales son espacios de trabajo, no fuentes alternativas de verdad global.

## 3. Unidad persistente de trabajo

La unidad persistente es el THREAD, no el chat.

- Un THREAD existe si y sólo si existe su MANIFEST en `knowledge`.
- Todo THREAD existente tiene exactamente un HANDOFF persistente.
- Un agente se incorpora mediante el MANIFEST.
- El HANDOFF contiene sólo inputs todavía no resueltos.
- Una conversación puede terminar sin cerrar el THREAD.

## 4. Descubrimiento

- `docs/core/THREAD_INDEX.md` descubre THREADs y sus MANIFEST/HANDOFF.
- `docs/core/DOCUMENT_INDEX.md` descubre el corpus documental y su autoridad de evolución.
- Ambos índices son derivados y no autoritativos.
- Las formas canónicas de ambos índices viven en sus plantillas de `docs/core/`.

Si un índice contradice a su fuente autoritativa, prevalece la fuente autoritativa y el índice debe regenerarse.

## 5. Responsabilidad y autoridad documental

Cada THREAD custodia el estado de un problema o línea de trabajo y gobierna la evolución del conocimiento dentro de su responsabilidad.

El corpus es común para lectura: cualquier THREAD puede consultar cualquier documento necesario.

La autoridad de evolución de cada documento es **única**. Un THREAD sólo modifica directamente documentos bajo su autoridad. Si necesita cambiar conocimiento gobernado por otro THREAD, registra una propuesta en el HANDOFF del THREAD responsable.

Si un documento es semánticamente transversal y varias responsabilidades necesitan influir de forma estable, no se comparte la edición: se crea un THREAD gestor que centraliza su evolución y recibe inputs de los demás.

Git conserva la procedencia histórica. No es necesario añadir `created_by` u otros historiales manuales para reconstruir quién creó o modificó un documento.

## 6. HANDOFF

El HANDOFF no es transición de sesión, resumen de conversación ni transferencia de agente.

Es la cola persistente de propuestas, revisiones, necesidades o tareas inter-THREAD todavía no resueltas.

Reglas:

1. cualquier THREAD puede registrar una entrada dirigida al receptor con contexto y evidencia;
2. sólo el THREAD receptor puede gestionar su estado y resolverla;
3. estados terminales no permanecen en el HANDOFF;
4. al resolverse, la entrada se retira en el mismo commit que aplica la decisión o registra su rechazo;
5. Git conserva el historial y el mensaje del commit conserva el porqué.

## 7. Git como historial de decisiones

La estrategia completa vive en `docs/core/GIT_COMMIT_RULES.md`.

Principio: **un commit = una decisión**.

No duplicar en documentos lo que Git ya conserva: fecha, autor, SHA, archivos afectados y diff. Las referencias a SHAs sólo se mantienen cuando tienen significado semántico o de reproducibilidad.

## 8. Consolidación de conocimiento

Un cambio se consolida cuando pasa a formar parte del estado autoritativo del proyecto.

```text
trabajo / análisis
      ↓
resultado persistente
      ↓
actualizar conocimiento / MANIFEST / HANDOFF cuando proceda
      ↓
COMMIT
      ↓
knowledge
```

No todo borrador requiere consolidación. Sí la requieren las decisiones, cambios documentales autoritativos, cambios de MANIFEST/HANDOFF y conocimiento validado.

## 9. Cierre de trabajo

Antes de cerrar una tarea o sesión sustantiva:

1. ejecutar validaciones/tests relevantes;
2. actualizar el conocimiento vigente dentro de la autoridad del THREAD;
3. registrar propuestas fuera de alcance en los HANDOFFs responsables;
4. revisar el HANDOFF propio;
5. retirar cualquier entrada resuelta en el mismo commit que aplica o registra la decisión;
6. consolidar en `knowledge` los cambios de conocimiento/estructura;
7. indicar incertidumbre o evidencia todavía faltante.

Cerrar una sesión no crea un HANDOFF. Cerrar un THREAD tampoco elimina su HANDOFF persistente.

## 10. Reglas de datos y evidencia

ClimaScope distingue hechos de fuente, datos derivados, valores modelados y evidencia documental.

Reglas no negociables:

- nunca convertir silenciosamente missing en cero;
- preservar material raw y procedencia;
- distinguir observado, derivado y modelado/interpolado;
- conservar método, transformación y QC;
- `not_assessed` nunca significa ausencia de riesgo;
- una observación de estación no equivale automáticamente al valor de una ubicación cercana.

## 11. Datos raw / processed / derived

La dirección objetivo es:

```text
data/
├── raw/
├── processed/
├── derived/
└── reports/
```

No mover datos existentes sólo por estilo. Una migración de datos requiere decisión explícita y trazabilidad.

## 12. Adquisición e investigación progresivas

No descargar ni investigar exhaustivamente todas las ubicaciones antes de priorizar.

Flujo preferido:

```text
candidata
  → cribada
  → datos adquiridos
  → QC
  → investigación documental priorizada
  → evaluada
```

## 13. Modelo Station / Location / Evidence

Debe distinguirse al menos:

```text
Station → observaciones
Location → lugar evaluado
Scope/Representativeness → relevancia espacial
Evidence → soporte cuantitativo, derivado o documental
```

La interpolación se aplaza hasta disponer de modelo, método, trazabilidad e incertidumbre explícitos.

## 14. Punto de entrada operativo

La secuencia reutilizable de incorporación vive en `docs/core/THREAD_CONTEXT_BOOTSTRAP.md` y el contexto mínimo para agentes en `docs/core/PROJECT_AGENT_CONTEXT.md`.

## 15. Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 2.0.0 | 2026-09-08 | Consolidación de reglas conforme a Arquitectura 1.0.0: HANDOFF persistente, índices separados, autoridad documental única y Git como historial. |
