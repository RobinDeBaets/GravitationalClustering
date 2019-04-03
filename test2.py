# Grid of 100x100
# 3 circles of 15x15 with each 10 points
import testgenerator
from clusterer import Clusterer
from clustervisualizer import ClusterVisualizer

points = testgenerator.create_circle_points(1000, 50, 50, 20, point_mass=10)
clusterer = Clusterer(5, 10, 2)
clustervisualizer = ClusterVisualizer(clusterer)
clusterer.set_points(points)
clusterer.run()

