"""Job storage under ``demo-data/{job_id}/`` and the single-worker process pool."""

from __future__ import annotations

import json
import multiprocessing
import os
import re
import secrets
from concurrent.futures import Future, ProcessPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = Path(os.environ.get("PBS_DEMO_DATA", REPO_ROOT / "demo-data"))

RUNNING = ("queued", "converting", "projecting", "checking")
_JOB_ID = re.compile(r"^[0-9a-f]{12}$")
_executor: ProcessPoolExecutor | None = None


def job_dir(job_id: str) -> Path | None:
    if not _JOB_ID.match(job_id):
        return None
    path = DATA_DIR / job_id
    return path if path.is_dir() else None


def read_json(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default


def write_json(path: Path, data: Any) -> None:
    tmp = path.with_suffix(path.suffix + ".part")
    tmp.write_text(json.dumps(data, ensure_ascii=False, default=str), encoding="utf-8")
    tmp.replace(path)


def write_status(directory: Path, stage: str, **extra: Any) -> None:
    status = read_json(directory / "status.json", {})
    status.update(stage=stage, updated_at=_now(), **extra)
    write_json(directory / "status.json", status)


def status(directory: Path) -> dict[str, Any]:
    return read_json(directory / "status.json", {"stage": "unknown"})


def create_job(filename: str, data: bytes) -> str:
    job_id = secrets.token_hex(6)
    directory = DATA_DIR / job_id
    directory.mkdir(parents=True)
    (directory / "model.ifc").write_bytes(data)
    write_json(directory / "meta.json", {"name": filename, "size": len(data), "uploaded_at": _now()})
    write_status(directory, "queued")
    return job_id


def submit(job_id: str) -> None:
    from demo.app.worker import run_job

    directory = DATA_DIR / job_id
    future = _pool().submit(run_job, directory)
    future.add_done_callback(lambda f: _on_done(directory, f))


def list_jobs() -> list[dict[str, Any]]:
    if not DATA_DIR.is_dir():
        return []
    jobs = []
    for directory in DATA_DIR.iterdir():
        if job_dir(directory.name) is None:
            continue
        meta = read_json(directory / "meta.json", {})
        jobs.append({"id": directory.name, **meta, "status": status(directory)})
    return sorted(jobs, key=lambda j: j.get("uploaded_at", ""), reverse=True)


def mark_interrupted() -> None:
    """Jobs left running by a previous server process cannot resume."""
    for job in list_jobs():
        if job["status"].get("stage") in RUNNING:
            write_status(DATA_DIR / job["id"], "failed", error="Interrupted by a server restart.")


def shutdown() -> None:
    global _executor
    if _executor is not None:
        _executor.shutdown(wait=False, cancel_futures=True)
        _executor = None


def _pool() -> ProcessPoolExecutor:
    global _executor
    if _executor is None:
        _executor = ProcessPoolExecutor(max_workers=1, mp_context=multiprocessing.get_context("spawn"))
    return _executor


def _on_done(directory: Path, future: Future) -> None:
    error = future.exception()
    if error is not None:
        write_status(directory, "failed", error=f"Worker process failed: {error!r}")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")
