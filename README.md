# RigaRada

Mobile-first card-reading prototype. This repository currently holds one standalone
prototype: the **Fan Arc v2** card-selection flow.

## Purpose

Explore a touch-friendly way to pick 1 or 3 face-down cards from a deck of 22, then
confirm and reveal them. Most users are expected to be on mobile, so the fan arc
(swipe to browse, tap or press Select to choose) is the preferred primary flow.

All card faces are neutral placeholders ("Card 01" … "Card 22", "Artwork TBD").
Final artwork is a separate workstream and is not part of this repository yet.

## Run locally

The prototype is a single self-contained HTML file with no build step, no framework and
no external dependencies.

- Open `prototypes/rigarada-mobile-fan-v2.html` directly in a browser, or
- serve the folder with any static server, e.g. `python3 -m http.server` from the
  repository root, then visit `/prototypes/rigarada-mobile-fan-v2.html`.

For a realistic view, use a phone or your browser's device emulation at about
375×812 or 390×844.

## Layout

```
README.md
docs/FAN_ARC_HANDOFF.md                 design decisions, evidence, next steps
prototypes/rigarada-mobile-fan-v2.html  the prototype
```

See [docs/FAN_ARC_HANDOFF.md](docs/FAN_ARC_HANDOFF.md) for the design rationale and
what has and has not been tested.
