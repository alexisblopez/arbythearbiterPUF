import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np


class SupportVectorMachine:
    def __init__(self, visualization=True):
        self.visualization = visualization
        self.colors = {1: 'r', -1: 'b'}

        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1, 1, 1)

    def fit(self, data):
        pass

    def predict(self, data):
        # sign( x.w+b )
        # classification =
        pass
