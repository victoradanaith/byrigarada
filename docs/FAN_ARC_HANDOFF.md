# Fan Arc — complete deck handoff

- The pool now contains all 78 unique cards, with stable suit/rank IDs and matching approved artwork.
- Card identities remain in the script closure until reveal. The fan and selected tray show CSS backs;
  the reveal confirmation creates the face images, accessible card names and visible captions.
- Each revealed card uses its original crop aspect ratio. Images use `object-fit: contain`.
- Selection, removal, Undo, shuffle/cut, 1/3-card reading, confirmation and new-reading flows are retained.
- A 10-card option uses numbered Card 1–10 positions, five columns before reveal and a Celtic Cross after reveal.
  Reveal is available only with all ten picks. Positions are Present, Challenge, Foundation, Past, Goals, Near future, Self, Environment, Hopes & fears and Outcome. The second card crosses the first; cards 7–10 form the right column from bottom to top. Each card opens an accessible inspection dialog with a larger image, short position context and Previous/Next controls.
- Before reveal, switching size keeps the earliest picks and returns extras to the deck. Undo restores
  the previous size and picks. Switching during selection cancels its pending animation callback.
- Horizontal swipes never select. The tested `lostpointercapture` guard remains unchanged so child-card
  implicit capture transfer does not end a gesture early. Vertical gestures remain available to scroll.
- Replacing a reading during its reveal invalidates old animation callbacks, preventing stale artwork
  or errors when switching between 1, 3 and 10 cards.
- An unavailable image shows its card name and a clear fallback without changing the draw.
- Assets are original generated illustrations; no external image host or credentials are used.

Real iOS/Android device checks and VoiceOver/TalkBack remain necessary. Browser automation is emulation.

The local 10-card regression harness passed 223 assertions across 320, 375 and 390 px widths:
all three sizes, ordered picks, maximum selection, early-reveal prevention, Undo/reselection,
confirmation, unique IDs, actual image loading, reset, size changes during selection/reveal,
horizontal overflow and ten missing-image fallbacks. The fan gesture code is unchanged. Celtic Cross inspection and layout are also checked at desktop width.

Position numbering follows a common variant; Celtic Cross variants differ in positions 3/5 and 4/6. Reference: https://tarotelements.com/celtic-cross-tarot-spread/

## Viewport fit correction

The revealed Celtic Cross reserves space for the header, status, inspection hint and New reading control, then sizes all ten card boxes equally from the remaining area. The crossing card uses the same intrinsic dimensions, rotated 90 degrees. Source artwork remains proportional within those boxes. Short screens use position number badges and larger inspection dialogs; extra options are hidden after a ten-card reveal. Tested portrait, landscape and desktop viewports: 320×568, 375×667, 390×844, 568×320, 844×390, 1024×768, 1440×900. Physical devices and browser chrome variations remain untested.
