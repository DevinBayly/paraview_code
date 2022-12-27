
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

pth = Path("~/Downloads/adjusted.npy")
all_data = np.load(pth)
## this will be in the format of a named numpy array with things like x y z intensity and reflectivity

data = np.column_stack([all_data["x"],all_data["y"],all_data["z"]])
intensity = all_data["intensity"]
reflectivity = all_data["reflectivity"]
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
output.PointData.append(reflectivity,"reflectivity")
