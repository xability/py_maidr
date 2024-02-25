from typing import Any

import seaborn as sns
from matplotlib.axes import Axes

from maidr.core.enum.plot_type import PlotType

from tests.fixture.matplotlib_factory import MatplotlibFactory


class SeabornFactory(MatplotlibFactory):
    def plot_on_ax(self, ax: Axes, plot_type: PlotType):
        if plot_type == PlotType.BAR:
            self.create_bar_plot(ax)

    def create_bar_plot(self, ax: Axes) -> Any:
        sns.barplot(x=[1, 2, 3], y=[4, 5, 6], ax=ax)
