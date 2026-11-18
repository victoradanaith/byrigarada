import glob, sys, numpy as np
from PIL import Image
W,H=600,1080; PAD=0
def frame(g):
    d=(g<110)
    h,w=d.shape
    def scan(fr, axis, rng):
        for i in rng:
            lo,hi=max(0,i-3),i+4
            band = d[lo:hi,:].any(0) if axis==0 else d[:,lo:hi].any(1)
            core = band[int(len(band)*.15):int(len(band)*.85)]
            if core.mean()>fr: return i
        return None
    top=scan(.6,0,range(0,int(h*.12))); bot=scan(.6,0,range(h-1,int(h*.88),-1))
    lef=scan(.6,1,range(0,int(w*.15))); rig=scan(.6,1,range(w-1,int(w*.85),-1))
    def snap(i,axis,sign):
        # move to the darkest line within 14px inward, so no paper is left outside the black frame
        if i is None: return None
        best=i;bv=1e9
        for j in range(i,i+sign*14,sign):
            if not (0<=j<(h if axis==0 else w)): break
            line=g[j,int(w*.15):int(w*.85)] if axis==0 else g[int(h*.15):int(h*.85),j]
            v=line.mean()
            if v<bv: bv=v;best=j
        return best
    return snap(top,0,1),snap(bot,0,-1),snap(lef,1,1),snap(rig,1,-1)
res=[]
for f in sorted(glob.glob(sys.argv[1]+'/*/*.jpg')):
    im=Image.open(f).convert('RGB'); a=np.asarray(im).astype(float)
    t,b,l,r=frame(a.mean(2))
    res.append((f.split('/')[-1],t,b,l,r,im.size))
    if None in (t,b,l,r): print('NOFRAME',f,t,b,l,r); continue
    k=6  # trim inside the frame so worn paper corners don't show
    c=a[t+k:b+1-k,l+k:r+1-k]
    # neutralise paper tint: map each channel's 99th percentile to 248
    p=np.percentile(c.reshape(-1,3),99,axis=0)
    c=np.clip(c*(248/p),0,255)
    out=Image.fromarray(c.astype('uint8')).resize((W-2*PAD,H-2*PAD),Image.LANCZOS)
    card=Image.new('RGB',(W,H),(250,249,246)); card.paste(out,(PAD,PAD))
    if len(sys.argv)>2: card.save(f.replace(sys.argv[1],sys.argv[2]),quality=88,optimize=True)
asp=[(r-l)/(b-t) for _,t,b,l,r,_ in res if None not in (t,b,l,r)]
[print(x,round((x[4]-x[3])/(x[2]-x[1]),3)) for x in res if None not in x[1:5] and not .55<(x[4]-x[3])/(x[2]-x[1])<.6]
print(len(res),'aspect min/max',round(min(asp),3),round(max(asp),3))
