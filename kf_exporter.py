from paraview.simple import *
from pathlib import Path
import json
import uuid
rv = GetActiveViewOrCreate("RenderView")
anim = GetAnimationScene()
cue = GetCameraTrack(view = rv)
kfs = cue.KeyFrames
pth = Path(Path.home()/".config/Paraview/Animation_Cues/")
pth.mkdir(exist_ok=True,parents=True)
# finding suitable name
src = GetActiveSource()
pxm = servermanager.ProxyManager()
name = pxm.GetProxyName("sources",src)
with open(f"{pth}/paraview_animation_{name}_{uuid.uuid1()}","w") as phile:
    all_kfs = []
    for kf in kfs:
        all_kfs.append([kf.KeyTime ,list(kf.Position) ,list(kf.FocalPoint) ,list(kf.ViewUp) ])
    phile.write(json.dumps(all_kfs))
