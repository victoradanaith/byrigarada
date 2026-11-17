# RigaRada

Mobile-first Fan Arc tarot picker with the complete 78-card Modern Doodle Tarot deck.
Choose 1, 3 or 10 face-down cards, review or undo your picks, then confirm to reveal the artwork.
The 10-card draw labels picks Card 1–10 in order and reveals them as a Celtic Cross. All ten cards share one size and fit the available viewport. Tap a position for a larger image, its label and Previous/Next navigation. Short screens use numbered thumbnails.
Swiping browses without selecting. Previous/Next buttons and keyboard controls are available.

## Run locally

No build step or external dependencies. Serve the repository with `python3 -m http.server`
and visit `/prototypes/rigarada-mobile-fan-v2.html`.
Keep `assets/tarot/` alongside `prototypes/` when copying the site.

## Artwork

78 approved illustrations: 22 Major Arcana and 14 cards in each of Wands, Cups, Swords and Pentacles.
XII uses the approved handstand reinterpretation. The final thin-margin crops are preserved
in proportional JPEG web derivatives (long edge 900 px, quality 88); full-resolution originals
remain outside this repository. `assets/tarot/deck.json` maps stable card IDs, names and paths.
Artwork requests start only after reveal confirmation. A readable named fallback appears if
an image fails to load; the selected draw remains unchanged.

See [the handoff](docs/FAN_ARC_HANDOFF.md) for interaction details and testing limitations.

## Smith Waite tarot (`smith-waite/`)

The same picker with the 78 cards of the original 1909 Rider–Waite–Smith printing (art by Pamela Colman Smith), public-domain scans from Wikimedia Commons; see `assets/smith-waite/SOURCES.md` and `sources.json` for every file's source page, licence and SHA-1. An option switches between upright cards only (หัวตั้งล้วน) and upright mixed with reversed (หัวตั้งผสมกลับหัว); in mixed mode each card has an even chance of being reversed when the reading is revealed, and reversed cards are shown rotated and labelled กลับหัว. These are not U.S. Games Systems' Centennial scans.
