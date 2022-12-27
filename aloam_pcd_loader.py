

def GetUpdateTimestep(algorithm):
    """Returns the requested time value, or None if not present"""
    executive = algorithm.GetExecutive()
    outInfo = executive.GetOutputInformation(0)
    return outInfo.Get(executive.UPDATE_TIME_STEP()) \
              if outInfo.Has(executive.UPDATE_TIME_STEP()) else None
def makepcloud(pcd_name):
    with open(pcd_name,"rb") as phile:
        line = phile.readline()
        header = []
        while not b"DATA" in line:
            line = phile.readline()
            print(line)
            header.append(line)
        buf = phile.read()
    parts = [[e for e in d.decode().strip().split(" ")[1:]] for d in header[1:] ]
    parts = [p for p in parts if len(p) >0]
    parts
    print("parts are",parts)
    collection = []
    for attri,e in enumerate(parts[3]):
        print("e is ",e)
        for i in range(int(e)):
            name = parts[0][attri]
            if name =="_":
                name+=str(i)+str(attri)
            unit = (parts[2][attri]+parts[1][attri]).lower()
            collection.append((name,unit))
    d = np.dtype(collection)
    byte_amt = d.itemsize
    print(byte_amt)
    points = int(parts[4][0])
    print(points)
    arr = np.frombuffer(buf[:byte_amt*points],dtype=d)
    return arr

# This is the requested time-step. This may not be exactly equal to the
# timesteps published in RequestInformation(). Your code must handle that
# correctly.
req_time = int(GetUpdateTimestep(self))
#print(req_time)
from pathlib import Path
import numpy as np

from vtk.numpy_interface import algorithms as algs
from vtk.numpy_interface import dataset_adapter as dsa

pth = Path("/home/yara/Downloads/135.694091710.pcd")
arr = makepcloud(pth)
all_data = arr
## this will be in the format of a named numpy array with things like x y z intensity and reflectivity

data = np.column_stack([all_data["x"],all_data["y"],all_data["z"]])
intensity = all_data["intensity"]
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
