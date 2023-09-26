## contents of this would go in a programmable filter undernearth the step that uses Compute Connected surface properties

import numpy as np
import pandas as pd
from pathlib import Path
i = inputs[0]
df = pd.read_csv(Path.home()/"Downloads/for_andy_to_import.csv")
new_column_array = df["new_column"]
print(new_column_array)
#print(dir(volumeArray))
#print(volumeArray.GetTuple(0))
cells = i.CellData
cellkeys = cells.keys()
#print(cellkeys)
ids = cells["ObjectIds"]

obj_volumes = []
#print(obj_volumes)
for i,id in enumerate(ids[:]):
  customdata= new_column_array[id]
  #print(vol)
  obj_volumes.append(customdata)

#print(obj_volumes)
obj_volumes = np.array(obj_volumes)
print(obj_volumes)
output.CellData.append(obj_volumes,"customdata")
#output.CellData.append(ids,"ObjectIds")
