
import vtk
from scipy.spatial import Delaunay
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
from kneed import KneeLocator
import numpy as np

from matplotlib import pyplot as plt
from sklearn.neighbors import NearestNeighbors
import pandas as pd

df = pd.read_csv("./centroids_and_such.csv")



dataset = df[["ObjectCentroids_0","ObjectCentroids_1","ObjectCentroids_2"]]

neighbors = NearestNeighbors(n_neighbors=20)
neighbors_fit = neighbors.fit(dataset)
distances, indices = neighbors_fit.kneighbors(dataset)






## Ben's code

neighbors = NearestNeighbors(n_neighbors=20)
neighbors_fit = neighbors.fit(dataset)
distances, indices = neighbors_fit.kneighbors(dataset)
sorted_dists = sorted(distances[:,1])[:len(distances)//1]
plt.plot(sorted_dists)

# Find epsilon
eps = KneeLocator(range(len(sorted_dists)), sorted_dists, curve='convex', direction='increasing').knee
plt.vlines(eps, 0, max(sorted_dists), linestyles='dashed')
# Cluster
clustering = DBSCAN(eps=eps, min_samples=40).fit(dataset)
labeled_dataset = dataset.copy()
labeled_dataset['labels'] = clustering.labels_


df["labels"] = labeled_dataset["labels"]

df.to_csv("centroids_and_such_labeled.csv",index=False)







big_tri = Delaunay(dataset)




points = vtk.vtkPoints()
for point in dataset.to_numpy():
    points.InsertNextPoint(point)
    


# now the lines
line = vtk.vtkCellArray()
line.Allocate(points.GetNumberOfPoints())
for group in big_tri.simplices:
    pairs = [[group[i],group[(i+1)%4]] for i in range(4)]
    for pair in pairs:
        line.InsertNextCell(2,pair)

polydata = vtk.vtkPolyData()
polydata.SetPoints(points)

polydata.SetLines(line)

writer = vtk.vtkXMLPolyDataWriter()

writer.SetFileName("test_dl_network.vtp")
writer.SetInputData(polydata)
writer.Write()


