def GetUpdateTimestep(algorithm):
    """Returns the requested time value, or None if not present"""
    executive = algorithm.GetExecutive()
    outInfo = executive.GetOutputInformation(0)
    return outInfo.Get(executive.UPDATE_TIME_STEP()) \
              if outInfo.Has(executive.UPDATE_TIME_STEP()) else None

# This is the requested time-step. This may not be exactly equal to the
# timesteps published in RequestInformation(). Your code must handle that
# correctly.
req_time = int(GetUpdateTimestep(self))
#print(req_time)
from pathlib import Path
import numpy as np

from vtk.numpy_interface import algorithms as algs
from vtk.numpy_interface import dataset_adapter as dsa
def srtkey(a):
    return str(a)
pth = Path("/xdisk/chrisreidy/baylyd/Sama_lidar/temp/babel_pcl")
npy_pcls = sorted(list(Path(pth).rglob("*.npy")),key=srtkey)

npy_pcl =  npy_pcls[req_time]
all_data = np.load(npy_pcl)
data = all_data[:,:3]
intensity = all_data[:,3]
#print(data)


# make vtk points
pts = vtk.vtkPoints()
pts.SetData(dsa.numpyTovtkDataArray(data,"Points"))

output.SetPoints(pts)
#make single cell
numpts = pts.GetNumberOfPoints()
ids = vtk.vtkIdList()
ids.SetNumberOfIds(numpts)
for a in range(numpts):
    ids.SetId(a,a)

output.Allocate(1)
output.InsertNextCell(vtk.VTK_POLY_VERTEX,ids)
#add scalar data to output
output.PointData.append(intensity,"intensity")
