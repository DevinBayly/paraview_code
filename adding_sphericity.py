## contents of this would go in a programmable filter undernearth the step that uses Compute Connected surface properties

import numpy as np
i = inputs[0]


## here read from a csv, that has the same number of rows as there are object ids
## this will include sphericity values and object volumes
cells = i.CellData
cellkeys = cells.keys()
#print(cellkeys)
ids = cells["ObjectIds"]


### now you have to loop through all the cells, and in each loop you need to index 2 values from your imported csv

##now instead of one obj volumes list
## need to make a sphericity list too
obj_volumes = []
#print(obj_volumes)
for i,id in enumerate(ids[:]):
  ## here's where we index a vol and sphere value
  #print(vol)
  ## now we have to append to our lists
  obj_volumes.append(vol)

#print(obj_volumes)
# now make a numpy array from both the volumes list and the sphere one
obj_volumes = np.array(obj_volumes)
## now we append the arrays the same way with the correct name
output.CellData.append(obj_volumes,"ObjectVolumes")
output.CellData.append(ids,"ObjectIds")
