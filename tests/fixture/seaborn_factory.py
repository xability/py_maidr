from typing import Any

import seaborn as sns
from matplotlib.axes import Axes

from maidr.core.enum.plot_type import PlotType

from tests.fixture.matplotlib_factory import MatplotlibFactory


def create_countplot(ax: Axes) -> Any:
    sns.countplot(x=["a", "b", "a", "c", "b", "a"], ax=ax)
    ax.set_title("Test seaborn count title")
    ax.set_xlabel("Test seaborn count x label")
    ax.set_ylabel("Test seaborn count y label")


class SeabornFactory(MatplotlibFactory):
    def plot_on_ax(self, ax: Axes, plot_type: PlotType) -> Any:
        if plot_type == PlotType.COUNT:
            create_countplot(ax)
        elif plot_type is PlotType.BAR:
            self.create_barplot(ax)
        elif plot_type is PlotType.BOX:
            self.create_boxplot(ax)

    def create_barplot(self, ax: Axes) -> Any:
        sns.barplot(x=[1, 2, 3], y=[4, 5, 6], ax=ax)
        ax.set_title("Test seaborn bar title")
        ax.set_xlabel("Test seaborn bar x label")
        ax.set_ylabel("Test seaborn bar y label")

    def create_boxplot(self, ax: Axes) -> Any:
        sns.boxplot(data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], ax=ax)
        ax.set_title("Test seaborn box title")
        ax.set_xlabel("Test seaborn box x label")
        ax.set_ylabel("Test seaborn box y label")
