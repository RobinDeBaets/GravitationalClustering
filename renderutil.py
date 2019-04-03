from matplotlib import pyplot


def render(points):
    locs = [point.loc for point in points]
    masses = [point.mass for point in points]
    return pyplot.scatter(*zip(*locs), s=masses, c=["b" for _ in masses])
