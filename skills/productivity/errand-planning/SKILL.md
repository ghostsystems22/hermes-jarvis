---
name: errand-planning
description: Plan errands like grocery runs by combining calendar availability, travel time, store hours, and shopping lists from sheets.
version: 1.0.0
author: Nous Research
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [calendar, shopping, errands, logistics, planning, maps, sheets]
---

# Errand Planning

Use this skill when the user wants to fit an errand into their day: grocery shopping, a supply run, pickup/dropoff, or any task that depends on *where* they are, *when* they’re free, and *what* they need to buy.

## Triggers
- "Best time to go shopping"
- "Fit this errand around my calendar"
- "Plan a grocery run"
- "How long will this take?"
- "What can I buy at X store based on my sheet?"

## Core workflow
1. **Pull the list of things needed.**
   - Prefer a spreadsheet or checklist as the source of truth.
   - If the source is a Google Drive `.xlsx`, download it and parse locally.
   - If it is a native Google Sheet, read the relevant range directly.
2. **Estimate errand duration.**
   - Separate travel time from in-store time.
   - Use list size and store type to estimate how long the shopping itself will take.
3. **Check the calendar.**
   - Look for a *continuous* free block long enough for travel + shopping + return.
   - Use the user's local timezone.
4. **Check practical constraints.**
   - Store hours.
   - Whether the store is on the way or requires a dedicated trip.
   - Whether the user is carrying groceries back themselves.
5. **Recommend the best slot.**
   - Choose the earliest realistic block that fits.
   - If nothing fits, say so plainly and suggest another day or delivery.

## Time heuristics
- Small top-up: 20–30 min in store
- Normal grocery run: 35–50 min in store
- Wholesale / stock-up run: 45–75 min in store
- Add commute both ways unless the store is walkable from the user's location

## Good output format
- A short recommendation first
- Then a compact table:
  - travel time
  - shopping time
  - total time
  - suggested slot
  - reasons

## Pitfalls
- Don't assume calendar gaps are usable unless they are long enough for the *full* round trip.
- Don't recommend a time outside store opening hours.
- If the user says a suggestion is closed/unavailable, re-evaluate before repeating it.
- Don't overfit to one store: the same logic should work for supermarkets, pharmacies, hardware stores, and bulk shops.

## Verification
- Confirm the required items were actually extracted from the sheet/list.
- Confirm the chosen slot is long enough after adding travel time.
- Confirm store hours support the recommendation.

## References
- `references/grocery-run-example.md` — Makro Phuket / The Base Central example from a real session.
