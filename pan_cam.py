import numpy as np
from paraview.simple import *

num = 4
rv = GetActiveView()
cen = np.array(rv.CenterOfRotation)
# this code ensures that we take the existing camera direction and add the rotation from there. Otherwise we don't get control over what is shown in each panel
cam = GetActiveCamera()
print(cam.GetFocalPoint())
fp = cam.GetFocalPoint()
mag = np.linalg.norm(np.array(fp[:2]))
print("magnitude is",mag)
print("center is",cen)
norm = np.array(fp[:2])/mag
print("normalized is",norm)
st_theta = np.arctan(norm[1]/norm[0])
print("starting theta is",st_theta)
#cam.SetPosition(cen + np.array([0,0,3]))
#print(cen)
#print(cam.GetPosition())
for i in range(num):
    theta = i/num*2*np.pi+ st_theta
    fp = np.array([np.cos(theta),np.sin(theta),0])+ cen
    cam.SetFocalPoint(fp.tolist())
    Render()
    SaveScreenshot(f'/home/yara/Downloads/rotation_test{i}.png', rv, ImageResolution=[1920,1080],
        FontScaling='Scale fonts proportionally',
        OverrideColorPalette='',
        StereoMode='No change',
        TransparentBackground=0, 
        # PNG options
        CompressionLevel='5',
        MetaData=['Application', 'ParaView'])
