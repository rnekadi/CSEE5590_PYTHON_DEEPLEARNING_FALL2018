# import matplotlib for plotting the clusters
import matplotlib.pyplot as plt

# import numpy library
import numpy as np

# from sklearn import kmeans

from sklearn.cluster import KMeans


# Create X array using Numpy

x = np.array([1.0, 1.5, 3.0, 5.0, 3.5, 4.5])

# use uniform function to get the float values within range(60,80)

y = np.array([1.0, 2.0, 4.0, 7.0, 5.0, 5.0])

# numpy function vstack to stack the two arrays vertically

X = np.vstack((x, y)).T

# print the 2d array
print(X)

# define the model and pass in number of clusters

kmeans = KMeans(n_clusters=2)

# fit the model to the array X
kmeans.fit(X)

# Scatter plot the datapoints with different colors assigned to various clusters
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='rainbow')

# Scatter plot the centroids with black color
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black')

# show the plot using matplotlib package
plt.show()
