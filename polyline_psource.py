## programmable source code for a polyline, based on https://examples.vtk.org/site/Python/GeometricObjects/PolyLine/
from vtkmodules.vtkCommonDataModel import vtkCellArray,vtkPolyData,vtkPolyLine
from vtkmodules.vtkCommonCore import vtkPoints
print(vtkCellArray)

origin = [0.0, 0.0, 0.0]
p0 = [1.0, 0.0, 0.0]
p1 = [0.0, 1.0, 0.0]
p2 = [0.0, 1.0, 2.0]
p3 = [1.0, 2.0, 3.0]

points = vtkPoints()
points.InsertNextPoint(origin)
points.InsertNextPoint(p0)
points.InsertNextPoint(p1)
points.InsertNextPoint(p2)
points.InsertNextPoint(p3)
polyline = vtkPolyLine()
polyline.GetPointIds().SetNumberOfIds(5)
for i in range(5):
  polyline.GetPointIds().SetId(i,i)

print(polyline)

cells = vtkCellArray()
cells.InsertNextCell(polyline)
print(cells)

output.SetPoints(points)
output.SetLines(cells)
print(dir(output))
