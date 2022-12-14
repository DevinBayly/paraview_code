import h5py
from pathlib import Path
import numpy as np
from vtk.numpy_interface import algorithms as algs
from vtk.numpy_interface import dataset_adapter as dsa

pth = Path.home().rglob("*position*h5")
f = h5py.File(str(pth))
keys = list(f.keys())

data = f[keys[0]][:]
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