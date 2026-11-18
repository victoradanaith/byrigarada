import glob, sys, numpy as np
from PIL import Image
W,H=620,1080; PAD=16
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
    return top,bot,lef,rig
res=[]
for f in sorted(glob.glob(sys.argv[1]+'/*/*.jpg')):
    im=Image.open(f).convert('RGB'); a=np.asarray(im).astype(float)
    t,b,l,r=frame(a.mean(2))
    res.append((f.split('/')[-1],t,b,l,r,im.size))
    if None in (t,b,l,r): print('NOFRAME',f,t,b,l,r); continue
    c=a[t:b+1,l:r+1]
    # neutralise paper tint: map each channel's 99th percentile to 248
    p=np.percentile(c.reshape(-1,3),99,axis=0)
    c=np.clip(c*(248/p),0,255)
    out=Image.fromarray(c.astype('uint8')).resize((W-2*PAD,H-2*PAD),Image.LANCZOS)
    card=Image.new('RGB',(W,H),(250,249,246)); card.paste(out,(PAD,PAD))
    if len(sys.argv)>2: card.save(f.replace(sys.argv[1],sys.argv[2]),quality=88,optimize=True)
asp=[(r-l)/(b-t) for _,t,b,l,r,_ in res if None not in (t,b,l,r)]
[print(x,round((x[4]-x[3])/(x[2]-x[1]),3)) for x in res if None not in x[1:5] and not .55<(x[4]-x[3])/(x[2]-x[1])<.6]
print(len(res),'aspect min/max',round(min(asp),3),round(max(asp),3))
