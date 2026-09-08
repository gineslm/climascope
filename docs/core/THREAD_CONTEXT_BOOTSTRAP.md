# ClimaScope — Bootstrap de contexto de nuevos hilos

**Versión del documento:** 1.5.0  
**Creado:** 2026-08-15  
**Repositorio:** `gineslm/climascope`  
**Rama raíz de conocimiento:** `knowledge`  
**Propósito:** bloque reutilizable de contexto/instrucciones para abrir una nueva conversación de ClimaScope.

## 1. Propósito

Este documento es el bootstrap estándar para una nueva conversación que trabaje en ClimaScope.

> **Fuente canónica del bloque operativo de bootstrap.** El modelo subyacente es `docs/core/THREAD_ARCHITECTURE.md` §9; este documento proporciona la secuencia operativa reutilizable y no lo redefine.

Su propósito es hacer que cada conversación:

- sea independiente del histórico de chats anteriores;
- se conecte al repositorio central;
- conozca el método y la documentación vigente del proyecto;
- se incorpore a un THREAD mediante su MANIFEST cuando exista;
- quede explícitamente acotada a una responsabilidad;
- no absorba silenciosamente responsabilidades de otras líneas;
- consulte el HANDOFF del THREAD como registro de entradas pendientes, no como memoria de sesión.

El repositorio es la fuente de verdad. La conversación es una sesión de trabajo, no la memoria permanente del proyecto.

## 2. Bootstrap obligatorio

Cuando este documento forme parte del contexto del proyecto, la conversación debe seguir esta secuencia antes de realizar trabajo sustantivo:

> **Bootstrap de proyecto ClimaScope**
>
> Trabaja contra el repositorio central de GitHub `gineslm/climascope`.
>
> **Primero entra conceptualmente en la rama `knowledge` como raíz de conocimiento y estructura consolidada.** Después lee `docs/core/PROJECT_WORKING_RULES.md`, `docs/core/THREAD_ARCHITECTURE.md` y el contexto de proyecto vigente. Resuelve el THREAD objetivo y su MANIFEST. Una vez incorporado al THREAD, consulta su HANDOFF como registro de propuestas/revisiones pendientes y el corpus documental relevante.
>
> GitHub es el registro autoritativo del proyecto. No asumas que una información existe porque apareciera en otra conversación. Si falta un documento referenciado en el repositorio, informa de ello y solicítalo en lugar de inventarlo.
>
> Antes de realizar cambios sustantivos, informa de las versiones documentales relevantes, el estado consolidado y la responsabilidad que se ha resuelto.

### Regla de autoridad

Una rama de trabajo indicada por un MANIFEST es una referencia al trabajo operativo, no una fuente alternativa de verdad global. Las reglas, arquitectura, identidad de THREAD, MANIFEST, HANDOFF y decisiones consolidadas deben resolverse desde `knowledge`.

**El HANDOFF no es un documento de transición entre sesiones ni el mecanismo de incorporación de agentes.** La incorporación se realiza mediante el MANIFEST; el HANDOFF es el registro persistente de entradas pendientes del THREAD.

## 3. Alta de THREAD (crear su MANIFEST y HANDOFF)

Dar de alta un THREAD es **crear y consolidar su MANIFEST**. Un THREAD existe si y solo si existe su MANIFEST.

En el flujo normal se crea también, en la misma inicialización, su **HANDOFF persistente**. El HANDOFF puede estar vacío o contener las propuestas que motivaron la nueva responsabilidad.

Cuando una conversación nueva identifica una responsabilidad y no existe un THREAD compatible:

1. resolver primero el estado de `knowledge`;
2. crear su MANIFEST (el alta) con `origin.type: USER_DECLARED`, salvo que el origen corresponda a otra categoría canónica;
3. crear su HANDOFF persistente;
4. registrar en el MANIFEST el commit de `knowledge` desde el que se da de alta el THREAD:

```yaml
repository:
  knowledge_branch: knowledge
  created_from_knowledge_commit: <sha>
```

`created_from_knowledge_commit` es histórico e inmutable y no se actualiza cuando `knowledge` avanza.

Un HANDOFF provisional puede existir antes del MANIFEST cuando otro THREAD haya identificado una responsabilidad aún no formalizada; **ese HANDOFF no da de alta el THREAD**. Antes de operar dentro de esa responsabilidad debe crearse su MANIFEST.

El usuario no necesita conocer la estructura interna del MANIFEST.

## 4. Responsabilidad y alcance

Toda conversación sustantiva conectada a un THREAD debe establecer un contrato compacto de responsabilidad antes de que el trabajo se expanda.

Formato recomendado:

```text
RESPONSABILIDAD DE LA CONVERSACIÓN

THREAD:
Responsabilidad:
Dentro de alcance:
Fuera de alcance:
Documentos que puede modificar directamente:
Corpus/dependencias principales que debe consultar:
Código/datos principales:
Entregable esperado:
Validación requerida:
HANDOFF asociado:
```

La conversación debe hacer cumplir activamente este límite.

### Trabajo dentro de alcance

Puede:

- inspeccionar cualquier parte del corpus necesaria para su tarea;
- modificar los archivos cuya evolución corresponda directamente a su responsabilidad;
- añadir o actualizar tests relevantes;
- actualizar documentación necesaria para conservar la trazabilidad;
- registrar propuestas en el HANDOFF de otro THREAD cuando detecte una necesidad fuera de su autoridad de edición.

### Trabajo fuera de alcance

No debe:

- rediseñar subsistemas no relacionados;
- modificar directamente documentos cuya evolución corresponda a otro THREAD;
- descargar grandes datasets sólo porque estén disponibles;
- modificar datos raw sin razón explícita;
- definir scoring definitivo cuando la tarea sólo cubre preparación de datos;
- introducir interpolación cuando la responsabilidad no la incluye;
- realizar investigación documental exhaustiva cuando la tarea sólo cubre cribado cuantitativo;
- cambiar metodología de proyecto sin documentar y escalar la decisión;
- asumir la responsabilidad de otra conversación porque el trabajo parezca adyacente.

Si un problema adyacente bloquea o afecta a la tarea, debe registrarse como propuesta en el HANDOFF del THREAD responsable cuando éste exista, conservando contexto y evidencia.

## 5. Orientación mínima del repositorio

La inspección inicial debe cubrir normalmente:

```text
1. knowledge
2. docs/core/PROJECT_WORKING_RULES.md
3. docs/core/THREAD_ARCHITECTURE.md
4. docs/core/PROJECT_INDEX.md
5. MANIFEST del THREAD
6. HANDOFF asociado
7. informe y corpus documental relevante
8. README.md cuando proceda
9. código y tests relevantes
10. rama/commit de trabajo resueltos desde el MANIFEST
```

No inspeccionar todo el repositorio indiscriminadamente. Comenzar con el contexto mínimo necesario y ampliar según la responsabilidad. El corpus es común para lectura: el hecho de que un documento no pertenezca al ámbito de edición del THREAD no impide consultarlo.

## 6. Jerarquía documental

### Reglas maestras

`docs/core/PROJECT_WORKING_RULES.md`

Reglas operativas permanentes.

### Arquitectura de hilos

`docs/core/THREAD_ARCHITECTURE.md`

Especificación del modelo operativo de THREADs: identidad, responsabilidad, estados, ciclos, dependencias, HANDOFF, MANIFEST, autoridad documental y bootstrap.

### Informes y documentos de conocimiento

Registran el conocimiento vigente, lo implementado, probado, medido, decidido y cambiado. Son parte de un corpus común para lectura; su autoridad de edición se delimita por responsabilidad.

### MANIFEST

Registra la identidad y el estado operativo actual del THREAD y es el mecanismo de incorporación de nuevas instancias/agentes.

### HANDOFF

Cada THREAD dispone, como regla general, de un HANDOFF persistente que actúa como **registro de eventos de entrada**: propuestas, revisiones, necesidades o tareas pendientes. No es un documento de transición de conversación.

Cualquier THREAD puede registrar una propuesta en el HANDOFF receptor; sólo el THREAD propietario evalúa la propuesta, cambia su estado y registra la resolución.

## 7. Aislamiento de responsabilidades

ClimaScope debe desarrollarse como un conjunto de líneas acotadas. Algunas responsabilidades típicas son:

```text
A. Método / documentación de proyecto
B. Catálogo y adquisición de estaciones
C. Datos climáticos / QC
D. Datos de agua / QC / agregación
E. Modelo Station-Location-Scope
F. Evidencia documental / investigación cualitativa
G. Análisis espacial / interpolación
H. Scoring / ranking
I. UX / aplicación / mapa
J. Arquitectura de datos / persistencia
K. Testing / CI / release engineering
```

Una conversación debe asumir normalmente una línea principal y, como máximo, dependencias secundarias explícitas.

## 8. Escalado en lugar de expansión de alcance

Cuando aparezca un problema fuera de responsabilidad:

```text
PROPUESTA FUERA DE ALCANCE
Problema / necesidad:
Por qué afecta a la tarea actual:
Evidencia:
THREAD responsable recomendado:
¿Bloquea?: sí/no
Entrada de HANDOFF creada:
```

Si existe un THREAD responsable, registrar la propuesta en su HANDOFF. La propuesta no implica aceptación, dependencia ni modificación automática. El THREAD receptor debe evaluarla y registrar su resolución.

Sólo ampliar el alcance cuando el propietario lo autorice o la definición actual ya lo incluya.

## 9. Disciplina documental

Si una conversación adopta una decisión metodológica sustantiva, no debe permanecer sólo en el chat.

Debe:

1. identificar el documento adecuado;
2. comprobar que su modificación entra dentro de la autoridad del THREAD;
3. si no entra, registrar una propuesta en el HANDOFF del THREAD responsable;
4. si entra, actualizar versión y contenido;
5. registrar decisión y justificación;
6. hacer commit en GitHub;
7. consolidar en `knowledge` cuando modifique conocimiento o estructura autoritativos;
8. registrar los SHAs relevantes.

Las reglas maestras sólo cambian cuando cambia una regla operativa global. Las decisiones específicas pertenecen al documento, informe, MANIFEST o resolución correspondiente.

## 10. Seguridad de datos

El bootstrap hereda las reglas del proyecto:

- preservar material raw;
- nunca convertir silenciosamente missing en cero;
- distinguir observado, derivado y modelado;
- conservar procedencia;
- no regenerar grandes datasets innecesariamente;
- no tratar `not_assessed` como ausencia de riesgo;
- utilizar tests y QC antes de promover datos a análisis.

## 11. Protocolo de finalización

Una conversación sustantiva debe cerrar con:

```text
RESPONSABILIDAD CERRADA / SESIÓN FINALIZADA

Trabajo dentro de alcance completado:
Propuestas fuera de alcance registradas:
Entradas de HANDOFF evaluadas:
Archivos modificados:
Datos modificados:
Tests/validación:
Versiones documentales:
Rama:
Commit SHA:
SHA de consolidación en knowledge:
Incertidumbre restante:
```

El estado final debe poder reproducirse desde GitHub sin necesitar el histórico de la conversación.

Finalizar una conversación **no crea un HANDOFF de sesión**. El HANDOFF del THREAD continúa existiendo como registro persistente de inputs pendientes y resueltos.

## 12. Versión compacta para nuevas conversaciones

> **ClimaScope — bootstrap de conversación**
>
> Repositorio: `gineslm/climascope`  
> Fuente de verdad: GitHub  
> Raíz de conocimiento: `knowledge`
>
> Antes de trabajar, entra conceptualmente en `knowledge`, lee `docs/core/PROJECT_WORKING_RULES.md` y `docs/core/THREAD_ARCHITECTURE.md`, localiza el THREAD objetivo y **conéctate mediante su MANIFEST**. Después consulta su HANDOFF como registro persistente de propuestas/revisiones pendientes y lee el corpus documental relevante.
>
> El HANDOFF no es memoria ni transición entre sesiones. Si otro THREAD detecta una necesidad que afecta a esta responsabilidad, puede registrar una propuesta en el HANDOFF; sólo el THREAD receptor la evalúa y registra la resolución.
>
> El corpus es común para lectura, pero la autoridad de edición está delimitada por responsabilidad. Si necesitas cambiar conocimiento fuera de tu autoridad, registra una propuesta en el HANDOFF del THREAD responsable en lugar de modificarlo directamente.
>
> Si se identifica una responsabilidad nueva y no existe THREAD compatible, da de alta el THREAD creando su MANIFEST y, normalmente, su HANDOFF persistente. El MANIFEST debe registrar `created_from_knowledge_commit` con el commit de `knowledge` desde el que se da de alta.

## 13. Historial de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 2026-08-15 | Bootstrap estándar inicial para conversaciones independientes y acotadas por responsabilidad. |
| 1.1.0 | 2026-08-16 | Alineación con `knowledge` como raíz de bootstrap y distinción explícita entre `created_from_knowledge_commit` y estado vigente de `knowledge`. |
| 1.2.0 | 2026-08-17 | Alineación con Arquitectura 0.5.0: alta = crear el MANIFEST; retirada de THREAD DECLARATION. |
| 1.3.0 | 2026-08-23 | Declaración de canonicidad del bloque operativo. |
| 1.4.0 | 2026-08-23 | Reorganización 2C: rutas actualizadas a `docs/core/…`. |
| 1.5.0 | 2026-09-08 | Alineación con Arquitectura 0.7.0: incorporación exclusivamente mediante MANIFEST; HANDOFF redefinido como registro persistente de eventos de entrada; corpus común para lectura y edición delimitada por responsabilidad. |
