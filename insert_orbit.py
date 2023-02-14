from paraview.simple import *

anim = GetAnimationScene()

renderView1 = GetActiveViewOrCreate("RenderView")
cameraAnimationCue1 = CameraAnimationCue()
#cameraAnimationCue1 = GetCameraTrack(view=rv)
cameraAnimationCue1.Mode = 'Path-based'
cameraAnimationCue1.AnimatedProxy = renderView1
# create a new key frame
s = GetActiveSource()
d = s.GetDataInformation()
n = d.DataInformation.GetNumberOfTimeSteps()
# if we decide that we want a certain number of frames per revolution we should multiple the number of plants by that amount and set that as the animations number of frames
# logic is that if we have a person watching for about a minute (600 frames at 10fps) and we have n orbits to complete then we will need to move at a different number of frames
total_seconds = 30
target_fps = 10
frames_per_orbit  = ((total_seconds*target_fps)//n)+1
anim.NumberOfFrames = (total_seconds*target_fps)
## if we do more orbits then I think people will get dizzy
orbits = 3
for i in range(orbits):
    keyFrameN = CameraKeyFrame()
    keyFrameN.Position = [-6.6921304299024635, 0.0, 0.0]
    keyFrameN.FocalPoint = [1e-20, 0.0, 0.0]
    keyFrameN.ViewUp = [0.0, 0.0, 1.0]
    keyFrameN.ParallelScale = 1.7320508075688772
    keyFrameN.PositionPathPoints = [-0.027969280712061628, -0.5221370489856471, 0.5202375330914683, 0.27053340707321527, -0.42514764634574914, 0.5202375330914683, 0.4550182138577148, -0.17122609368594643, 0.5202375330914683, 0.4550182138577148, 0.14263820635386187, 0.5202375330914683, 0.27053340707321527, 0.39655975901366425, 0.5202375330914683, -0.027969280712061496, 0.4935491616535621, 0.5202375330914683, -0.32647196849733834, 0.39655975901366425, 0.5202375330914683, -0.5109567752818371, 0.142638206353862, 0.5202375330914683, -0.5109567752818371, -0.17122609368594618, 0.5202375330914683, -0.3264719684973385, -0.4251476463457486, 0.5202375330914683]
    keyFrameN.FocalPathPoints = [0.0, 0.0, 0.0]
    keyFrameN.ClosedPositionPath = 1 
# can't use normalized time here because the ply reader sets the model changes in index time
    keyFrameN.KeyTime = i/orbits 
    print(i/orbits,"time")
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
