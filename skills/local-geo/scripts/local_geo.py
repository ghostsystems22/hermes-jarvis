"""Local GPS helpers for the Overland webhook."""

from __future__ import annotations

import argparse
import hmac
import json
import os
from datetime import UTC, datetime, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOCATION_PATH = SKILL_ROOT / "current_location.json"
DEFAULT_TOKEN_PATH = SKILL_ROOT / "token.txt"
DEFAULT_ROUTE = "/webhooks/overland"
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 80
STALE_AFTER = timedelta(hours=3)


def _utc_now() -> datetime:
    return datetime.now(UTC)


def _ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def _json_response(handler: BaseHTTPRequestHandler, status: int, payload: dict[str, Any]) -> None:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    if status == 401:
        handler.send_header("WWW-Authenticate", 'Bearer realm="overland"')
    handler.end_headers()
    handler.wfile.write(body)


def _parse_timestamp(value: Any) -> datetime:
    if isinstance(value, (int, float)):
        seconds = float(value)
        if seconds > 10**11:
            seconds /= 1000.0
        return datetime.fromtimestamp(seconds, tz=UTC)
    if isinstance(value, str):
        text = value.strip()
        if not text:
            raise ValueError("empty timestamp")
        if text.isdigit():
            return _parse_timestamp(int(text))
        if text.endswith("Z"):
            text = text[:-1] + "+00:00"
        try:
            parsed = datetime.fromisoformat(text)
        except ValueError as exc:
            raise ValueError(f"unsupported timestamp format: {value!r}") from exc
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=UTC)
        return parsed.astimezone(UTC)
    raise ValueError(f"unsupported timestamp type: {type(value).__name__}")


def _extract_features(payload: dict[str, Any]) -> list[dict[str, Any]]:
    locations = payload.get("locations")
    if isinstance(locations, dict):
        if locations.get("type") == "FeatureCollection":
            features = locations.get("features", [])
        elif isinstance(locations.get("features"), list):
            features = locations.get("features", [])
        else:
            features = [locations]
    elif isinstance(locations, list):
        features = locations
    else:
        features = []
    return [feature for feature in features if isinstance(feature, dict)]


def _last_point_feature(features: list[dict[str, Any]]) -> dict[str, Any] | None:
    for feature in reversed(features):
        geometry = feature.get("geometry")
        if not isinstance(geometry, dict) or geometry.get("type") != "Point":
            continue
        coordinates = geometry.get("coordinates")
        if not isinstance(coordinates, list) or len(coordinates) < 2:
            continue
        properties = feature.get("properties")
        if not isinstance(properties, dict):
            continue
        timestamp = properties.get("timestamp")
        if timestamp is None:
            continue
        try:
            lon = float(coordinates[0])
            lat = float(coordinates[1])
        except (TypeError, ValueError):
            continue
        return {"lat": lat, "lon": lon, "timestamp": timestamp}
    return None


def store_current_location(record: dict[str, Any], location_path: Path = DEFAULT_LOCATION_PATH) -> Path:
    _ensure_parent(location_path)
    stored = {
        "lat": record["lat"],
        "lon": record["lon"],
        "timestamp": record["timestamp"],
        "received_at": _utc_now().isoformat().replace("+00:00", "Z"),
        "source": "overland",
    }
    location_path.write_text(json.dumps(stored, ensure_ascii=False, indent=2), encoding="utf-8")
    return location_path


def process_overland_payload(payload: dict[str, Any], location_path: Path = DEFAULT_LOCATION_PATH) -> dict[str, Any] | None:
    features = _extract_features(payload)
    record = _last_point_feature(features)
    if record is None:
        return None
    store_current_location(record, location_path=location_path)
    return record


def get_current_location(location_path: Path | str = DEFAULT_LOCATION_PATH) -> dict[str, Any]:
    path = Path(location_path)
    data = json.loads(path.read_text(encoding="utf-8"))
    lat = float(data["lat"])
    lon = float(data["lon"])
    timestamp = data["timestamp"]
    result: dict[str, Any] = {"lat": lat, "lon": lon, "timestamp": timestamp}

    try:
        point_time = _parse_timestamp(timestamp)
    except ValueError:
        result["warning"] = "position possiblement périmée"
        return result

    if _utc_now() - point_time > STALE_AFTER:
        result["warning"] = "position possiblement périmée"
    return result


def _load_token(token_file: Path = DEFAULT_TOKEN_PATH) -> str:
    token = os.environ.get("LOCAL_GEO_TOKEN", "").strip()
    if token:
        return token

    token_path = Path(os.environ.get("LOCAL_GEO_TOKEN_FILE", str(token_file)))
    token = token_path.read_text(encoding="utf-8").strip()
    if not token:
        raise RuntimeError(f"empty token in {token_path}")
    return token


def _authorization_ok(handler: BaseHTTPRequestHandler, token: str) -> bool:
    header = handler.headers.get("Authorization", "")
    if not header.startswith("Bearer "):
        return False
    supplied = header.removeprefix("Bearer ").strip()
    return hmac.compare_digest(supplied, token)


class OverlandWebhookHandler(BaseHTTPRequestHandler):
    storage_path = DEFAULT_LOCATION_PATH
    route = DEFAULT_ROUTE
    token = None

    def do_POST(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
        if urlparse(self.path).path.rstrip("/") != self.route.rstrip("/"):
            _json_response(self, 404, {"result": "error", "error": "not found"})
            return

        if not self.token or not _authorization_ok(self, self.token):
            _json_response(self, 401, {"result": "error", "error": "unauthorized"})
            return

        content_length = int(self.headers.get("Content-Length", "0"))
        raw_body = self.rfile.read(content_length)
        try:
            payload = json.loads(raw_body.decode("utf-8"))
        except json.JSONDecodeError:
            _json_response(self, 400, {"result": "error", "error": "invalid json"})
            return

        if not isinstance(payload, dict):
            _json_response(self, 400, {"result": "error", "error": "json body must be an object"})
            return

        process_overland_payload(payload, location_path=self.storage_path)
        _json_response(self, 200, {"result": "ok"})

    def log_message(self, format: str, *args: Any) -> None:  # noqa: A003 - inherited API
        message = format % args
        print(f"[{self.log_date_time_string()}] {self.client_address[0]} {message}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Serve the Overland location webhook.")
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--route", default=DEFAULT_ROUTE)
    parser.add_argument("--storage-path", type=Path, default=DEFAULT_LOCATION_PATH)
    parser.add_argument("--token-file", type=Path, default=DEFAULT_TOKEN_PATH)
    return parser


def run_server(host: str, port: int, route: str, storage_path: Path, token_file: Path) -> None:
    handler = type(
        "ConfiguredOverlandWebhookHandler",
        (OverlandWebhookHandler,),
        {"route": route, "storage_path": storage_path, "token": _load_token(token_file)},
    )
    server = ThreadingHTTPServer((host, port), handler)
    print(f"Serving Overland webhook on http://{host}:{port}{route}")
    print(f"Writing current location to {storage_path}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    run_server(args.host, args.port, args.route, args.storage_path, args.token_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
