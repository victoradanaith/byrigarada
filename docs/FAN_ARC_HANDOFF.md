# Fan Arc — complete deck handoff

- The pool now contains all 78 unique cards, with stable suit/rank IDs and matching approved artwork.
- Card identities remain in the script closure until reveal. The fan and selected tray show CSS backs;
  the reveal confirmation creates the face images, accessible card names and visible captions.
- Each revealed card uses its original crop aspect ratio. Images use `object-fit: contain`.
- Selection, removal, Undo, shuffle/cut, 1/3-card reading, confirmation and new-reading flows are retained.
- Horizontal swipes never select. The tested `lostpointercapture` guard remains unchanged so child-card
  implicit capture transfer does not end a gesture early. Vertical gestures remain available to scroll.
- Replacing a reading during its reveal invalidates old animation callbacks, preventing stale artwork
  or errors when switching between 1 and 3 cards.
- An unavailable image shows its card name and a clear fallback without changing the draw.
- Assets are original generated illustrations; no external image host or credentials are used.

Real iOS/Android device checks and VoiceOver/TalkBack remain necessary. Browser automation is emulation.
