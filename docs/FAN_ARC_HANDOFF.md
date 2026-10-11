# Fan Arc v2 — handoff

Prototype: `prototypes/rigarada-mobile-fan-v2.html` (standalone HTML/CSS/JS, no dependencies).
This migration copies the prototype as-is. No redesign and no framework conversion.

## Design decisions

- **Mobile first.** Most users will be on mobile. Fan Arc is the preferred primary flow.
- **Browsing.** Horizontal swipe/drag moves through the fan. Vertical gestures are left to page scroll.
- **Focus.** The center card is enlarged, raised and highlighted, with a clear
  position label for the face-down card ("Card N of M").
- **Swiping never selects.** Any movement beyond a small slop threshold is a drag; the
  trailing click is suppressed.
- **Tap rules.** Tapping a side card only focuses it. Tapping the focused card, or the
  explicit **Select** button, selects it.
- **Reading size.** 1 or 3 cards. Selected count, remaining count and deck size are always shown.
- **No duplicate draws.** Chosen cards leave the fan; selection is guarded against duplicates.
- **Undo / deselect.** Undo history, and tapping a chosen card in the tray returns it to the deck.
- **Separate confirmation.** Reveal opens a confirmation dialog ("Go back" keeps picks editable).
- **Alternatives to gestures.** Previous/Next buttons; keyboard (arrows, Home/End,
  PageUp/PageDown, Enter/Space, Ctrl/Cmd+Z); horizontal wheel.
- **Reduced motion.** Honors `prefers-reduced-motion`, with a manual Auto / Reduce / Full override.
- **Artwork is separate.** Card backs are CSS patterns; faces are generated text
  placeholders created only at reveal, so identities never appear in the DOM before then.
  Rect/Oval card shape is a placeholder toggle.
- Extras present in the prototype: Shuffle, Cut (3 piles), dark mode via system preference.

## Evidence (read carefully)

**Inherited, reported by the earlier design session — not re-run for this migration:**
63/63 headless Chromium 141 Playwright checks at 375×812 and 390×844, covering simulated
CDP touch, vertical-vs-horizontal gestures, drag click suppression, side vs center taps,
button and keyboard use, undo, full selection, confirmation, distinct reveals, the
1-card flow and reduced motion.

**Independently observed earlier by the owner (manual, on the downloaded v2):**
no horizontal overflow at both narrow widths; mouse drag moved focus from card 12 to 18
without selecting; a centered click selected one card; Undo restored the deck;
arrows/Enter selected; the 3-card confirm and reveal showed distinct placeholders.

**Checked during this migration (static only, no browser run):**
the embedded script passes `node --check`; HTML tags are balanced; the file contains no
external URLs, `<link>`, `src`, `@import`, network calls or credentials.

**Not tested:** real iOS Safari and Android devices; VoiceOver and TalkBack.

## Transfer note

The prototype file is byte-identical to the authorized source (26,579 bytes,
SHA-256 `ce8378b6179b891f06a7b85088e4128e940e0c307f1924ee4eac888780455c56`), restored
from a base64 transfer after an earlier plain-text transfer lost its line breaks.
Verify with `sha256sum prototypes/rigarada-mobile-fan-v2.html`.

## Next steps

1. Test on real iOS Safari and Android Chrome (touch, scroll interplay, safe areas, notch).
2. Screen-reader pass with VoiceOver and TalkBack (listbox/option pattern, live announcements).
3. Decide final card artwork and shape (rect vs oval), then replace the placeholders.
4. Re-run the browser checks against this repo copy and keep them as repo tests if wanted.
5. Decide on any framework or build tooling only after the interaction model is signed off.
