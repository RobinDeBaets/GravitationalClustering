from math import sqrt


class Particle:
    def __init__(self, mass, loc, uuid):
        self.mass = mass
        self.loc = loc
        self.uuid = uuid

    def distance_to(self, other):
        return sqrt(sum((self.loc[i] - other.loc[i]) ** 2 for i in range(len(self.loc))))
