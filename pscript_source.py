def GetUpdateTimestep(algorithm):
    """Returns the requested time value, or None if not present"""
    executive = algorithm.GetExecutive()
    outInfo = executive.GetOutputInformation(0)
    return outInfo.Get(executive.UPDATE_TIME_STEP()) \
              if outInfo.Has(executive.UPDATE_TIME_STEP()) else None

# This is the requested time-step. This may not be exactly equal to the
# timesteps published in RequestInformation(). Your code must handle that
# correctly.
req_time = GetUpdateTimestep(self)
#print(req_time)
from pathlib import Path
import numpy as np

from vtk.numpy_interface import algorithms as algs
from vtk.numpy_interface import dataset_adapter as dsa
pth = Path.home()/"Downloads/lidar_data"
npy_pcls = list(Path(pth).rglob("*.npy"))
npy_pcl = [npy for npy in npy_pcls if req_time == float(f"{npy.stem}")][0]
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
