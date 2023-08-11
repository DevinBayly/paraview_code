## programmable source code for a polyline, based on https://examples.vtk.org/site/Python/GeometricObjects/PolyLine/
from vtkmodules.vtkCommonDataModel import vtkCellArray,vtkPolyData,vtkPolyLine
from vtkmodules.vtkCommonCore import vtkPoints
import numpy as np
print(vtkCellArray)

origin = [0.0, 0.0, 0.0]
p0 = [1.0, 0.0, 0.0]
p1 = [0.0, 1.0, 0.0]
p2 = [0.0, 1.0, 2.0]
p3 = [1.0, 2.0, 3.0]

points = vtkPoints()
rands = np.random.random((200,3))
for row in rands[:]:
  points.InsertNextPoint(list(row))

print(points)

polyline = vtkPolyLine()
polyline.GetPointIds().SetNumberOfIds(rands.shape[0])
for i in range(rands.shape[0]):
  polyline.GetPointIds().SetId(i,i)

print(polyline)

cells = vtkCellArray()
cells.InsertNextCell(polyline)
print(cells)

output.SetPoints(points)
output.SetLines(cells)
print(dir(output))
