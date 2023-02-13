from paraview.simple import *

anim = GetAnimationScene()
renderView1 = GetActiveViewOrCreate("RenderView")
cameraAnimationCue1 = CameraAnimationCue()
#cameraAnimationCue1 = GetCameraTrack(view=rv)
cameraAnimationCue1.Mode = 'Path-based'
cameraAnimationCue1.AnimatedProxy = renderView1
# create a new key frame
n = 3 
for i in range(n):
    keyFrameN = CameraKeyFrame()
    keyFrameN.Position = [-6.6921304299024635, 0.0, 0.0]
    keyFrameN.FocalPoint = [1e-20, 0.0, 0.0]
    keyFrameN.ViewUp = [0.0, 0.0, 1.0]
    keyFrameN.ParallelScale = 1.7320508075688772
    keyFrameN.PositionPathPoints = [0.0, -5.0, 0.0, 2.938926261462365, -4.045084971874736, 0.0, 4.755282581475766, -1.545084971874737, 0.0, 4.755282581475766, 1.5450849718747361, 0.0, 2.938926261462365, 4.045084971874735, 0.0, 1.3322676295501878e-15, 4.9999999999999964, 0.0, -2.9389262614623624, 4.045084971874735, 0.0, -4.755282581475763, 1.5450849718747368, 0.0, -4.755282581475763, -1.5450849718747341, 0.0, -2.9389262614623632, -4.045084971874731, 0.0]
    keyFrameN.FocalPathPoints = [0.0, 0.0, 0.0]
    keyFrameN.ClosedPositionPath = 1 
    keyFrameN.KeyTime = i/n 
    cameraAnimationCue1.KeyFrames.append(keyFrameN)



# ending scale
keyFrame9333 = CameraKeyFrame()
keyFrame9333.KeyTime = 1.0 
keyFrame9333.Position = [-6.6921304299024635, 0.0, 0.0]
keyFrame9333.FocalPoint = [1e-20, 0.0, 0.0]
keyFrame9333.ViewUp = [0.0, 0.0, 1.0]
keyFrame9333.ParallelScale = 1.7320508075688772


# initialize the animation track
cameraAnimationCue1.KeyFrames.append( keyFrame9333)
anim.Cues.append(cameraAnimationCue1)
