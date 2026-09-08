# ClimaScope

**Versión del README:** 1.0.0  
**Idioma:** español (España)  
**Rama raíz de conocimiento:** `knowledge`

ClimaScope es un proyecto híbrido de producción y validación de conocimiento apoyado por agentes de IA. El repositorio conserva el conocimiento vigente, la estructura de trabajo y el historial de decisiones; las conversaciones son instancias temporales que se conectan a líneas persistentes de trabajo llamadas **THREADs**.

## 1. Punto de entrada

Para reconstruir el estado del proyecto desde `knowledge`:

1. `docs/core/PROJECT_WORKING_RULES.md`
2. `docs/core/THREAD_ARCHITECTURE.md`
3. `docs/core/THREAD_INDEX.md`
4. `docs/core/DOCUMENT_INDEX.md`

Después, localizar el THREAD relevante y leer su `MANIFEST.md` y su único `HANDOFF.md` persistente.

## 2. Arquitectura documental

```text
THREAD_INDEX.md
  → descubre THREADs, responsabilidades, MANIFESTs y HANDOFFs

DOCUMENT_INDEX.md
  → descubre el corpus documental y el THREAD con autoridad de evolución
```

El corpus es común para lectura. Cada documento tiene una única autoridad de evolución. Si un THREAD necesita cambiar conocimiento gobernado por otro, registra una propuesta en el HANDOFF del THREAD responsable.

El HANDOFF no es una transición de sesión: contiene únicamente inputs todavía no resueltos. Git conserva el historial de lo resuelto.

## 3. Ramas principales

```text
knowledge → conocimiento y estructura consolidados
develop   → integración del software
main      → software estable/desplegable
```

Las ramas de trabajo (`agent/*`, `feature/*`, etc.) no son fuentes alternativas de verdad global.

## 4. Estado técnico actual relevante

El repositorio contiene un pipeline AEMET de adquisición y procesamiento de datos climáticos/precipitación y una línea de trabajo de agua con QC y agregación W2.

La documentación vigente del pipeline de agua se encuentra en:

- `docs/threads/water-pipeline/AUDIT_REPORT.md`
- `docs/threads/water-pipeline/SOURCE_AUDIT.md`
- `docs/threads/water-pipeline/W1_PRECIPITATION_QC.md`

El modelo conceptual Station / Location / Scope / Evidence se documenta en:

- `docs/threads/station-location-evidence/MODEL.md`

## 5. Ejecución del pipeline AEMET existente

1. Copiar `.env.example` a `.env`.
2. Configurar una API key válida de AEMET fuera del repositorio.
3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutar:

```bash
python src/pipeline.py
```

La descarga histórica es reanudable por bloques: los bloques existentes en `data/raw/aemet/` se reutilizan cuando son válidos.

## 6. Datos y seguridad

- Los datos AEMET actuales viven principalmente en `data/raw/aemet/`.
- No convertir missing en cero.
- Preservar `.NO_DATA` como evidencia de disponibilidad de fuente.
- No guardar API keys, tokens ni secretos en el repositorio.
- Los datos raw y su procedencia no deben moverse o regenerarse sin una decisión explícita.

## 7. Tests

Para validar el código Python:

```bash
python -m pytest
```

Las cifras de validación histórica concretas se documentan en los informes de cada THREAD y no se tratan como garantía permanente del estado actual de la suite.

## 8. Trabajo con agentes de IA

Una conversación nueva debe entrar por `knowledge`, localizar el THREAD en `THREAD_INDEX.md`, incorporarse mediante su MANIFEST y consultar después su HANDOFF y el corpus relevante.

El detalle operativo se define en:

- `docs/core/PROJECT_AGENT_CONTEXT.md`
- `docs/core/THREAD_CONTEXT_BOOTSTRAP.md`

## 9. Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 2026-09-08 | README convertido en punto de entrada general de ClimaScope; la documentación histórica del downloader queda subordinada al estado actual del proyecto. |
