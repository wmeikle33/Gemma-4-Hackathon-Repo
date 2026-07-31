import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

from .schemas import SupportRequest, SupportResponse


def write_audit_record(
    request: SupportRequest,
    response: SupportResponse,
    output_dir: Path,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)

    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "request": asdict(request),
        "response": asdict(response),
    }

    output_path = output_dir / f"{request.request_id}.json"
    output_path.write_text(
        json.dumps(record, indent=2),
        encoding="utf-8",
    )

    return output_path
