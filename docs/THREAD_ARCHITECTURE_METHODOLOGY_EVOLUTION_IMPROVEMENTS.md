# Registro de mejoras — thread-architecture-methodology-evolution

**Estado:** Activo
**Idioma:** español (España)
**Ámbito:** propuestas de mejora de arquitectura, metodología y reglas operativas
detectadas por este THREAD o recibidas de otros THREAD.

## Formato mínimo de *improvement record*

Este formato queda definido a partir del primer caso real (IMP-002), según pedía el
HANDOFF, sin introducir complejidad innecesaria. Campos obligatorios:

- `id`: identificador estable (`IMP-NNN`).
- `status`: estado del ciclo — `observation` | `proposal` | `under_review` |
  `accepted` | `rejected` | `deferred`.
- `consolidation`: `none` | `pending` | `done` (con SHA cuando `done`).
- `type`: categoría breve (p. ej. `architecture / traceability`).
- `origin_thread`: THREAD de origen de la observación.
- `summary`: descripción concisa de la mejora.
- `evidence`: referencia al documento/estado/conversación que la origina.
- `decision`: decisión y justificación (obligatorio al cerrar).

Campos opcionales: `impact`, `affected`, `next_action`.

Ciclo: `observation → proposal → under_review → accepted/rejected/deferred →
consolidated (si procede)`.

## Relación causal (descomposición de IMP-004)

IMP-004 es la raíz ontológica; IMP-005…IMP-008 son unidades de trazabilidad
dependientes. No obligan a un commit por unidad: la revisión 0.5.0 puede consolidarlas
en uno o varios commits.

```text
IMP-004  (ontología/terminología del THREAD — raíz)
  ├── IMP-005  (alta y ciclo de vida del THREAD)
  ├── IMP-006  (operación Crear vs Conectar)
  ├── IMP-007  (procedencia / legacy / MIGRATED)
  └── IMP-008  (REGISTRO e ÍNDICE)
```

Instancias/consecuencias previas: IMP-002 es instancia de IMP-005; la parte legacy de
IMP-003 se integra en IMP-007.

## Registro

### IMP-001

- `status`: `accepted`
- `consolidation`: `done`
- `type`: `architecture / traceability`
- `origin_thread`: pruebas de bootstrap previas a la creación de este THREAD
- `summary`: distinguir `created_from_knowledge_commit` (base histórica) del estado
  vigente de `knowledge`.
- `evidence`: `THREAD_ARCHITECTURE_METHODOLOGY_EVOLUTION(.md/_HANDOFF.md)`.
- `decision`: aceptada e incorporada a `THREAD_ARCHITECTURE.md`,
  `THREAD_CONTEXT_BOOTSTRAP.md` y MANIFESTs posteriores.

> Nota: IMP-001 ya existía en el HANDOFF; se traslada aquí para unificar el registro.

### IMP-002

- `status`: `accepted`
- `consolidation`: `done` (`4ab71c6`)
- `type`: `architecture / coherence`
- `origin_thread`: `thread-architecture-methodology-evolution` (autodetección al
  ejecutar "Conecta con el hilo")
- `summary`: el THREAD carecía de MANIFEST pese a que la arquitectura lo exige como
  autoridad del estado actual y como primer punto de consulta al conectar. La
  conexión tuvo que reconstruirse desde la declaración y el HANDOFF, práctica que la
  propia arquitectura desaconseja.
- `evidence`: en el momento de la detección (`knowledge@1cb593d`) no existía
  `docs/THREAD_ARCHITECTURE_METHODOLOGY_EVOLUTION_MANIFEST.md`; contraste con
  `THREAD_ARCHITECTURE.md` §7 ("El MANIFEST es la autoridad sobre el estado actual
  del THREAD"; "para conectar con un THREAD se consulta primero el MANIFEST") y con
  la regla de creación de THREAD `USER_DECLARED` (obliga a crear su MANIFEST).
- `impact`: reconexiones futuras no conformes al protocolo; riesgo de derivar estado
  desde HANDOFF histórico.
- `decision`: crear el MANIFEST del THREAD conforme a §7 y consolidarlo en `knowledge`.
  Justificación: restablece la conformidad del hilo con su propio protocolo de
  reconexión y resuelve el CONFLICTO con evidencia.
- `resolution`: MANIFEST consolidado en `knowledge` en el commit `4ab71c6`
  (`docs: alta de thread-architecture-methodology-evolution via MANIFEST (IMP-002)`).
  El THREAD queda formalmente de alta bajo Alt 1.
- `reevaluación (IMP-004)`: reclasificada como **instancia** de IMP-004/IMP-005. La
  causa raíz no es "falta un fichero MANIFEST" sino que el procedimiento de alta permite
  un estado limbo (declaración sin MANIFEST). La remediación (crear el MANIFEST) no
  cambia. Cuestión abierta derivada: el fichero de DECLARACIÓN de este hilo queda
  redundante con el MANIFEST; decidir si se deprecia (se tratará en IMP-005).

### IMP-003

- `status`: `under_review`
- `consolidation`: `none`
- `type`: `methodology / spec-ambiguity`
- `origin_thread`: `thread-architecture-methodology-evolution`
- `summary`: la referencia de conocimiento de un MANIFEST está definida de forma
  ambigua e implementada de forma inconsistente. (a) La semántica de
  `created_from_knowledge_commit` colisiona consigo misma cuando el MANIFEST se crea
  después de la declaración del THREAD; (b) coexisten cuatro formas de campo para el
  mismo concepto de "base histórica de conocimiento".
- `evidence`:
    - Ambigüedad de anclaje en `THREAD_ARCHITECTURE.md`:
        - línea 236: `created_from_knowledge_commit` = «este THREAD fue **declarado**
          a partir de este estado de `knowledge`» (ancla: declaración del THREAD).
        - líneas 356 y 374: registrar el SHA «utilizado para **crear el MANIFEST**»
          (ancla: creación del MANIFEST). Ambos anclajes divergen si el MANIFEST se
          materializa más tarde que la declaración — el caso exacto de este THREAD.
    - Misma ambigüedad latente en `THREAD_CONTEXT_BOOTSTRAP.md`: línea 56 = «desde el
      que **nació** el THREAD»; línea 244 = SHA «utilizado para **crearlo**» (el
      MANIFEST).
    - `PROJECT_WORKING_RULES.md`: silencio total sobre estos campos (ninguna
      coincidencia). No hay autoridad que resuelva el conflicto en las reglas.
    - Cuatro formas de campo para el mismo concepto histórico:
        1. `created_from_knowledge_commit: <sha>` (plano) — plantilla §7.1, bootstrap,
           HANDOFF de este THREAD.
        2. `knowledge_commit: <sha>` — campo ambiguo **prohibido por IMP-001**, aún
           en uso en `THREAD_MANIFEST_ARCHITECTURE_THREAD.md` (línea 25). Manifest no
           conforme.
        3. `created_from_knowledge:` + `branch/commit` (anidado) — usado en
           `THREAD_APP_SCOPE_UX_MANIFEST.md` (líneas 102-104), tras sustituir
           `knowledge_basis` según su changelog.
        4. `knowledge_basis:` + `branch/commit` — en `THREAD_ARCHITECTURE.md`
           (líneas 88-93), con propósito distinto (base reproducible de una
           implementación de software), pero semánticamente solapado.
- `impact`: reconexiones no deterministas; MANIFESTs no comparables; regla IMP-001
  incumplida en al menos un manifest; imposibilidad de automatizar comprobaciones de
  coherencia mientras haya cuatro formas.
- `decision`: **pendiente de consolidación** — semántica de campo único adoptada en
  los borradores de cambio; IMP-003 permanece `under_review` hasta consolidar.
- `next_action`: revisar los borradores de edición de `THREAD_ARCHITECTURE.md`,
  `THREAD_CONTEXT_BOOTSTRAP.md` y `PROJECT_WORKING_RULES.md` (opcional), y la
  `MIGRATION_PROPOSAL_knowledge_reference_fields.md` para los manifests ajenos. Al
  aprobarse y consolidarse, pasar a `accepted`/`consolidated` con SHA.

#### Propuesta de semántica inequívoca (para decisión, no adoptada)

Conceptos que deben nombrarse de forma distinta y no confundirse:

- **A — origen del THREAD:** estado de `knowledge` desde el que se *declaró* el
  THREAD. Inmutable, ligado al evento de declaración.
- **B — materialización del MANIFEST:** estado de `knowledge` al crear una versión
  del MANIFEST. En el flujo normal A = B; divergen si el MANIFEST se crea después.
- **C — base reproducible de software:** `knowledge_basis.commit`, ya definido y
  correcto para THREAD de software. Se mantiene sin cambios.

**Opción recomendada (campo único, mínima complejidad):**
fijar `created_from_knowledge_commit` = Concepto **A** (declaración del THREAD),
plano e inmutable, copiado verbatim en cada versión del MANIFEST y en el HANDOFF.
Se descarta un campo para B: la materialización del MANIFEST ya queda registrada por
git (commit que añade el fichero) y por el changelog/versión del propio MANIFEST.
Retirar `knowledge_commit` (ya prohibido) y la forma anidada `created_from_knowledge`;
conservar `knowledge_basis` solo para C.

- *Pros:* honra el principio operativo del THREAD (rastrear hasta el origen);
  coherente con la línea 236, con bootstrap l.56 y con lo ya escrito en el HANDOFF
  (`c2df5df`); no añade campos; deja una sola forma automatizable.
- *Contras:* obliga a corregir dos líneas de la arquitectura (356, 374) y a migrar
  dos manifests de otros THREAD; no captura B en un campo propio (se asume que git
  basta).

**Alternativa (dos campos):** `thread_declared_from_commit` (A) +
`manifest_created_from_commit` (B), retirando `created_from_knowledge_commit`.
- *Pros:* separa A y B sin ambigüedad.
- *Contras:* añade un campo; contradice el principio de mínima complejidad si B no
  aporta valor sobre git.

**Documentos a modificar (si se adopta la opción recomendada):**

1. `THREAD_ARCHITECTURE.md` — reescribir líneas 356 y 374 para anclar el campo a la
   *declaración del THREAD* (no a la creación del MANIFEST); declarar §7.1 como
   definición única; retirar explícitamente `knowledge_commit` y la forma anidada
   `created_from_knowledge`; mantener `knowledge_basis` para software.
2. `THREAD_CONTEXT_BOOTSTRAP.md` — corregir la línea 244 en el mismo sentido (l.56 ya
   es correcta); subir versión.
3. `PROJECT_WORKING_RULES.md` — añadir una referencia mínima a la definición canónica
   para que las reglas no queden mudas (prioridad baja).
4. `THREAD_MANIFEST_ARCHITECTURE_THREAD.md` — migrar `knowledge_commit` →
   `created_from_knowledge_commit` (**otro THREAD**: coordinación, no edición
   unilateral).
5. `THREAD_APP_SCOPE_UX_MANIFEST.md` — migrar forma anidada → plana (**otro THREAD**:
   coordinación).

> Disciplina de alcance: los puntos 4 y 5 pertenecen a otros THREAD. Este THREAD
> propone y coordina; no reescribe manifests ajenos por su cuenta.

- `reevaluación (IMP-004)`: la decisión de campo único **sobrevive y se simplifica**.
  Bajo la ontología de IMP-004, declarar ≡ crear el MANIFEST, por lo que "declaración
  del THREAD" y "creación del MANIFEST" dejan de ser dos momentos: A = B por
  construcción y la ambigüedad no reaparece en THREAD futuros. Queda una reconciliación
  *legacy* solo para este hilo (registró `c2df5df` sin MANIFEST): grandfather vs
  re-anclaje. La parte legacy se integra en IMP-007.

### IMP-004

- `status`: `under_review`
- `consolidation`: `none`
- `type`: `architecture / ontology / terminology`
- `origin_thread`: `thread-architecture-methodology-evolution` (hipótesis del usuario)
- `summary`: clarificación ontológica y terminológica del modelo THREAD. La
  arquitectura atribuye la "declaración/alta" de un THREAD a tres artefactos distintos
  (THREAD DECLARATION, MANIFEST y HANDOFF) y trata declaración y MANIFEST como pasos
  separados, lo que permite un estado limbo "declarado sin alta". Incluye además la
  corrección de la **taxonomía de `origin.type`**: el enum actual
  (`HANDOFF | USER_DECLARED | MIGRATED`) confunde origen con mecanismo. Propuesta:
  THREAD = entidad; el MANIFEST es el acto de alta; HANDOFF solo transfiere; formalizar
  REGISTRO e introducir ÍNDICE; nombrar AGENTE/CONVERSACIÓN; y fijar `origin.type` como
  eje único de origen de la responsabilidad con los valores
  `USER_DECLARED | THREAD_DERIVED | MIGRATED`.
- `origin.type` (semántica confirmada por el usuario):
    - `USER_DECLARED` — responsabilidad nueva declarada desde una conversación nueva.
    - `THREAD_DERIVED` — responsabilidad nacida del trabajo de otro THREAD; **absorbe el
      caso HANDOFF** (recibir por handoff es transferencia, no origen).
    - `MIGRATED` — importación de una conversación externa con contexto/documentos,
      adoptada como hilo con revisión de compatibilidad; implica procedimiento de
      admisión.
    - Corrección arquitectónica: retirar `HANDOFF` del enum, añadir `THREAD_DERIVED`,
      re-anclar `MIGRATED` al origen; arreglar §5.1 (l.172, l.176-178), diagrama §6
      (l.193) y §9.2 paso 7 (l.318).
- `evidence` (autocontenida, citas de `THREAD_ARCHITECTURE.md` en `knowledge`):
    - la "declaración/alta" se atribuye a tres artefactos distintos: §6 (THREAD
      DECLARATION «convierte una responsabilidad en una entidad persistente»), §10
      (el MANIFEST hace lo mismo) y la tabla de autoridad §16 + §13 (que asignan
      "declaración" al HANDOFF);
    - creación en dos pasos (declaración + MANIFEST) en §9.4 y §9.2;
    - `origin.type` mezcla origen y mecanismo: enum `HANDOFF | USER_DECLARED | MIGRATED`
      (§5.1 l.172-178, diagrama §6 l.193) y §9.2 paso 7 (l.318) fuerza
      `origin.type: HANDOFF`;
    - REGISTRO opcional/infra-especificado (§15); ÍNDICE ausente;
    - empírica: `THREAD_DERIVED` no aparece en el repo; único THREAD con
      declaración-fichero y sin MANIFEST era este hilo (resuelto en `4ab71c6`).
- `impact`: afecta al procedimiento de alta, a la taxonomía de origen y a varias
  secciones de `THREAD_ARCHITECTURE.md` y del bootstrap; salto de versión mayor. No
  requiere tocar manifests de otros THREAD.
- `relations`: IMP-002 es instancia de IMP-005; IMP-003 es consecuencia ya alineada
  (su parte legacy → IMP-007). Descomposición IMP-004→IMP-008 registrada en este
  documento (árbol causal arriba).
- `decision`: **pendiente** (no resolver por inferencia). Alt 1 adoptada como hipótesis
  de trabajo; taxonomía de origen confirmada; ambas pendientes de consolidar en la
  revisión 0.5.0.
- `next_action`: ejecutar la revisión 0.5.0 por bloques (arquitectura, bootstrap,
  reglas, contexto ChatGPT) como cambio de modelo, no como parche.

### IMP-005

- `status`: `under_review`
- `consolidation`: `none`
- `type`: `architecture / lifecycle`
- `depends_on`: IMP-004
- `origin_thread`: `thread-architecture-methodology-evolution`
- `summary`: alta y ciclo de vida del THREAD bajo Alt 1. Crear un THREAD = crear y
  consolidar su MANIFEST; regla anti-limbo ("existe si y solo si existe su MANIFEST");
  retirada del artefacto DECLARATION; HANDOFF inicial opcional/diferido; procedimiento
  de alta común con la admisión propia de MIGRATED como sub-paso.
- `evidence`: bajo Alt 1 (validada conceptualmente), crear un THREAD = crear su
  MANIFEST; contraste con §6/§9.4 (que separan DECLARATION y MANIFEST) y §5 (identidad
  en el MANIFEST). Caso real: este hilo estuvo en estado limbo hasta `4ab71c6`.
- `relations`: **absorbe IMP-002** como instancia (THREAD sin MANIFEST).
- `decision`: **pendiente** (se materializa en la revisión 0.5.0).

### IMP-006

- `status`: `under_review`
- `consolidation`: `none`
- `type`: `architecture / operations`
- `depends_on`: IMP-004
- `origin_thread`: `thread-architecture-methodology-evolution`
- `summary`: distinción explícita CREAR THREAD (alta de entidad vía MANIFEST) vs
  CONECTAR CON THREAD (localizar MANIFEST, resolver estado/HANDOFF, enganchar
  agente/conversación). Incluye la anomalía "conectar sin MANIFEST" (no operar como si
  existiera; formalizar o marcar inconsistencia).
- `evidence`: protocolo actual §9.3/§10 ya alineado en conexión («asocia una nueva
  instancia de conversación a un THREAD existente»; «no crea un nuevo THREAD»), pero
  desalineado en creación/transferencia (§9.4 doble paso; §10/§13 permiten al HANDOFF
  "declarar"). Anomalía observada en este ciclo: "conectar con THREAD" sin MANIFEST.
- `decision`: **pendiente**.

### IMP-007

- `status`: `under_review`
- `consolidation`: `none`
- `type`: `architecture / provenance`
- `depends_on`: IMP-004
- `origin_thread`: `thread-architecture-methodology-evolution`
- `summary`: `origin.type` como eje único de origen de la responsabilidad
  (`USER_DECLARED | THREAD_DERIVED | MIGRATED`): retirar `HANDOFF` del enum (queda en
  THREAD_DERIVED), re-anclar `MIGRATED` a importación/adopción con admisión. Semántica
  uniforme de `created_from_knowledge_commit` = commit de alta vía MANIFEST; la
  prehistoria de un MIGRATED vive en `origin.source_id`/corpus, no en el campo.
- `evidence`: enum actual `HANDOFF | USER_DECLARED | MIGRATED` (§5.1 l.172-178, diagrama
  §6 l.193) con `origin.type: HANDOFF` forzado en §9.2 (l.318); `THREAD_DERIVED` ausente
  en todo el repo. Semántica de origen confirmada por el usuario (importación externa =
  MIGRATED; recepción por handoff = THREAD_DERIVED).
- `relations`: integra la **parte legacy de IMP-003** (interpretación del campo para
  THREAD creados bajo el modelo previo).
- `decision`: **pendiente**.

### IMP-008

- `status`: `under_review`
- `consolidation`: `none`
- `type`: `architecture / registry-index`
- `depends_on`: IMP-004
- `origin_thread`: `thread-architecture-methodology-evolution`
- `summary`: formalizar el REGISTRO (Activity Log por-THREAD: actividad, decisiones,
  eventos) e introducir el PROJECT INDEX como artefacto **derivado y no autoritativo**,
  reconstruible desde los MANIFEST (si discrepa, prevalece el MANIFEST). Sustituir el
  "Inventario documental conocido" manual y desactualizado.
- `evidence`: §15 (Activity Log declarado como opcional) y `PROJECT_WORKING_RULES.md`
  §16 ("Inventario documental conocido") manual y desactualizado (declara
  `THREAD_ARCHITECTURE.md` 0.3.0 y omite THREAD), síntoma de que falta un índice
  derivable.
- `decision`: **pendiente**. Puede aplazarse respecto al resto de la 0.5.0.
