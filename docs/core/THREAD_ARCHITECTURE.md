# ClimaScope — Arquitectura de hilos de trabajo

**Versión:** 0.7.0  
**Estado:** Especificación operativa  
**Idioma:** español (España)  
**Repositorio:** `gineslm/climascope`  
**Rama raíz de conocimiento:** `knowledge`

## 1. Propósito

Este documento formaliza el modelo operativo de los hilos de trabajo de ClimaScope. Complementa `docs/core/PROJECT_WORKING_RULES.md` y `docs/core/PROJECT_AGENT_CONTEXT.md`; no los sustituye.

La unidad persistente de trabajo es el **THREAD de proyecto**, no la conversación de ChatGPT. GitHub es la fuente duradera de verdad. Una conversación es una instancia operativa de IA que se conecta a un THREAD.

La arquitectura distingue dos ciclos relacionados pero diferentes:

```text
KNOWLEDGE → consolidación del conocimiento y del estado estructural
SOFTWARE  → desarrollo, integración y publicación del software
```

## 2. Principios

1. Un THREAD es una entidad persistente de trabajo; no es un chat.
2. Una conversación es una instancia operativa mediante la cual un agente se conecta a un THREAD y opera sobre él.
3. Toda instancia debe tener una responsabilidad delimitada.
4. Una conversación no es fuente autoritativa del proyecto.
5. El conocimiento duradero debe sincronizarse con el repositorio.
6. El MANIFEST es la autoridad sobre la identidad y el estado operativo actual del THREAD.
7. Un HANDOFF **no es un documento de transición entre sesiones ni un mecanismo de reincorporación de agentes**. Es el registro persistente de eventos de entrada del THREAD: propuestas, revisiones y tareas pendientes que el THREAD receptor debe evaluar.
8. Un agente se incorpora a un THREAD resolviendo y leyendo su MANIFEST. Puede llegar al MANIFEST a partir de una referencia a un HANDOFF, pero el HANDOFF no sustituye al MANIFEST como mecanismo de incorporación.
9. Ningún THREAD modifica directamente el conocimiento cuya evolución corresponde a otro THREAD. Puede leerlo y puede registrar una propuesta en el HANDOFF del THREAD responsable.
10. Una propuesta registrada en un HANDOFF no constituye por sí misma una dependencia, una decisión ni un cambio del conocimiento vigente.
11. Los conflictos entre conversación y repositorio se hacen explícitos.
12. Una rama de trabajo no es autoritativa por el mero hecho de existir.
13. El conocimiento consolidado y la implementación del software son dimensiones distintas.
14. La nomenclatura prioriza nombres completos y legibles; no se introducen prefijos compactos mientras no exista necesidad demostrada.
15. Los identificadores Git que fijan un estado histórico deben expresar su función temporal y no presentarse como si fueran referencias dinámicas al estado actual.
16. Crear un THREAD es crear y consolidar su MANIFEST; un THREAD existe si y solo si existe su MANIFEST.
17. No existe un artefacto de «declaración» de THREAD independiente del MANIFEST: «declarar» es la operación de crear el MANIFEST.
18. El corpus de conocimiento del proyecto es común para lectura: un THREAD puede consultar cualquier documento necesario para razonar dentro de su responsabilidad. La autoridad de **edición** se restringe por responsabilidad, no por visibilidad.
19. Un THREAD custodia el **estado de un problema o línea de investigación/trabajo** y es responsable de la evolución del conocimiento dentro de ese alcance; no debe interpretarse como propietario exclusivo de todo conocimiento al que accede.

## 3. Modelo de ramas y raíz del proyecto

Git representa estados diferentes del proyecto:

```text
                         PROYECTO
                            │
              ┌─────────────┴─────────────┐
              │                           │
          KNOWLEDGE                    SOFTWARE
              │                           │
              ▼                           ▼
          `knowledge`                  `develop`
              │                           │
              │                           ▼
              │                         `main`
              │
              ├── reglas y contexto
              ├── arquitectura
              ├── THREADs / MANIFESTs
              ├── HANDOFFs
              ├── conocimiento validado
              └── estado estructural consolidado
```

### 3.1 `knowledge` es la raíz de conocimiento y bootstrap

`knowledge` es la **referencia inicial y estable para descubrir el estado consolidado de conocimiento y estructura del proyecto**.

Toda nueva instancia de conversación debe entrar conceptualmente por `knowledge` antes de resolver una responsabilidad o un THREAD. No debe empezar por `main` ni seleccionar arbitrariamente una rama de trabajo para reconstruir el estado global.

Como mínimo, desde `knowledge` deben poder descubrirse:

- `docs/core/PROJECT_AGENT_CONTEXT.md`;
- `docs/core/PROJECT_WORKING_RULES.md`;
- `docs/core/THREAD_ARCHITECTURE.md`;
- `docs/core/PROJECT_INDEX.md`;
- informes de proyecto vigentes;
- THREADs y sus MANIFESTs;
- HANDOFFs de los THREADs;
- conocimiento metodológico y decisiones consolidadas;
- documentos del corpus de conocimiento;
- referencias a las ramas/commits de trabajo cuando existan.

La rama `knowledge` no es una rama temporal ni una copia de trabajo. Es la línea donde se fija el estado autoritativo de conocimiento/estructura.

La arquitectura requiere mecanismos de descubrimiento suficientes para que un agente conectado a un THREAD pueda reconstruir el corpus relevante sin conocerlo de antemano. `PROJECT_INDEX.md` cubre actualmente el descubrimiento de THREADs; queda abierta (§19) la necesidad de un índice específico del corpus documental y de las autoridades de edición.

### 3.2 `develop`

`develop` representa la línea de integración del software.

Cuando una implementación dependa de conocimiento consolidado, el THREAD de software debe registrar el estado de `knowledge` utilizado como base:

```yaml
knowledge_basis:
  branch: knowledge
  commit: <sha>
```

En este caso `knowledge_basis.commit` es una **base histórica de la implementación** y no debe interpretarse como el estado actual de `knowledge` una vez que la rama haya avanzado.

No se establece que todo el contenido de `knowledge` deba fusionarse físicamente en `develop`. La implementación puede incorporar selectivamente la documentación técnica que necesite.

### 3.3 `main`

`main` representa el software estable/desplegable. No es la fuente global del conocimiento del proyecto.

Un cambio consolidado en `knowledge` no tiene que llegar a `main` si todavía no existe implementación, queda fuera del producto o sigue un ciclo independiente.

La documentación técnica necesaria para desarrollar, mantener, operar o utilizar el software puede permanecer en `develop` y/o `main`. No se adopta la regla `main = develop - docs`.

### 3.4 Ramas de trabajo

Las ramas `agent/*`, `feature/*` u otras ramas temporales representan trabajo en evolución.

Una rama de trabajo puede producir dos tipos de resultado:

```text
resultado de conocimiento → consolidación en `knowledge`
resultado de software     → integración en `develop` / `main`
```

Una rama de trabajo es una referencia de trabajo, no una fuente alternativa de verdad global.

## 4. Evento de consolidación

Un evento de consolidación ocurre cuando un cambio deja de ser exclusivamente trabajo de una conversación o rama temporal y pasa a formar parte del estado autoritativo del proyecto.

Son ejemplos:

- creación/modificación de documento autoritativo;
- decisión persistente adoptada;
- creación/actualización de MANIFEST;
- creación/actualización de HANDOFF;
- cierre de THREAD con estado persistente;
- actividad operativa significativa;
- conocimiento validado;
- modificación relevante de arquitectura.

Flujo:

```text
trabajo / análisis
      ↓
resultado persistente
      ↓
documentar / actualizar estado
      ↓
COMMIT
      ↓
consolidar en `knowledge`
```

No todo borrador o pensamiento requiere consolidación. El criterio es si modifica una fuente autoritativa o el estado persistente.

## 5. THREAD como entidad persistente

Un THREAD existe independientemente de que haya una conversación abierta. Su identidad se conserva mediante un MANIFEST.

Un THREAD existe **si y solo si** existe su MANIFEST en `knowledge`: crear un THREAD es crear y consolidar su MANIFEST. Ningún otro artefacto —una responsabilidad enunciada, un HANDOFF, una conversación o una entrada de índice— da de alta un THREAD.

Como mínimo:

```yaml
thread_id:
domain:
status:
owner:
created:
current_cycle:
responsibility:
origin:
```

El `thread_id` permanece estable durante la vida del THREAD. Si la responsabilidad deja de ser conceptualmente unitaria y necesita desacoplarse en nuevas responsabilidades, debe evaluarse el cierre/archivo del THREAD y el alta de nuevos THREADs, preservando la procedencia entre ellos.

### 5.1 Origen del THREAD

```yaml
origin:
  type: USER_DECLARED | THREAD_DERIVED | MIGRATED
  source_id:
```

`origin.type` representa el **origen de la responsabilidad**, no el mecanismo por el que se formalizó:

- `USER_DECLARED`: responsabilidad nueva identificada por el usuario.
- `THREAD_DERIVED`: responsabilidad nueva identificada durante el trabajo de otro THREAD existente.
- `MIGRATED`: importación de una conversación/responsabilidad externa —con su contexto y documentos— que se adopta como THREAD, extrayendo su responsabilidad y su corpus y revisando su compatibilidad con los THREAD preexistentes.

El origen es histórico y no cambia. `source_id` referencia la fuente del origen (la conversación, el THREAD de origen o la fuente importada, según el tipo).

Cuando un THREAD existente detecta una nueva área de responsabilidad, puede preparar el MANIFEST y el HANDOFF del futuro THREAD con la propuesta inicial que motivó su creación. También puede existir provisionalmente un HANDOFF dirigido a una responsabilidad aún no formalizada; esa existencia provisional **no da de alta el THREAD**. El THREAD sólo existe cuando su MANIFEST queda creado y consolidado.

## 6. Alta del THREAD

Dar de alta un THREAD es **crear y consolidar su MANIFEST**. No existe un artefacto de «declaración» independiente del MANIFEST: «declarar» un THREAD es precisamente la operación que crea su MANIFEST.

Regla de existencia (anti-limbo): un THREAD existe **si y solo si** existe su MANIFEST en `knowledge`. Si existe un HANDOFF provisional para una responsabilidad sin MANIFEST, debe tratarse como propuesta de alta, no como THREAD existente.

En el proceso normal, el HANDOFF persistente del THREAD se crea a la vez que el MANIFEST. Si el THREAD nace de una propuesta previa, el HANDOFF puede inicializarse con esa entrada.

El MANIFEST inicializa identidad, alcance, dependencias, origen, estado y autoridad documental (§7) antes de considerar completado cualquier trabajo técnico. El origen de la responsabilidad se registra en `origin.type` (§5.1).

## 7. MANIFEST

El MANIFEST es el **contrato persistente y fuente autoritativa del estado operativo actual del THREAD**.

Debe resolver, cuando proceda:

- identidad y responsabilidad;
- propietario/línea;
- estado y ciclo;
- origen;
- documentos cuya evolución está bajo responsabilidad directa del THREAD;
- documentos/dependencias que debe consultar;
- entregables y validación;
- HANDOFF asociado;
- cuestiones abiertas;
- referencias Git relevantes.

La lista de documentos del MANIFEST **no limita la lectura**. Un THREAD puede consultar cualquier parte del corpus necesaria para resolver su responsabilidad. Sí debe delimitar qué documentos puede modificar directamente en virtud de su responsabilidad y qué cambios debe proponer a otros THREADs mediante sus HANDOFFs.

### 7.1 Referencia de conocimiento del MANIFEST

El MANIFEST debe distinguir entre **el estado de conocimiento desde el que se dio de alta el THREAD** y **el estado vigente de `knowledge`**.

Al dar de alta un THREAD (crear su MANIFEST), registrar el commit de `knowledge` leído como base:

```yaml
repository:
  knowledge_branch: knowledge
  created_from_knowledge_commit: <sha>
  work_branch: <branch>
  work_commit: <sha>
```

**Definición canónica.** `created_from_knowledge_commit` es el commit de `knowledge` desde el que se **da de alta** el THREAD mediante la creación de su MANIFEST. Tiene la **misma semántica para los tres orígenes** (`USER_DECLARED`, `THREAD_DERIVED`, `MIGRATED`): siempre el commit de alta vía MANIFEST. Es una referencia histórica **inmutable**: no se actualiza cuando `knowledge` avanza.

No representa el **estado vigente** de `knowledge` (que se resuelve siempre leyendo la rama) ni la **prehistoria** de la responsabilidad. En un THREAD `MIGRATED`, la historia previa a la formalización se representa mediante `origin.source_id` y las referencias al corpus/documentación incorporados.

**Forma canónica única**: el campo plano `created_from_knowledge_commit`. Quedan retiradas las variantes para el mismo concepto:

- `knowledge_commit` sin calificador;
- la forma anidada `created_from_knowledge` con `branch`/`commit`.

Si un THREAD necesita fijar una base histórica para una implementación o dependencia reproducible de software, puede utilizar `knowledge_basis.commit` con esa función explícita; `knowledge_basis` no se emplea como base de alta de un THREAD.

Un MANIFEST nuevo debe aplicar esta distinción desde su primera versión.

Los campos se utilizan según el tipo de THREAD. Un THREAD exclusivamente documental puede no tener `work_branch`.

### 7.2 HANDOFF asociado

Cada THREAD dispone, como regla general, de **un único HANDOFF persistente**, asociado de forma estable a su identidad:

```yaml
handoff:
  handoff_id:
  path:
  status: ACTIVE
```

El HANDOFF no representa una sesión ni una transferencia entre agentes. Es el buzón/registro estructurado de entradas pendientes del THREAD (§13). Su historial se conserva dentro del propio registro mediante las entradas y sus cambios de estado, no mediante una sucesión conceptual de HANDOFFs de sesión.

Para conectar con un THREAD se consulta primero el MANIFEST. Después se lee su HANDOFF para conocer propuestas y revisiones pendientes.

## 8. Estados del THREAD

```text
PROPOSED
ACTIVE
BLOCKED
READY_FOR_HANDOFF
CLOSED
ARCHIVED
```

El estado debe reflejar el repositorio, no una impresión temporal de la conversación.

> `READY_FOR_HANDOFF` es nomenclatura heredada de versiones anteriores y debe revisarse en una evolución posterior, porque el HANDOFF ya no representa una transferencia de sesión. Se conserva provisionalmente para no mezclar en esta revisión una migración adicional del ciclo de estados.

## 9. THREAD BOOTSTRAP

> **Fuente canónica del modelo de bootstrap.** Esta sección define el modelo: resolución de `knowledge`, conexión mediante MANIFEST, alta de responsabilidad nueva y reincorporación. La secuencia operativa reutilizable vive en `docs/core/THREAD_CONTEXT_BOOTSTRAP.md`, que aplica este modelo sin redefinirlo.

El THREAD BOOTSTRAP es el protocolo universal de incorporación de una nueva instancia de conversación.

### 9.1 Regla raíz

**Toda ruta de entrada debe comenzar conceptualmente en `knowledge`.**

El orden general es:

```text
NUEVA CONVERSACIÓN
        ↓
    `knowledge`
        ↓
reglas + contexto + arquitectura
        ↓
resolver THREAD objetivo
        ↓
MANIFEST
        ↓
HANDOFF + corpus relevante
        ↓
work_branch, si procede
```

La rama de trabajo nunca precede a la resolución del estado consolidado salvo que una comprobación explícita de integridad indique que `knowledge` está inaccesible.

### 9.2 Referencia de entrada mediante HANDOFF

Si el usuario indica:

> **«Parte del handoff `<id>`.»**

la frase se interpreta como una **referencia de descubrimiento**, no como un mecanismo alternativo de incorporación. El agente debe:

1. entrar en `knowledge`;
2. localizar el HANDOFF por identificador;
3. identificar el THREAD o responsabilidad receptora;
4. localizar su MANIFEST;
5. si el MANIFEST existe, incorporarse al THREAD a través de él;
6. si el MANIFEST no existe y el HANDOFF es una propuesta provisional de nueva responsabilidad, dar de alta el THREAD creando su MANIFEST antes de operar como ese THREAD;
7. resolver desde el MANIFEST responsabilidad, autoridad documental, dependencias y referencias Git;
8. leer el HANDOFF como registro de entradas pendientes;
9. resolver el corpus documental relevante desde `knowledge`;
10. informar del diagnóstico y comenzar el trabajo dentro de la responsabilidad.

El HANDOFF puede ayudar a **encontrar** la responsabilidad, pero nunca sustituye al MANIFEST como contrato de incorporación.

### 9.3 Entrada directa por THREAD

Si el usuario indica:

> **«Conecta con el hilo `<thread_id>`.»**

el agente debe:

1. entrar en `knowledge`;
2. localizar el MANIFEST;
3. verificar identidad y estado;
4. leer el HANDOFF asociado;
5. resolver dependencias y corpus relevante;
6. resolver `work_branch`/`work_commit` desde el MANIFEST;
7. informar del diagnóstico;
8. continuar dentro de la responsabilidad vigente.

La conexión directa no crea un nuevo THREAD ni reinicia el ciclo. Si no existe MANIFEST para `<thread_id>`, no hay THREAD que conectar: debe formalizarse o declararse el estado como inconsistente (§6).

### 9.4 Entrada desde responsabilidad nueva

Si una conversación nueva declara una responsabilidad y no existe un THREAD compatible:

1. entrar en `knowledge`;
2. comprobar si existe THREAD compatible;
3. si existe, conectar con él mediante su MANIFEST;
4. si no existe, crear su MANIFEST (alta del THREAD) con `origin.type: USER_DECLARED`;
5. crear su HANDOFF persistente, normalmente vacío salvo que ya existan propuestas de entrada;
6. establecer en el MANIFEST identidad, alcance, autoridad documental, dependencias y estado;
7. registrar `created_from_knowledge_commit` (§7.1);
8. consolidar MANIFEST y HANDOFF en `knowledge` cuando constituyan estado persistente;
9. comenzar el trabajo.

El usuario no necesita conocer la estructura interna del MANIFEST.

### 9.5 Reincorporación de conversación existente

Ante:

> **«Reincorpórate al contexto del proyecto.»**

se debe entrar en `knowledge`, reconstruir la responsabilidad y comparar la conversación con el estado consolidado. Las discrepancias se clasifican como `NUEVO`, `OBSOLETO`, `CONFLICTO`, `DUPLICADO` o `FUERA DE ALCANCE`.

## 10. Crear, conectar y proponer

### Crear THREAD

Da de alta una entidad nueva **creando y consolidando su MANIFEST** (§6). El MANIFEST fija identidad, alcance, dependencias, estado, `origin.type` (§5.1), autoridad documental y `created_from_knowledge_commit` (§7.1). En el proceso normal se crea también su HANDOFF persistente.

### Conectar con THREAD

Localiza el MANIFEST de un THREAD **existente**, resuelve su estado y asocia una nueva conversación/agente a esa responsabilidad. Después consulta su HANDOFF y el corpus documental necesario. No crea ni modifica la entidad.

### Proponer revisión a otro THREAD

Cuando un THREAD descubre una necesidad que afecta a conocimiento cuya evolución corresponde a otro THREAD:

1. no modifica directamente esos documentos;
2. identifica el THREAD responsable mediante el índice/los MANIFESTs;
3. registra una entrada en el HANDOFF del THREAD receptor;
4. adjunta contexto, evidencia y referencias suficientes;
5. continúa dentro de su propia responsabilidad salvo que la propuesta sea un bloqueo explícito.

El THREAD receptor es el único que evalúa la propuesta y modifica su estado (`accepted`, `rejected`, `deferred`, `superseded` u otro estado canónico futuro), registra la decisión y, si procede, actualiza el conocimiento bajo su responsabilidad.

## 11. Contrato de responsabilidad

Toda conversación sustantiva conectada a un THREAD debe poder responder:

```text
THREAD:
Responsabilidad:
Propietario / línea:
Estado / ciclo:
Dentro de alcance:
Fuera de alcance:
Documentos que puede modificar directamente:
Corpus/dependencias principales que debe consultar:
Código / datos principales:
Entregables:
Validación:
Handoff asociado:
Base de conocimiento:
Rama/commit de trabajo:
```

## 12. Dependencias, propuestas y versiones

Una **propuesta** en un HANDOFF no es por sí misma una dependencia. Las dependencias representan conocimiento o artefactos cuya versión condiciona efectivamente el trabajo del THREAD.

Las dependencias relevantes deben poder fijarse a una versión:

```yaml
dependency:
  document: docs/threads/station-location-evidence/MODEL.md
  version: 0.1.1
  status: current
```

Si una dependencia cambia, el THREAD debe poder detectar posible obsolescencia antes de continuar.

Una propuesta puede convertirse en dependencia sólo como consecuencia de una decisión explícita del THREAD receptor o de una modificación consolidada del conocimiento que afecte al THREAD emisor.

## 13. HANDOFF

### 13.1 Definición canónica

El **HANDOFF no es un documento de transición de sesiones**, no resume una conversación para que otra la continúe y no es el mecanismo por el que un agente se incorpora al THREAD.

El HANDOFF es el **registro persistente de eventos de entrada** de una responsabilidad: una cola deliberativa de propuestas, revisiones, necesidades y tareas que otros THREADs —o el propio ecosistema— remiten al THREAD receptor para que éste las evalúe.

Como regla general existe **un único HANDOFF por THREAD**. Pertenece a la responsabilidad del THREAD y persiste aunque cambien los agentes o no exista ninguna conversación activa.

### 13.2 Autoría y soberanía

El HANDOFF distingue dos autoridades:

- **Entrada/propuesta**: cualquier THREAD puede registrar una propuesta dirigida al receptor, siempre con origen y evidencia suficientes.
- **Estado/resolución**: sólo el THREAD propietario del HANDOFF evalúa la entrada, cambia su estado, registra la decisión y modifica, si procede, el conocimiento dentro de su responsabilidad.

Esta separación preserva la soberanía de responsabilidad: otros THREADs pueden escribir **propuestas** en el HANDOFF, pero no pueden escribir la **resolución** ni modificar directamente el conocimiento del receptor.

### 13.3 Estructura mínima de una entrada

Cada entrada es conceptualmente cercana a un **Architecture Decision Record (ADR)**: conserva el contexto de una decisión potencial y su resolución, aunque no todo evento tenga naturaleza estrictamente arquitectónica.

Formato mínimo provisional:

```yaml
entry_id:
origin_thread:
created:
type: proposal | review | need | task
summary:
context:
evidence:
target_scope:

resolution:
  status: proposed | accepted | rejected | deferred | superseded
  decided_by:
  decided_at:
  rationale:
  resulting_changes:
```

La estructura puede representarse físicamente como dos columnas o dos zonas lógicas:

| Entrada / propuesta | Estado / resolución del THREAD receptor |
|---|---|
| Escribible por el THREAD emisor; conserva origen, necesidad, contexto y evidencia. | Escribible por el THREAD propietario; conserva estado, deliberación, decisión y cambios resultantes. |

La implementación física definitiva del formato queda abierta; la separación de autoridad entre ambas partes es normativa.

### 13.4 Ciclo de una entrada

```text
propuesta registrada
        ↓
evaluación por THREAD receptor
        ├── accepted   → actualiza conocimiento / tareas si procede
        ├── rejected   → conserva razón
        ├── deferred   → permanece pendiente
        └── superseded → referencia a la entrada que la sustituye
```

La existencia de entradas no resueltas es parte del estado operativo del THREAD y debe revisarse antes de cerrar, archivar o redefinir su responsabilidad.

### 13.5 Creación del HANDOFF

En el flujo normal, el HANDOFF se crea junto con el MANIFEST del THREAD. Si otro THREAD descubre una responsabilidad nueva, puede preparar una propuesta de alta y un HANDOFF inicial con las entradas que motivaron esa nueva responsabilidad. Un HANDOFF provisional sin MANIFEST **no constituye todavía un THREAD** (§5-6).

## 14. Propuestas y decisiones

```text
propuesta externa
      ↓
HANDOFF del receptor
      ↓
evaluación soberana del THREAD
      ↓
accepted / rejected / deferred / superseded
      ↓ (si accepted)
documentación → implementación/validación → consolidación
```

El chat no convierte por sí mismo una propuesta en conocimiento autoritativo. El HANDOFF tampoco: sólo registra la propuesta y su resolución. El conocimiento vigente se modifica en sus documentos autoritativos cuando el THREAD responsable acepta y consolida el cambio.

## 15. Registro e índice del proyecto

### 15.1 Registro (Activity Log)

Cada THREAD puede mantener un **registro** de su actividad operativa significativa: eventos, decisiones y cambios de estado, con su origen y evidencia. No debe ser una copia íntegra de conversaciones.

El Activity Log no debe confundirse con el HANDOFF: el HANDOFF organiza **inputs deliberables** dirigidos al THREAD; el Activity Log conserva, cuando exista, la historia operativa general del THREAD.

El registro es historial: conserva lo ocurrido, pero **no es autoritativo sobre el estado actual** (esa autoridad es del MANIFEST y de los documentos de conocimiento vigentes). Cuando una entrada del registro modifica estado autoritativo, debe consolidarse en `knowledge` junto con los artefactos afectados.

### 15.2 Índice del proyecto

El **índice del proyecto** es un artefacto de **descubrimiento**: permite localizar qué THREAD existen y dónde están sus artefactos.

Es **derivado y no autoritativo**: debe poder reconstruirse a partir del conjunto de MANIFEST consolidados en `knowledge`. No es una segunda fuente de verdad; si el índice y un MANIFEST discrepan, **prevalece el MANIFEST**. El índice no da de alta THREAD: refleja los que ya existen (§6).

La arquitectura deja abierta la extensión del índice —o la creación de un índice documental separado— para descubrir el corpus de conocimiento, sus documentos, relaciones y autoridades de edición (§19).

## 16. Autoridad documental

| Información | Fuente principal |
|---|---|
| Reglas permanentes | `docs/core/PROJECT_WORKING_RULES.md` en `knowledge` |
| Integración agente ↔ repositorio | `docs/core/PROJECT_AGENT_CONTEXT.md` en `knowledge` |
| Arquitectura de hilos | `docs/core/THREAD_ARCHITECTURE.md` en `knowledge` |
| Estado/metodología validada | documentos de conocimiento vigentes en `knowledge` |
| Identidad, estado y alta de THREAD | MANIFEST en `knowledge` |
| Entradas/propuestas dirigidas al THREAD y sus resoluciones | HANDOFF del THREAD en `knowledge` |
| Historial de actividad general del THREAD | Registro (Activity Log), cuando exista |
| Descubrimiento de THREAD | Índice del proyecto (derivado, no autoritativo) |
| Implementación en curso | rama/commit de trabajo |
| Software integrado | `develop` / `main` |
| Datos fuente | fuente + procedencia |
| Conversación/agente | contexto operativo no autoritativo |

Si fuentes comparables discrepan, se expone el conflicto y se determina cuál prevalece.

## 17. Cierre

Antes de cerrar un THREAD sustantivo:

1. revisar y resolver o clasificar las entradas abiertas de su HANDOFF;
2. validar/tests cuando proceda;
3. documentar resultados y decisiones;
4. actualizar versiones y MANIFEST;
5. actualizar el HANDOFF con el estado de las propuestas tratadas;
6. hacer commit en la rama de trabajo cuando exista;
7. consolidar en `knowledge` los cambios autoritativos de conocimiento/estructura;
8. registrar los SHAs relevantes;
9. indicar incertidumbres restantes.

Cerrar un THREAD no elimina su conocimiento ni el historial de su HANDOFF.

## 18. Disposición física de `docs/`

`docs/` se organiza actualmente en dos ramas físicas según la naturaleza de la responsabilidad:

```text
docs/
├── core/              → sistema: hilos meta + documentos de sistema
│   └── threads/       → MANIFEST/HANDOFF/IMPROVEMENTS de hilos meta
└── threads/           → hilos de dominio y artefactos asociados
```

**Criterio meta vs. dominio.** Un THREAD es **meta** si su responsabilidad es el propio sistema —arquitectura, metodología, reglas— y vive en `docs/core/threads/<thread>/`; es de **dominio** si trabaja sobre el producto de ClimaScope —datos, modelo científico, UX— y actualmente vive en `docs/threads/<thread>/`.

Dentro de cada carpeta de THREAD, los artefactos operativos específicos del THREAD se nombran por **rol** (`MANIFEST.md`, `HANDOFF.md`, `IMPROVEMENTS.md`, etc.).

Esta disposición física **no resuelve todavía la arquitectura final del corpus de conocimiento**. En particular, no debe inferirse de la ubicación actual que todo documento de conocimiento sea propiedad exclusiva del THREAD cuya carpeta lo contiene. La cuestión queda explicitada en §19.

## 19. Cuestión abierta — capa documental del conocimiento

### 19.1 Hechos ya fijados

La arquitectura distingue entre **acceso al corpus** y **autoridad de edición**:

- todos los documentos son potencialmente transversales para lectura;
- cualquier THREAD puede consultar cualquier documento necesario para razonar dentro de su responsabilidad;
- un THREAD sólo modifica directamente conocimiento cuya evolución corresponde a su responsabilidad;
- si detecta una necesidad fuera de ese ámbito, registra una propuesta en el HANDOFF del THREAD responsable;
- el THREAD custodia el estado de un problema/línea de trabajo y es responsable de la evolución del conocimiento en ese alcance.

Ejemplo: un THREAD puede consultar un documento general de miembros del equipo para planificar una tarea. Si el perfil necesario existe, utiliza esa información dentro de su trabajo. Si detecta que falta un perfil cuya gestión pertenece a otro THREAD, no modifica el documento de personal: registra una propuesta justificada en el HANDOFF del THREAD responsable.

### 19.2 Decisión todavía abierta

No se ha fijado aún la relación física y de gobernanza entre los documentos del corpus y los THREADs. Se mantienen dos modelos de investigación:

**Modelo A — corpus común con autoridad de edición federada por THREAD**

Los documentos forman un corpus global legible por todos los THREADs, pero cada documento o ámbito documental tiene una responsabilidad de evolución claramente asignada. La federación afecta a la **escritura**, no al acceso.

**Modelo B — corpus documental independiente con gobernanza desacoplada de los THREADs**

Los documentos pertenecen a un dominio de conocimiento común y los THREADs reciben permisos/roles de intervención sobre ellos. Este modelo podría facilitar documentos con gobernanza compartida, pero introduce una capa adicional de autoridad que todavía no ha demostrado ser necesaria.

### 19.3 Preguntas pendientes

- ¿Debe cada documento tener un THREAD responsable único de su evolución o pueden existir responsabilidades compartidas?
- ¿Qué ocurre cuando una responsabilidad se divide y un THREAD se archiva: cómo se redistribuye la autoridad sobre documentos ya existentes?
- ¿Debe existir un `DOCUMENT_INDEX` separado o basta con ampliar `PROJECT_INDEX` para describir el corpus y su autoridad de edición?
- ¿La autoridad debe declararse por documento completo, por sección/entidad conceptual o por otro límite?
- ¿Puede un documento ser producto histórico de un THREAD cerrado pero quedar bajo responsabilidad de un THREAD posterior sin moverlo físicamente?

Estas preguntas deben contrastarse con el estado del arte antes de introducir nuevas entidades o capas de gobernanza.
