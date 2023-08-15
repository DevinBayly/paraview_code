## contents of this would go in a programmable filter undernearth the step that uses Compute Connected surface properties

import numpy as np
i = inputs[0]

#print(dir(i))
df = i.FieldData
#print(df[0])
#print(df.VTKObject)
volumeArray = df.VTKObject.GetAbstractArray(2)
#print(dir(volumeArray))
#print(volumeArray.GetTuple(0))
cells = i.CellData
cellkeys = cells.keys()
#print(cellkeys)
ids = cells["ObjectIds"]

obj_volumes = []
#print(obj_volumes)
for i,id in enumerate(ids[:]):
  vol= volumeArray.GetTuple(id)[0]
  #print(vol)
  obj_volumes.append(vol)

#print(obj_volumes)
obj_volumes = np.array(obj_volumes)
output.CellData.append(obj_volumes,"ObjectVolumes")
output.CellData.append(ids,"ObjectIds")
