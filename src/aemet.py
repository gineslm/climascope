import os, time, json, csv
from pathlib import Path
from datetime import date, timedelta
import requests

BASE = "https://opendata.aemet.es/opendata/api"
CHUNK_DAYS = 180

def _chunk_path(out_dir, station_id, start, end):
    return Path(out_dir) / f"{station_id}_{start}_{end}.json"

def _no_data_path(out_dir, station_id, start, end):
    return Path(out_dir) / f"{station_id}_{start}_{end}.NO_DATA"

def _download_chunk(station_id, start, end, key, max_retries=6):
    url = (
        f"{BASE}/valores/climatologicos/diarios/datos/"
        f"fechaini/{start}T00:00:00UTC/"
        f"fechafin/{end}T23:59:59UTC/"
        f"estacion/{station_id}"
    )

    last_error = None
    for attempt in range(1, max_retries + 1):
        try:
            r = requests.get(
                url,
                headers={"api_key": key, "Cache-Control": "no-cache"},
                timeout=60,
            )
            r.raise_for_status()
            meta = r.json()

            # 404 from the AEMET API is a permanent "no data for this criteria"
            # condition, not a transient download failure.
            if meta.get("estado") == 404:
                desc = meta.get("descripcion", "No hay datos")
                return None, f"NO_DATA: {desc}"

            if meta.get("estado") != 200:
                raise RuntimeError(
                    f"AEMET estado {meta.get('estado')}: {meta.get('descripcion')}"
                )

            d = requests.get(
                meta["datos"],
                headers={"Cache-Control": "no-cache"},
                timeout=180,
            )

            if d.status_code == 200:
                payload = d.json()
                if not isinstance(payload, list):
                    raise RuntimeError(f"Respuesta inesperada de AEMET: {type(payload)}")
                return payload, None

            last_error = f"HTTP {d.status_code}: {d.text[:300]}"

        except (requests.RequestException, ValueError, RuntimeError) as exc:
            last_error = str(exc)

        wait = min(2 ** attempt, 30)
        print(
            f"  bloque {station_id} {start}->{end}: fallo ({last_error}); "
            f"reintento {attempt}/{max_retries} en {wait}s..."
        )
        time.sleep(wait)

    raise RuntimeError(
        f"No se pudo descargar {station_id} {start} -> {end} "
        f"tras {max_retries} intentos. Último error: {last_error}"
    )

def _expected_chunks(start_date, end_date):
    chunks = []
    cursor = start_date
    while cursor <= end_date:
        chunk_end = min(cursor + timedelta(days=CHUNK_DAYS - 1), end_date)
        chunks.append((cursor, chunk_end))
        cursor = chunk_end + timedelta(days=1)
    return chunks

def _read_chunk(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def _update_coverage(out_dir, station_id, records):
    """Actualiza un CSV sencillo con cobertura por estación."""
    path = Path(out_dir) / "station_coverage.csv"
    rows = {}
    if path.exists():
        with path.open("r", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                rows[row["station_id"]] = row

    dates = sorted(r.get("fecha") for r in records if r.get("fecha"))
    rows[station_id] = {
        "station_id": station_id,
        "first_data": dates[0] if dates else "",
        "last_data": dates[-1] if dates else "",
        "records": str(len(dates)),
    }

    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["station_id", "first_data", "last_data", "records"]
        )
        writer.writeheader()
        writer.writerows(sorted(rows.values(), key=lambda x: x["station_id"]))

def get_daily_data(station_id, start, end, out_dir):
    """
    Descarga climatología diaria AEMET en bloques <=180 días.

    - JSON existente: reutiliza sin petición.
    - .NO_DATA existente: omite sin petición.
    - 404 "no hay datos": crea .NO_DATA y continúa.
    - errores transitorios: reintenta.
    """
    key = os.getenv("AEMET_API_KEY")
    if not key:
        raise RuntimeError(
            "Falta AEMET_API_KEY. Copia .env.example a .env y añade una nueva clave."
        )

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    consolidated = out_dir / f"{station_id}_{start}_{end}.json"
    start_date = date.fromisoformat(start)
    end_date = date.fromisoformat(end)

    all_rows = []

    for chunk_start, chunk_end in _expected_chunks(start_date, end_date):
        cs, ce = chunk_start.isoformat(), chunk_end.isoformat()
        chunk_file = _chunk_path(out_dir, station_id, cs, ce)
        no_data_file = _no_data_path(out_dir, station_id, cs, ce)

        if chunk_file.exists():
            try:
                rows = _read_chunk(chunk_file)
                if isinstance(rows, list) and rows:
                    print(f"AEMET {station_id}: {cs} -> {ce} [YA DESCARGADO, reutilizando]")
                    all_rows.extend(rows)
                    continue
            except Exception:
                print(f"AEMET {station_id}: {cs} -> {ce} [archivo inválido, redescargando]")

        if no_data_file.exists():
            print(f"AEMET {station_id}: {cs} -> {ce} [SIN DATOS, omitiendo]")
            continue

        print(f"AEMET {station_id}: {cs} -> {ce} [DESCARGANDO]")
        rows, status = _download_chunk(station_id, cs, ce, key)

        if status and status.startswith("NO_DATA"):
            no_data_file.write_text(status + "\n", encoding="utf-8")
            print(f"  {status} -> guardado como {no_data_file.name}")
            continue

        chunk_file.write_text(
            json.dumps(rows, ensure_ascii=False),
            encoding="utf-8"
        )
        print(f"  guardado: {chunk_file.name}")
        all_rows.extend(rows)

    by_date = {}
    for row in all_rows:
        if row.get("fecha"):
            by_date[row["fecha"]] = row

    unique = [by_date[k] for k in sorted(by_date)]

    consolidated.write_text(
        json.dumps(unique, ensure_ascii=False),
        encoding="utf-8"
    )
    _update_coverage(out_dir, station_id, unique)

    print(f"Consolidado: {consolidated}")
    return consolidated
