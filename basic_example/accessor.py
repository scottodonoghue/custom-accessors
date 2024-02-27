import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.image as image
import pandas as pd

@pd.api.extensions.register_dataframe_accessor("custom_plot")
class PlottingAccessor:
    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj = pandas_obj
        self.img = image.imread('plt_logo.png')

    @staticmethod
    def _validate(obj):
        pass

    def hist(self, var):
        fig, ax = plt.subplots()

        ax.hist(self._obj[var])
        ax.set_title(f"Histogram of: {var}")
        fig.figimage(self.img, 50, 50, zorder=3, alpha=.3)

        plt.show()

    def scatter(self, var1, var2):
        fig, ax = plt.subplots()
        ax.scatter(self._obj[var1], self._obj[var2])
        ax.set_title(f"{var1} vs {var2}")
        ax.set_xlabel(f"{var1}")
        ax.set_ylabel(f"{var2}")
        fig.figimage(self.img, 60, 60, zorder=3, alpha=.3)
        plt.show()