import matplotlib
matplotlib.use("TkAgg")
import renderutil
from matplotlib import animation, pyplot


possible_colors = {"b", "g", "r", "c", "m", "y", "k", "w"}


class ClusterVisualizer:
    """
    2D visualizer for clusterer
    """

    def __init__(self, clusterer):
        self.clusterer = clusterer
        clusterer.add_listener(self)
        self.xmin, self.xmax, self.ymin, self.ymax = (None,) * 4
        self.frame = 0
        self.ims = []
        self.fig = pyplot.figure()

    def on_set_points(self):
        points = self.clusterer.points
        for point in points:
            self.xmin = point.loc[0] if self.xmin is None else min(self.xmin, point.loc[0])
            self.xmax = point.loc[0] if self.xmax is None else max(self.xmax, point.loc[0])
            self.ymin = point.loc[1] if self.ymin is None else min(self.ymin, point.loc[1])
            self.ymax = point.loc[1] if self.ymax is None else max(self.ymax, point.loc[1])
        pyplot.xlim(xmin=self.xmin, xmax=self.xmax)
        pyplot.ylim(ymin=self.ymin, ymax=self.ymax)
        self.render()

    def on_update_points(self):
        self.render()
        self.frame += 1

    def render(self):
        self.ims.append([renderutil.render(self.clusterer.points)])

    def on_finish(self):
        print(len(self.ims))
        ani = animation.ArtistAnimation(self.fig, self.ims, interval=4, blit=True,
                                        repeat_delay=2000)
        ani.save("movie.mp4")
        pyplot.show()
