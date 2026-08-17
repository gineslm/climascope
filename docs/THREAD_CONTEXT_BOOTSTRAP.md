# ClimaScope — Bootstrap de contexto de nuevos hilos

**Versión del documento:** 1.2.0  
**Creado:** 2026-08-15  
**Repositorio:** `gineslm/climascope`  
**Rama raíz de conocimiento:** `knowledge`  
**Propósito:** bloque reutilizable de contexto/instrucciones para abrir una nueva conversación de ClimaScope.

## 1. Propósito

Este documento es el bootstrap estándar para una nueva conversación que trabaje en ClimaScope.

Su propósito es hacer que cada conversación:

- sea independiente del histórico de chats anteriores;
- se conecte al repositorio central;
- conozca el método y la documentación vigente del proyecto;
- quede explícitamente acotada a una responsabilidad;
- no absorba silenciosamente responsabilidades de otras líneas.

El repositorio es la fuente de verdad. La conversación es una sesión de trabajo, no la memoria permanente del proyecto.

## 2. Bootstrap obligatorio

Cuando este documento forme parte del contexto del proyecto, la conversación debe seguir esta secuencia antes de realizar trabajo sustantivo:

> **Bootstrap de proyecto ClimaScope**
>
> Trabaja contra el repositorio central de GitHub `gineslm/climascope`.
>
> **Primero entra conceptualmente en la rama `knowledge` como raíz de conocimiento y estructura consolidada.** Después lee `docs/PROJECT_WORKING_RULES.md`, `docs/THREAD_ARCHITECTURE.md` y el contexto de proyecto vigente. A continuación inspecciona el informe relevante y cualquier HANDOFF o MANIFEST aplicable.
>
> GitHub es el registro autoritativo del proyecto. No asumas que una información existe porque apareciera en otra conversación. Si falta un documento referenciado en el repositorio, informa de ello y solicítalo en lugar de inventarlo.
>
> Antes de realizar cambios sustantivos, informa de las versiones documentales relevantes, el estado consolidado y la responsabilidad que se ha resuelto.

### Regla de autoridad

Una rama de trabajo indicada por un HANDOFF o MANIFEST es una referencia al trabajo operativo, no una fuente alternativa de verdad global. Las reglas, arquitectura, identidad de THREAD, MANIFEST, HANDOFF y decisiones consolidadas deben resolverse desde `knowledge`.

## 3. Alta de THREAD (crear su MANIFEST)

Dar de alta un THREAD es **crear y consolidar su MANIFEST**; no existe un artefacto de «declaración» independiente. Un THREAD existe si y solo si existe su MANIFEST.

Cuando una conversación nueva identifica una responsabilidad y no existe un THREAD compatible:

1. resolver primero el estado de `knowledge`;
2. crear su MANIFEST (el alta) con `origin.type: USER_DECLARED`;
3. registrar en el MANIFEST el commit de `knowledge` desde el que se da de alta el THREAD:

```yaml
repository:
  knowledge_branch: knowledge
  created_from_knowledge_commit: <sha>
```

`created_from_knowledge_commit` es el commit de `knowledge` desde el que se da de alta el THREAD mediante su MANIFEST. Tiene la misma semántica para los tres orígenes (`USER_DECLARED`, `THREAD_DERIVED`, `MIGRATED`); es histórico e inmutable y no se actualiza cuando `knowledge` avanza.

Forma canónica única: el campo plano `created_from_knowledge_commit`. No usar `knowledge_commit` sin calificador ni la forma anidada `created_from_knowledge`. El estado vigente se resuelve siempre leyendo la rama `knowledge`; para fijar una base reproducible de software puede usarse `knowledge_basis.commit`.

El usuario no necesita conocer la estructura interna del MANIFEST.

## 4. Responsabilidad y alcance

Toda conversación sustantiva debe establecer un contrato compacto de responsabilidad antes de que el trabajo se expanda.

Formato recomendado:

```text
RESPONSABILIDAD DE LA CONVERSACIÓN

Responsabilidad:
Dentro de alcance:
Fuera de alcance:
Documentos principales:
Código/datos principales:
Entregable esperado:
Validación requerida:
Siguiente handoff, si procede:
```

La conversación debe hacer cumplir activamente este límite.

### Trabajo dentro de alcance

Puede:

- inspeccionar el contexto necesario para su tarea;
- modificar archivos directamente relevantes;
- añadir o actualizar tests relevantes;
- actualizar documentación necesaria para conservar la trazabilidad;
- crear un handoff para la siguiente conversación especializada.

### Trabajo fuera de alcance

No debe:

- rediseñar subsistemas no relacionados;
- descargar grandes datasets sólo porque estén disponibles;
- modificar datos raw sin razón explícita;
- definir scoring definitivo cuando la tarea sólo cubre preparación de datos;
- introducir interpolación cuando la responsabilidad no la incluye;
- realizar investigación documental exhaustiva cuando la tarea sólo cubre cribado cuantitativo;
- cambiar metodología de proyecto sin documentar y escalar la decisión;
- asumir la responsabilidad de otra conversación porque el trabajo parezca adyacente.

Si un problema adyacente bloquea la tarea, registrarlo como dependencia/cuestion abierta en lugar de ampliar automáticamente el alcance.

## 5. Orientación mínima del repositorio

La inspección inicial debe cubrir normalmente:

```text
1. knowledge
2. docs/PROJECT_WORKING_RULES.md
3. docs/THREAD_ARCHITECTURE.md
4. informe de proyecto relevante
5. MANIFEST/HANDOFF específico, si existe
6. README.md cuando proceda
7. código y tests relevantes
8. rama/commit de trabajo resueltos desde el MANIFEST
```

No inspeccionar todo el repositorio indiscriminadamente. Comenzar con el contexto mínimo necesario y ampliar sólo según la responsabilidad.

## 6. Jerarquía documental

### Reglas maestras

`docs/PROJECT_WORKING_RULES.md`

Reglas operativas permanentes.

### Arquitectura de hilos

`docs/THREAD_ARCHITECTURE.md`

Especificación del modelo operativo de THREADs: identidad, responsabilidad, estados, ciclos, dependencias, HANDOFF, MANIFEST, autoridad documental y bootstrap.

### Informes de proyecto

Los informes registran lo implementado, probado, medido, decidido y cambiado.

### MANIFESTs y HANDOFFs

Los MANIFESTs registran el estado operativo actual de cada THREAD. Los HANDOFFs transfieren responsabilidad/contexto. Ambos se consolidan en `knowledge`.

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
PROBLEMA FUERA DE ALCANCE
Problema:
Por qué afecta a la tarea actual:
Evidencia:
Responsable recomendado:
¿Bloquea?: sí/no
Siguiente handoff propuesto:
```

Sólo ampliar el alcance cuando el propietario lo autorice o la definición actual ya lo incluya.

## 9. Disciplina documental

Si una conversación adopta una decisión metodológica sustantiva, no debe permanecer sólo en el chat.

Debe:

1. identificar el documento adecuado;
2. actualizar su versión;
3. registrar decisión y justificación;
4. hacer commit en GitHub;
5. consolidar en `knowledge` cuando modifique conocimiento o estructura autoritativos;
6. registrar los SHAs relevantes.

Las reglas maestras sólo cambian cuando cambia una regla operativa global. Las decisiones específicas pertenecen al documento, informe, MANIFEST o HANDOFF correspondiente.

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
RESPONSABILIDAD CERRADA

Trabajo dentro de alcance completado:
Problemas fuera de alcance descubiertos:
Archivos modificados:
Datos modificados:
Tests/validación:
Versiones documentales:
Rama:
Commit SHA:
SHA de consolidación en knowledge:
Incertidumbre restante:
Siguiente handoff:
```

El estado final debe poder reproducirse desde GitHub sin necesitar el histórico de la conversación.

## 12. Versión compacta para nuevas conversaciones

> **ClimaScope — bootstrap de conversación**
>
> Repositorio: `gineslm/climascope`  
> Fuente de verdad: GitHub  
> Raíz de conocimiento: `knowledge`
>
> Antes de trabajar, entra conceptualmente en `knowledge`, lee `docs/PROJECT_WORKING_RULES.md` y `docs/THREAD_ARCHITECTURE.md`, y después el informe, MANIFEST o HANDOFF aplicable. No inventes documentos ausentes.
>
> Si se identifica una responsabilidad nueva y no existe THREAD compatible, da de alta el THREAD creando su MANIFEST con `origin.type: USER_DECLARED` (no hay un artefacto de declaración aparte). El MANIFEST debe registrar `created_from_knowledge_commit` con el commit de `knowledge` desde el que se da de alta el THREAD; es histórico e inmutable y el estado vigente se resuelve siempre desde `knowledge`.
>
> Mantén esta conversación acotada. Si aparece una dependencia adyacente, regístrala como fuera de alcance. Al terminar, informa de archivos, tests, versiones documentales, rama, SHA de trabajo y SHA de consolidación en `knowledge` cuando corresponda.

## 13. Historial de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 2026-08-15 | Bootstrap estándar inicial para conversaciones independientes y acotadas por responsabilidad. |
| 1.1.0 | 2026-08-16 | Alineación con `knowledge` como raíz de bootstrap y distinción explícita entre `created_from_knowledge_commit` y estado vigente de `knowledge`. |
| 1.2.0 | 2026-08-17 | Alineación con Arquitectura 0.5.0 (Alt 1): alta = crear el MANIFEST; retirada de THREAD DECLARATION; `created_from_knowledge_commit` con semántica uniforme y forma canónica única. |
