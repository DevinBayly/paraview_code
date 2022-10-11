from paraview.simple import *
kf = CameraKeyFrame()
anim = GetAnimationScene()
kf.KeyTime = anim.AnimationTime/anim.EndTime
print(kf.KeyTime)
rv = GetActiveViewOrCreate("RenderView")
print(rv)
campos = rv.CameraPosition
camfoc = rv.CameraFocalPoint
up = rv.CameraViewUp


kf.Position = campos
kf.FocalPoint = camfoc
kf.ViewUp =up
print(campos,camfoc)
pscale = rv.CameraParallelScale
# typically the camera will have been added after the default one
# todo figure out a better way to select by name Camera
cue = GetCameraTrack(view = rv)
print(cue)
cue.KeyFrames.append(kf)
print("appended frame")
