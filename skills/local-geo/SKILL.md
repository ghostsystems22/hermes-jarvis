---
name: local-geo
description: Use when you need an Overland-compatible location webhook or to read the latest stored GPS fix from the local JSON file. It serves POST /webhooks/overland, writes the newest point to current_location.json, and exposes get_current_location() with stale-location warnings.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [gps, overland, webhook, geojson, location]
    related_skills: [hermes-agent-skill-authoring]
---

# Local Geo

## Overview

Use this skill for a small, self-hosted location ingestion helper that accepts Overland's standard POST payload and stores the last received point on disk. The helper is intentionally simple: one HTTP endpoint, one JSON file, one read function.

Default storage file:

`~/.hermes/skills/local-geo/current_location.json`

Default endpoint:

`POST /webhooks/overland`

Authentication:

- Every POST must include `Authorization: Bearer <token>`
- The token is stored in `~/.hermes/skills/local-geo/token.txt` (or injected via `LOCAL_GEO_TOKEN` / `LOCAL_GEO_TOKEN_FILE`)

## When to Use

- You need to receive Overland location updates on a VPS or personal server
- You need a quick JSON file that always contains the latest known position
- You need a `get_current_location()` helper for other Hermes workflows
- You want stale-position detection without rejecting the value entirely

Don't use this for:

- Historical trip analytics
- Database-backed telemetry pipelines
- Multi-device tracking with account management

## Payload Contract

The webhook accepts JSON bodies where `locations` contains GeoJSON point features. Supported shapes:

- `{"locations": [<Feature>, ...]}`
- `{"locations": {"type": "FeatureCollection", "features": [<Feature>, ...]}}`
- `{"locations": {<Feature>}}`

Each feature must have:

- `geometry.type == "Point"`
- `geometry.coordinates == [lon, lat]`
- `properties.timestamp`

The helper stores the last valid point found in the request.

## Behavior

- On every valid POST, write the newest point to `current_location.json`
- Respond with `{"result":"ok"}`
- `get_current_location()` returns `lat`, `lon`, and `timestamp`
- If the timestamp is older than 3 hours, return the same data plus:
  - `warning: "position possiblement périmée"`

## Files

- `scripts/local_geo.py` — HTTP server + storage helper

## Verification Checklist

- [ ] POSTing an Overland payload returns `{"result":"ok"}`
- [ ] The latest feature is written to `current_location.json`
- [ ] `get_current_location()` returns lat/lon/timestamp
- [ ] Stale points still return data with the warning string
- [ ] The skill lives under `~/.hermes/skills/local-geo/`
