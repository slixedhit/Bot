"""Backup utilities (local file backups only)."""
from pathlib import Path
import zipfile
import datetime


def create_backup(data_directory: Path, out_dir: Path | None = None) -> Path:
    out_dir = out_dir or data_directory / "backups"
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    out_path = out_dir / f"backup-{ts}.zip"
    with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in data_directory.rglob("*"):
            if p.is_file():
                zf.write(p, p.relative_to(data_directory))
    return out_path
