#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprobador de coherencia del conocimiento — ClimaScope
=======================================================

Revisa invariantes ESTRUCTURALES del repositorio. Solo lee; no modifica nada.

Qué comprueba:
  1. Todo THREAD (directorio con MANIFEST.md) tiene un HANDOFF.md canónico y
     `handoff.path` apunta exactamente a ese archivo.
  2. El bloque de identidad del MANIFEST contiene los campos estructurados
     mínimos: thread_id, domain, status, owner, current_cycle, origin,
     repository y handoff.
  3. Cada MANIFEST contiene una sección `## Responsabilidad` no vacía.
  4. `status` y `origin.type` usan valores permitidos; THREAD_DERIVED y
     MIGRATED requieren `source_id`.
  5. THREAD_INDEX.md lista exactamente los THREADs existentes y coincide con
     sus MANIFESTs en thread_id, status y HANDOFF.
  6. DOCUMENT_INDEX.md sólo contiene documentos existentes, sin duplicados,
     con authority_thread/authority_manifest existentes y coherentes entre sí.
     Además, el MANIFEST autoritativo debe declarar el documento en su sección
     `## Autoridad documental vigente`.
  7. Las referencias documentales explícitas entre backticks dentro de los
     MANIFESTs apuntan a rutas existentes cuando tienen forma de archivo.
  8. Las entradas HANDOFF reconocibles como bloques YAML se validan best-effort:
     type/status válidos, origin_thread existente y distinto del THREAD receptor.
  9. Seguridad best-effort: código, configuración y documentación textual
     fuera de directorios voluminosos excluidos no contienen patrones típicos
     de credenciales.

Qué NO hace:
  - no juzga si una responsabilidad está bien definida;
  - no decide si un commit contiene realmente una sola decisión;
  - no infiere dependencias semánticas a partir de prosa;
  - no decide si un THREAD debería afectar a otro;
  - no valida todavía un formato físico canónico del HANDOFF más allá de
    bloques YAML que pueda reconocer.

Uso:
    python scripts/check_knowledge.py [ruta_raiz]

Sin argumento, busca la raíz del repo hacia arriba desde el directorio actual.
Devuelve 0 si no hay errores; 1 si hay al menos un error. Los avisos (WARN) no
hacen fallar la comprobación.
"""

import os
import re
import sys

STATUS_VALIDOS = {"PROPOSED", "ACTIVE", "BLOCKED", "CLOSED", "ARCHIVED"}
ORIGIN_VALIDOS = {"USER_DECLARED", "THREAD_DERIVED", "MIGRATED"}
CAMPOS_IDENTIDAD = [
    "thread_id",
    "domain",
    "status",
    "owner",
    "current_cycle",
    "origin",
    "repository",
    "handoff",
]
HANDOFF_TYPES = {"proposal", "review", "need", "task"}
HANDOFF_STATUS = {"proposed", "in_review", "deferred", "ready_to_apply"}

TEXT_EXTS = {
    ".md", ".py", ".yml", ".yaml", ".txt", ".toml", ".ini", ".cfg", ".sh",
    ".example",
}
SPECIAL_NAMES = {"requirements.txt", ".env", ".env.example", "Dockerfile"}
SKIP_DIRS = {".git", "data", "results", "__pycache__", ".pytest_cache"}
MAX_SECRET_SCAN_BYTES = 2_000_000

SECRET_PATTERNS = [
    ("GitHub token",   re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}")),
    ("GitHub PAT",     re.compile(r"github_pat_[A-Za-z0-9_]{30,}")),
    ("AWS access key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("Clave privada",  re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    (
        "token/secret/password",
        re.compile(
            r"(?i)\b(token|secret|password|passwd)\s*[:=]\s*"
            r"['\"]?[A-Za-z0-9/\+_\-]{20,}"
        ),
    ),
]

REF_EXTS = ("md", "py", "csv", "json", "yml", "yaml", "txt", "toml")


class Report:
    def __init__(self):
        self.errors = []
        self.warns = []

    def error(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warns.append(msg)

    def dump(self):
        if self.errors:
            print("\nERRORES:")
            for e in self.errors:
                print("  [ERROR] " + e)
        if self.warns:
            print("\nAVISOS:")
            for w in self.warns:
                print("  [WARN]  " + w)
        print(
            "\nResumen: %d error(es), %d aviso(s)."
            % (len(self.errors), len(self.warns))
        )
        return 1 if self.errors else 0


def find_root(start):
    cur = os.path.abspath(start)
    while True:
        if os.path.isfile(
            os.path.join(cur, "docs", "core", "THREAD_ARCHITECTURE.md")
        ):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return None
        cur = parent


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def parse_yaml_block(text):
    """Parser deliberadamente pequeño para el YAML simple de los MANIFESTs."""
    m = re.search(r"```ya?ml\s*\n(.*?)\n```", text, re.DOTALL)
    if not m:
        return None
    block = m.group(1)
    result = {}
    parent = None
    for raw in block.splitlines():
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        key, sep, val = raw.strip().partition(":")
        if not sep:
            continue
        key = key.strip()
        val = val.strip()
        if indent == 0:
            if val == "":
                result[key] = {}
                parent = key
            else:
                result[key] = val
                parent = None
        elif indent >= 2 and parent is not None:
            if not isinstance(result.get(parent), dict):
                result[parent] = {}
            result[parent][key] = val
    return result


def parse_md_tables(text):
    tables = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|"):
            block = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                block.append(lines[i].strip())
                i += 1
            rows = []
            for row in block:
                cells = [c.strip() for c in row.strip().strip("|").split("|")]
                rows.append(cells)
            data = [
                r
                for r in rows
                if not all(re.fullmatch(r":?-+:?", c or "-") for c in r)
            ]
            if data:
                tables.append((data[0], data[1:]))
        else:
            i += 1
    return tables


def unbacktick(cell):
    c = cell.strip()
    if c.startswith("`") and c.endswith("`") and len(c) >= 2:
        c = c[1:-1]
    return c.strip()


def find_thread_dirs(root):
    dirs = []
    for base, subdirs, files in os.walk(os.path.join(root, "docs")):
        subdirs[:] = [d for d in subdirs if d not in SKIP_DIRS]
        if "MANIFEST.md" in files:
            dirs.append(base)
    return sorted(dirs)


def rel(root, path):
    return os.path.relpath(path, root).replace(os.sep, "/")


def section_body(text, title):
    pattern = re.compile(
        r"^##\s+" + re.escape(title) + r"\s*$\n(.*?)(?=^##\s+|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(text)
    return m.group(1).strip() if m else None


def authority_paths_from_manifest(text):
    body = section_body(text, "Autoridad documental vigente")
    if body is None:
        return set(), False
    if re.search(r"\bNingun[ao]?\b|\bNingún\b", body, re.IGNORECASE):
        return set(), True
    paths = set()
    for token in re.findall(r"`([^`]+)`", body):
        token = token.strip()
        if "/" in token or token.endswith(".md"):
            paths.add(token)
    return paths, True


def check_threads(root, rep):
    thread_ids = {}
    manifest_paths = set()
    manifest_data = {}
    manifest_text = {}

    for d in find_thread_dirs(root):
        manifest = os.path.join(d, "MANIFEST.md")
        mrel = rel(root, manifest)
        manifest_paths.add(mrel)
        handoff = os.path.join(d, "HANDOFF.md")

        if not os.path.isfile(handoff):
            rep.error("%s: falta HANDOFF.md en el directorio del THREAD." % rel(root, d))

        text = read(manifest)
        manifest_text[mrel] = text
        y = parse_yaml_block(text)
        if y is None:
            rep.error("%s: no se encontró bloque de identidad ```yaml." % mrel)
            continue
        manifest_data[mrel] = y

        for campo in CAMPOS_IDENTIDAD:
            if campo not in y or y.get(campo) in (None, "", {}):
                rep.error("%s: falta el campo estructurado '%s'." % (mrel, campo))

        responsibility = section_body(text, "Responsabilidad")
        if responsibility is None:
            rep.error("%s: falta la sección '## Responsabilidad'." % mrel)
        elif not responsibility.strip():
            rep.error("%s: la sección '## Responsabilidad' está vacía." % mrel)

        st = y.get("status")
        if st is not None and st not in STATUS_VALIDOS:
            rep.error(
                "%s: status '%s' no válido (permitidos: %s)."
                % (mrel, st, ", ".join(sorted(STATUS_VALIDOS)))
            )

        origin = y.get("origin")
        if isinstance(origin, dict):
            otype = origin.get("type")
            if otype not in ORIGIN_VALIDOS:
                rep.error("%s: origin.type '%s' no válido." % (mrel, otype))
            if otype in ("THREAD_DERIVED", "MIGRATED") and not origin.get("source_id"):
                rep.error("%s: origin.type=%s requiere 'source_id'." % (mrel, otype))
        elif "origin" in y:
            rep.error("%s: 'origin' debe ser un bloque con 'type'." % mrel)

        repo = y.get("repository")
        if not isinstance(repo, dict):
            rep.error("%s: 'repository' debe ser un bloque." % mrel)
        else:
            if not repo.get("knowledge_branch"):
                rep.error("%s: repository.knowledge_branch es obligatorio." % mrel)
            sha = repo.get("created_from_knowledge_commit")
            if sha and not re.fullmatch(r"[0-9a-f]{7,40}", sha):
                rep.warn("%s: created_from_knowledge_commit no parece un SHA." % mrel)

        ho = y.get("handoff")
        if not isinstance(ho, dict):
            rep.error("%s: 'handoff' debe ser un bloque." % mrel)
        else:
            hp = ho.get("path")
            canonical = rel(root, handoff)
            if not hp:
                rep.error("%s: falta handoff.path." % mrel)
            elif not os.path.isfile(os.path.join(root, hp)):
                rep.error("%s: handoff.path '%s' no existe." % (mrel, hp))
            elif hp != canonical:
                rep.error(
                    "%s: handoff.path '%s' debe apuntar al HANDOFF canónico '%s'."
                    % (mrel, hp, canonical)
                )

        tid = y.get("thread_id")
        if tid:
            if tid in thread_ids:
                rep.error("thread_id duplicado '%s' (%s y %s)." % (tid, thread_ids[tid], mrel))
            thread_ids[tid] = mrel

        text_refs = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        for token in re.findall(r"`([^`]+)`", text_refs):
            token = token.strip()
            if "/" in token and "." in token and token.rsplit(".", 1)[-1].lower() in REF_EXTS:
                if not os.path.exists(os.path.join(root, token)):
                    rep.error("%s: referencia a '%s' que no existe." % (mrel, token))

    return thread_ids, manifest_paths, manifest_data, manifest_text


def check_thread_index(root, rep, manifest_paths, manifest_data):
    path = os.path.join(root, "docs", "core", "THREAD_INDEX.md")
    if not os.path.isfile(path):
        rep.error("Falta docs/core/THREAD_INDEX.md.")
        return
    text = read(path)
    tabla = None
    for head, rows in parse_md_tables(text):
        low = [h.lower() for h in head]
        required = {"thread_id", "status", "manifest", "handoff"}
        if required.issubset(set(low)):
            tabla = (low, rows)
            break
    if not tabla:
        rep.error("THREAD_INDEX.md: no se encontró la tabla canónica de THREADs.")
        return

    low, rows = tabla
    idx_tid = low.index("thread_id")
    idx_status = low.index("status")
    idx_manifest = low.index("manifest")
    idx_handoff = low.index("handoff")
    indexados = set()

    for r in rows:
        if len(r) <= max(idx_tid, idx_status, idx_manifest, idx_handoff):
            continue
        tid_idx = unbacktick(r[idx_tid])
        st_idx = unbacktick(r[idx_status])
        mp = unbacktick(r[idx_manifest])
        hp_idx = unbacktick(r[idx_handoff])
        indexados.add(mp)

        if mp not in manifest_paths:
            rep.error("THREAD_INDEX.md: lista '%s', que no existe." % mp)
            continue
        y = manifest_data.get(mp)
        if not y:
            continue
        if tid_idx != y.get("thread_id"):
            rep.error("THREAD_INDEX.md: thread_id '%s' no coincide con %s ('%s')." % (tid_idx, mp, y.get("thread_id")))
        if st_idx != y.get("status"):
            rep.error("THREAD_INDEX.md: status '%s' de %s no coincide con el MANIFEST ('%s')." % (st_idx, mp, y.get("status")))
        ho = y.get("handoff")
        hp_man = ho.get("path") if isinstance(ho, dict) else None
        if hp_idx != hp_man:
            rep.error("THREAD_INDEX.md: HANDOFF '%s' de %s no coincide con el MANIFEST ('%s')." % (hp_idx, mp, hp_man))

    for mp in manifest_paths:
        if mp not in indexados:
            rep.error("THREAD_INDEX.md: no lista el MANIFEST existente '%s'." % mp)


def check_document_index(root, rep, thread_ids, manifest_data, manifest_text):
    path = os.path.join(root, "docs", "core", "DOCUMENT_INDEX.md")
    if not os.path.isfile(path):
        rep.error("Falta docs/core/DOCUMENT_INDEX.md.")
        return
    text = read(path)
    tabla = None
    for head, rows in parse_md_tables(text):
        low = [h.lower() for h in head]
        required = {"path", "authority_thread", "authority_manifest"}
        if required.issubset(set(low)):
            tabla = (low, rows)
            break
    if not tabla:
        rep.error("DOCUMENT_INDEX.md: no se encontró la tabla canónica del corpus.")
        return

    low, rows = tabla
    i_path = low.index("path")
    i_thread = low.index("authority_thread")
    i_man = low.index("authority_manifest")
    vistos = set()

    for r in rows:
        if len(r) <= max(i_path, i_thread, i_man):
            continue
        p = unbacktick(r[i_path])
        th = unbacktick(r[i_thread])
        man = unbacktick(r[i_man])
        if p in vistos:
            rep.error("DOCUMENT_INDEX.md: documento duplicado '%s'." % p)
        vistos.add(p)
        if not os.path.isfile(os.path.join(root, p)):
            rep.error("DOCUMENT_INDEX.md: documento '%s' no existe." % p)
        if th not in thread_ids:
            rep.error("DOCUMENT_INDEX.md: authority_thread '%s' no corresponde a ningún THREAD." % th)
        if man not in manifest_data:
            rep.error("DOCUMENT_INDEX.md: authority_manifest '%s' no es un MANIFEST existente." % man)
            continue
        y = manifest_data[man]
        if y.get("thread_id") != th:
            rep.error("DOCUMENT_INDEX.md: '%s' declara authority_thread '%s' pero authority_manifest pertenece a '%s'." % (p, th, y.get("thread_id")))
        auth_paths, has_section = authority_paths_from_manifest(manifest_text[man])
        if not has_section:
            rep.error("%s: falta la sección '## Autoridad documental vigente' necesaria para verificar DOCUMENT_INDEX.md." % man)
        elif p not in auth_paths:
            rep.error("DOCUMENT_INDEX.md: '%s' no está declarado bajo autoridad en %s." % (p, man))


def check_handoffs(root, rep, thread_ids, manifest_data):
    manifest_by_dir = {}
    for mp, y in manifest_data.items():
        manifest_by_dir[os.path.dirname(os.path.join(root, mp))] = y
    for d in find_thread_dirs(root):
        handoff = os.path.join(d, "HANDOFF.md")
        if not os.path.isfile(handoff):
            continue
        text = read(handoff)
        receiver = manifest_by_dir.get(d, {}).get("thread_id")
        for m in re.finditer(r"```ya?ml\s*\n(.*?)\n```", text, re.DOTALL):
            entry = parse_yaml_block("```yaml\n" + m.group(1) + "\n```")
            if not entry or "type" not in entry:
                continue
            hrel = rel(root, handoff)
            if entry.get("type") not in HANDOFF_TYPES:
                rep.error("%s: entrada con type '%s' no válido." % (hrel, entry.get("type")))
            if entry.get("status") and entry.get("status") not in HANDOFF_STATUS:
                rep.error("%s: entrada con status '%s' no válido." % (hrel, entry.get("status")))
            origin = entry.get("origin_thread")
            if not origin:
                rep.error("%s: entrada sin 'origin_thread'." % hrel)
            elif origin not in thread_ids:
                rep.error("%s: origin_thread '%s' no corresponde a ningún THREAD." % (hrel, origin))
            elif receiver and origin == receiver:
                rep.error("%s: una entrada HANDOFF no puede originarse en el mismo THREAD receptor '%s'." % (hrel, receiver))


def check_secrets(root, rep):
    for base, subdirs, files in os.walk(root):
        subdirs[:] = [d for d in subdirs if d not in SKIP_DIRS]
        for fn in files:
            if fn == "check_knowledge.py":
                continue
            ext = os.path.splitext(fn)[1].lower()
            if ext not in TEXT_EXTS and fn not in SPECIAL_NAMES:
                continue
            full = os.path.join(base, fn)
            try:
                if os.path.getsize(full) > MAX_SECRET_SCAN_BYTES:
                    rep.warn("No se escanea por tamaño '%s' (> %d bytes)." % (rel(root, full), MAX_SECRET_SCAN_BYTES))
                    continue
                content = read(full)
            except Exception:
                continue
            for nombre, patron in SECRET_PATTERNS:
                if patron.search(content):
                    rep.error("Posible credencial (%s) en '%s'. Las llaves no van en el repo." % (nombre, rel(root, full)))
                    break


def main(argv):
    start = argv[1] if len(argv) > 1 else os.getcwd()
    root = find_root(start)
    if not root:
        print("No se encontró la raíz del repositorio (docs/core/THREAD_ARCHITECTURE.md).")
        return 2
    print("Comprobando coherencia del conocimiento en: %s" % root)
    rep = Report()
    thread_ids, manifest_paths, manifest_data, manifest_text = check_threads(root, rep)
    check_thread_index(root, rep, manifest_paths, manifest_data)
    check_document_index(root, rep, thread_ids, manifest_data, manifest_text)
    check_handoffs(root, rep, thread_ids, manifest_data)
    check_secrets(root, rep)
    print("THREADs encontrados: %d." % len(manifest_paths))
    return rep.dump()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
