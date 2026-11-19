"""Second pass: cut the light strip and black rule under the title band at the bottom of each card.
Usage: python3 tools/sw_bottom.py assets/smith-waite"""
import glob, sys, numpy as np
from PIL import Image
W, H = 600, 1080
for f in sorted(glob.glob(sys.argv[1] + '/*/*.jpg')):
    im = Image.open(f).convert('RGB'); g = np.asarray(im.convert('L')).astype(float)
    h = g.shape[0]
    dark = [(g[y, 60:540] < 110).mean() for y in range(h)]
    y = h - 1
    while y > h - 120 and dark[y] <= .5: y -= 1        # up through the light strip to the rule
    r = y
    while y > r - 8 and dark[y] > .3: y -= 1           # up through the rule itself (at most 8px; art may be dark above it)
    cut = y - 1                                        # 2px inside, so no rule shows
    im.crop((0, 0, im.width, cut)).resize((W, H), Image.LANCZOS).save(f, quality=90, optimize=True)
    print(f.split('/')[-1], h - cut)
