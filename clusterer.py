from math import sqrt
import numpy
from tqdm import tqdm

class Clusterer:
    def __init__(self, delta, epsilon, dimension):
        self.delta = delta
        self.epsilon = epsilon
        self.dimension = dimension
        self.points = None
        self.listeners = []

    def set_points(self, points):
        self.points = points.copy()
        for listener in self.listeners:
            listener.on_set_points()
        # TODO calculate approximate delta based on given points

    def run(self):
        # Unit attraction Markovian model
        def g(p1, p2):
            point_distance = p1.distance_to(p2)
            return (1 / p1.mass) * 1 / (point_distance ** 2)

        # def g(p1, p2):
        #     point_distance = p1.distance_to(p2)
        #     return sqrt(p1.mass * p2.mass) * (1 / p1.mass) * 1 / (point_distance ** 2)

        frame = 0
        while 1 < len(self.points):
            movements = numpy.zeros((len(self.points), self.dimension))
            max_distance = 0
            for i in tqdm(range(len(self.points)), ncols=120):
                point = self.points[i]
                for j in range(len(self.points)):
                    if i != j:
                        other_point = self.points[j]
                        scalar = g(point, other_point)
                        new_vector = numpy.subtract(other_point.loc, point.loc)
                        new_vector = numpy.multiply(new_vector, scalar / numpy.linalg.norm(new_vector))
                        movements[i] = numpy.add(movements[i], new_vector)
                distance = numpy.linalg.norm(movements[i])
                max_distance = max(max_distance, distance)
            #     delta = (dt ** 2) * distance
            # <=> dt = sqrt(delta / distance)
            dt = sqrt(self.delta / max_distance)
            dt_squared = dt ** 2
            movements = numpy.multiply(movements, dt_squared)
            for i in range(len(self.points)):
                self.points[i].loc = numpy.add(self.points[i].loc, movements[i])
            i = 0
            while i < len(self.points) - 1:
                point = self.points[i]
                y = i + 1
                while y < len(self.points):
                    other_point = self.points[y]
                    distance = numpy.linalg.norm(numpy.subtract(point.loc, other_point.loc))
                    if distance <= self.epsilon:
                        point.mass += other_point.mass
                        point.loc = numpy.mean([point.loc, other_point.loc], axis=0)
                        del self.points[y]
                    else:
                        y += 1
                i += 1
            frame += 1
            for listener in self.listeners:
                listener.on_update_points()
        for listener in self.listeners:
            listener.on_finish()

    def add_listener(self, listener):
        self.listeners.append(listener)
