import numpy as np
from paraview.simple import *

num = 5
rv = GetActiveView()
cen = np.array(rv.CenterOfRotation)
cam = GetActiveCamera()
cam.SetPosition(cen + np.array([0,0,3]))
print(cen)
print(cam.GetPosition())
for i in range(num):
    theta = i/num*2*np.pi
    fp = np.array([np.cos(theta),np.sin(theta),3])+ cen
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
