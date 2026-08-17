# ClimaScope — Arquitectura de hilos de trabajo

**Versión:** 0.5.0  
**Estado:** Especificación operativa  
**Idioma:** español (España)  
**Repositorio:** `gineslm/climascope`  
**Rama raíz de conocimiento:** `knowledge`

## 1. Propósito

Este documento formaliza el modelo operativo de los hilos de trabajo de ClimaScope. Complementa `docs/PROJECT_WORKING_RULES.md` y `docs/CHATGPT_PROJECT_CONTEXT.md`; no los sustituye.

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
6. El MANIFEST es la autoridad sobre el estado actual del THREAD.
7. Un HANDOFF transmite responsabilidad/contexto; no sustituye al MANIFEST una vez creado el receptor.
8. Los conflictos entre conversación y repositorio se hacen explícitos.
9. Una rama de trabajo no es autoritativa por el mero hecho de existir.
10. El conocimiento consolidado y la implementación del software son dimensiones distintas.
11. La nomenclatura prioriza nombres completos y legibles; no se introducen prefijos compactos mientras no exista necesidad demostrada.
12. Los identificadores Git que fijan un estado histórico deben expresar su función temporal y no presentarse como si fueran referencias dinámicas al estado actual.
13. Crear un THREAD es crear y consolidar su MANIFEST; un THREAD existe si y solo si existe su MANIFEST.
14. No existe un artefacto de «declaración» de THREAD independiente del MANIFEST: «declarar» es la operación de crear el MANIFEST.

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

Toda nueva instancia de conversación debe entrar conceptualmente por `knowledge` antes de resolver una responsabilidad, un HANDOFF o un THREAD. No debe empezar por `main` ni seleccionar arbitrariamente una rama de trabajo para reconstruir el estado global.

Como mínimo, desde `knowledge` deben poder descubrirse:

- `docs/CHATGPT_PROJECT_CONTEXT.md`;
- `docs/PROJECT_WORKING_RULES.md`;
- `docs/THREAD_ARCHITECTURE.md`;
- informes de proyecto vigentes;
- THREADs y sus MANIFESTs;
- HANDOFFs vigentes e históricos;
- conocimiento metodológico y decisiones consolidadas;
- referencias a las ramas/commits de trabajo cuando existan.

La rama `knowledge` no es una rama temporal ni una copia de trabajo. Es la línea donde se fija el estado autoritativo de conocimiento/estructura.

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

La rama de trabajo indicada por un HANDOFF es una **referencia de trabajo**, no una fuente alternativa de verdad global.

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

El `thread_id` permanece estable durante la vida del THREAD. Los ciclos posteriores no reescriben retrospectivamente los anteriores.

### 5.1 Origen del THREAD

```yaml
origin:
  type: USER_DECLARED | THREAD_DERIVED | MIGRATED
  source_id:
```

`origin.type` representa el **origen de la responsabilidad**, no el mecanismo por el que llegó ni el momento de formalización:

- `USER_DECLARED`: responsabilidad nueva identificada por el usuario desde una conversación nueva.
- `THREAD_DERIVED`: responsabilidad nacida del trabajo de otro THREAD existente. Incluye el caso en que la responsabilidad se recibe por HANDOFF: el HANDOFF es el vehículo de transferencia, no el origen.
- `MIGRATED`: importación de una conversación/responsabilidad externa —con su contexto y documentos— que se adopta como THREAD, extrayendo su responsabilidad y su corpus y revisando su compatibilidad con los THREAD preexistentes.

El origen es histórico y no cambia por posteriores transferencias. `source_id` referencia la fuente del origen (la conversación, el THREAD de origen o la fuente importada, según el tipo).

## 6. Alta del THREAD

Dar de alta un THREAD es **crear y consolidar su MANIFEST**. No existe un artefacto de «declaración» independiente del MANIFEST: «declarar» un THREAD es precisamente la operación que crea su MANIFEST.

Regla de existencia (anti-limbo): un THREAD existe **si y solo si** existe su MANIFEST en `knowledge`. No debe operarse ni transferirse un THREAD cuyo MANIFEST no exista; si se intenta conectar con un THREAD sin MANIFEST, debe formalizarse (crear el MANIFEST) o declararse el estado como inconsistente, en lugar de operarlo como si existiera.

El MANIFEST inicializa identidad, alcance, dependencias, origen y estado (§7) antes de considerar completado cualquier trabajo técnico. El origen de la responsabilidad se registra en `origin.type` (§5.1).

## 7. MANIFEST

El MANIFEST es el **contrato persistente y fuente autoritativa del estado operativo actual del THREAD**.

Debe resolver, cuando proceda:

- identidad y responsabilidad;
- propietario/línea;
- estado y ciclo;
- origen;
- documentos autoritativos;
- dependencias;
- entregables y validación;
- HANDOFF vigente e histórico;
- cuestiones abiertas;
- referencias Git relevantes.

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

**Definición canónica.** `created_from_knowledge_commit` es el commit de `knowledge` desde el que se **da de alta** el THREAD mediante la creación de su MANIFEST. Tiene la **misma semántica para los tres orígenes** (`USER_DECLARED`, `THREAD_DERIVED`, `MIGRATED`): siempre el commit de alta vía MANIFEST. Es una referencia histórica **inmutable**: no se actualiza cuando `knowledge` avanza ni por transferencias posteriores, y no depende del concepto de «declaración».

No representa el **estado vigente** de `knowledge` (que se resuelve siempre leyendo la rama) ni la **prehistoria** de la responsabilidad. En un THREAD `MIGRATED`, la historia previa a la formalización se representa mediante `origin.source_id` y las referencias al corpus/documentación incorporados, no mediante este campo.

**Forma canónica única**: el campo plano `created_from_knowledge_commit`. Quedan retiradas las variantes para el mismo concepto:

- `knowledge_commit` sin calificador (induce a leer un SHA histórico como referencia dinámica);
- la forma anidada `created_from_knowledge` con `branch`/`commit`.

Si un THREAD necesita fijar una base histórica para una implementación o dependencia reproducible de software, puede utilizar `knowledge_basis.commit` con esa función explícita; `knowledge_basis` no se emplea como base de alta de un THREAD.

Un MANIFEST nuevo debe aplicar esta distinción desde su primera versión; no debe copiar un campo ambiguo de un MANIFEST anterior.

Los campos se utilizan según el tipo de THREAD. Un THREAD exclusivamente documental puede no tener `work_branch`.

### 7.2 HANDOFF actual e histórico

```yaml
current_handoff:
  handoff_id:
  version:
  status: ACTIVE

handoff_history:
  - handoff_id:
    version:
    role: CREATION | TRANSFER | UPDATE
    status: SUPERSEDED | CLOSED | ACTIVE
```

Para conectar con un THREAD se consulta primero el MANIFEST. Nunca se selecciona un HANDOFF por ser el primero o el más antiguo encontrado.

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

## 9. THREAD BOOTSTRAP

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
resolver entrada del usuario
        ↓
THREAD / MANIFEST
        ↓
estado vigente
        ↓
work_branch, si procede
```

La rama de trabajo nunca precede a la resolución del estado consolidado salvo que una comprobación explícita de integridad indique que `knowledge` está inaccesible.

### 9.2 Entrada por HANDOFF

Si el usuario indica:

> **«Parte del handoff `<id>`.»**

el agente debe:

1. entrar en `knowledge`;
2. localizar el HANDOFF por identificador;
3. identificar el THREAD receptor;
4. localizar su MANIFEST;
5. comprobar si el THREAD ya está inicializado;
6. si no existe, dar de alta el THREAD creando su MANIFEST a partir del contexto transferido por el HANDOFF;
7. registrar `origin.type` según el origen de la responsabilidad (normalmente `THREAD_DERIVED` cuando procede de otro THREAD) y `source_id`; el HANDOFF es el vehículo, no el origen;
8. resolver documentos y dependencias desde `knowledge`;
9. validar compatibilidad del HANDOFF con el estado consolidado;
10. resolver desde el MANIFEST la rama/commit de trabajo;
11. pasar a `ACTIVE` cuando la inicialización sea válida;
12. informar del diagnóstico y comenzar el trabajo.

El alta del THREAD (crear su MANIFEST) es la primera responsabilidad operativa cuando el HANDOFF transfiere hacia un receptor inexistente.

### 9.3 Entrada directa por THREAD

Si el usuario indica:

> **«Conecta con el hilo `<thread_id>`.»**

el agente debe:

1. entrar en `knowledge`;
2. localizar el MANIFEST;
3. verificar identidad y estado;
4. leer `current_handoff`, si existe;
5. resolver dependencias vigentes;
6. resolver `work_branch`/`work_commit` desde el MANIFEST;
7. informar del diagnóstico;
8. continuar dentro de la responsabilidad vigente.

La conexión directa no crea un nuevo THREAD ni reinicia el ciclo. Si no existe MANIFEST para `<thread_id>`, no hay THREAD que conectar: debe formalizarse (crear su MANIFEST) o declararse el estado como inconsistente (§6).

### 9.4 Entrada desde responsabilidad nueva

Si una conversación nueva declara una responsabilidad sin HANDOFF:

1. entrar en `knowledge`;
2. comprobar si existe THREAD compatible;
3. si existe, conectar con él;
4. si no existe, crear su MANIFEST (alta del THREAD) con `origin.type: USER_DECLARED`;
5. establecer en el MANIFEST identidad, alcance, dependencias y estado;
6. registrar `created_from_knowledge_commit` (§7.1);
7. consolidar el MANIFEST en `knowledge` cuando constituya estado persistente;
8. comenzar el trabajo.

El usuario no necesita conocer la estructura interna del MANIFEST.

### 9.5 Reincorporación de conversación existente

Ante:

> **«Reincorpórate al contexto del proyecto.»**

se debe entrar en `knowledge`, reconstruir la responsabilidad y comparar la conversación con el estado consolidado. Las discrepancias se clasifican como `NUEVO`, `OBSOLETO`, `CONFLICTO`, `DUPLICADO` o `FUERA DE ALCANCE`.

## 10. Crear, conectar y transferir

### Crear THREAD

Da de alta una entidad nueva **creando y consolidando su MANIFEST** (§6). Es el único acto que da de alta un THREAD; no presupone ni requiere un artefacto de declaración. El MANIFEST fija identidad, alcance, dependencias, estado, `origin.type` (§5.1) y `created_from_knowledge_commit` (§7.1).

### Conectar con THREAD

Localiza el MANIFEST de un THREAD **existente**, resuelve su estado y su HANDOFF vigente, y asocia una nueva conversación/agente a esa responsabilidad. No crea ni modifica la entidad. Si el THREAD no tiene MANIFEST, no puede conectarse: debe formalizarse (crear su MANIFEST) o declararse el estado como inconsistente (§6).

### Transferir responsabilidad

Transfiere el estado operativo de un THREAD mediante HANDOFF. El HANDOFF **no da de alta ni declara** THREADs: si el receptor no existe, primero se le da de alta creando su MANIFEST (§6) y después se transfiere; si existe, se actualiza su estado.

Son operaciones distintas: **crear** da de alta la entidad; **conectar** engancha una conversación/agente a una entidad existente; **transferir** mueve estado operativo entre agentes.

## 11. Contrato de responsabilidad

Toda conversación sustantiva debe poder responder:

```text
THREAD:
Responsabilidad:
Propietario / línea:
Estado / ciclo:
Dentro de alcance:
Fuera de alcance:
Documentos principales:
Código / datos principales:
Entregables:
Validación:
Dependencias:
Handoff actual:
Base de conocimiento:
Rama/commit de trabajo:
```

## 12. Dependencias y versiones

Las dependencias relevantes deben poder fijarse a una versión:

```yaml
dependency:
  document: docs/THREAD_STATION_LOCATION_EVIDENCE_MODEL.md
  version: 0.1.1
  status: current
```

Si una dependencia cambia, el THREAD debe poder detectar posible obsolescencia antes de continuar.

## 13. HANDOFF

Un HANDOFF es un artefacto de transferencia de estado operativo de un THREAD existente; no da de alta ni declara THREADs. Debe incluir, cuando proceda:

- identificador y versión;
- emisor y receptor;
- objetivo y estado;
- decisiones y restricciones;
- documentos/versiones;
- código/datos afectados;
- validación;
- cuestiones abiertas;
- trabajo fuera de alcance;
- commit/SHA;
- referencia al estado de `knowledge` cuando sea necesaria para reproducibilidad.

La rama de trabajo indicada en un HANDOFF identifica dónde está el trabajo asociado. **No convierte esa rama en fuente de verdad global.**

Una vez creado el receptor, el MANIFEST determina el estado vigente.

## 14. Propuestas y decisiones

```text
propuesta → discusión → decisión → documentación → implementación/validación
```

El chat no convierte por sí mismo una propuesta en conocimiento autoritativo.

## 15. Registro e índice del proyecto

### 15.1 Registro (Activity Log)

Cada THREAD puede mantener un **registro** de su actividad operativa significativa: eventos, decisiones y cambios de estado, con su origen y evidencia. No debe ser una copia íntegra de conversaciones.

El registro es historial: conserva lo ocurrido, pero **no es autoritativo sobre el estado actual** (esa autoridad es del MANIFEST). Cuando una entrada del registro modifica estado autoritativo, debe consolidarse en `knowledge` junto con los artefactos afectados.

### 15.2 Índice del proyecto

El **índice del proyecto** es un artefacto de **descubrimiento**: permite localizar qué THREAD existen y dónde están sus artefactos.

Es **derivado y no autoritativo**: debe poder reconstruirse a partir del conjunto de MANIFEST consolidados en `knowledge`. No es una segunda fuente de verdad; si el índice y un MANIFEST discrepan, **prevalece el MANIFEST**. El índice no da de alta THREAD: refleja los que ya existen (§6).

## 16. Autoridad documental

| Información | Fuente principal |
|---|---|
| Reglas permanentes | `PROJECT_WORKING_RULES.md` en `knowledge` |
| Integración ChatGPT ↔ proyecto | `CHATGPT_PROJECT_CONTEXT.md` en `knowledge` |
| Arquitectura de hilos | `THREAD_ARCHITECTURE.md` en `knowledge` |
| Estado/metodología validada | documentos de conocimiento vigentes en `knowledge` |
| Identidad, estado y alta de THREAD | MANIFEST en `knowledge` |
| Transferencia de estado operativo | HANDOFF en `knowledge` |
| Historial de actividad del THREAD | Registro (Activity Log) en `knowledge` |
| Descubrimiento de THREAD | Índice del proyecto (derivado, no autoritativo) |
| Implementación en curso | rama/commit de trabajo |
| Software integrado | `develop` / `main` |
| Datos fuente | fuente + procedencia |
| Conversación/agente | contexto operativo no autoritativo |

Si fuentes comparables discrepan, se expone el conflicto y se determina cuál prevalece.

## 17. Cierre

Antes de cerrar un THREAD sustantivo:

1. validar/tests cuando proceda;
2. documentar resultados y decisiones;
3. actualizar versiones y MANIFEST;
4. crear/actualizar HANDOFF si procede;
5. hacer commit en la rama de trabajo;
6. consolidar en `knowledge` los cambios autoritativos de conocimiento/estructura;
7. registrar los SHAs relevantes;
8. indicar incertidumbres restantes.

Cerrar un THREAD no elimina su conocimiento.