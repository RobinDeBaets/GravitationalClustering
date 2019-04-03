import random
from math import sqrt, cos, sin, pi
from random import randint, random, uniform

from particle import Particle


def create_circle_points(grid_size, circle_count, circle_radius, circle_points, point_mass=60,
                         circle_radius_deviation=0.2,
                         circle_points_deviation=0.2):
    """
    :param grid_size: size of grid (length and height are equal)
    :param circle_count: amount of circles in the grid
    :param circle_radius: radius in which each circle will generate points
    :param circle_points: amount of points to be generated per circle
    :param point_mass: mass of each point
    :param circle_radius_deviation: deviation percentage for circle radius
    :param circle_points_deviation: deviation percentage for amount of points per circle
    :return: randomly generated points in randomly generated circles in a two dimensiona plane
    """
    points = []
    p_index = 0
    for _ in range(circle_count):
        circle_x = randint(0, grid_size)
        circle_y = randint(0, grid_size)
        radius = circle_radius * (1 + uniform(-circle_radius_deviation, circle_radius_deviation))
        points_count = int(circle_points * (1 + uniform(-circle_points_deviation, circle_points_deviation)))
        for _ in range(points_count):
            r = radius * sqrt(random())
            theta = random() * 2 * pi
            x = r * cos(theta)
            y = r * sin(theta)
            points.append(Particle(point_mass,
                                   [circle_x + x, circle_y + y], p_index))
            p_index += 1
    return points
