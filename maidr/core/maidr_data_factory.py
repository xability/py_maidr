from __future__ import annotations

from matplotlib.axes import Axes

from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_data import MaidrData
from maidr.core.plot.bar_data import BarData


class MaidrDataFactory:
    """
    A factory class for creating MaidrData objects based on the given axes, plot, and plot type.
    """

    @staticmethod
    def create(axes: Axes, plot, plot_type: PlotType) -> MaidrData:
        """
        Create a MaidrData object based on the given axes, plot, and plot type.

        Parameters:
            axes (Axes): The axes object on which the plot is displayed.
            plot: The plot object.
            plot_type (PlotType): The type of plot.

        Returns:
            MaidrData: The created MaidrData object.

        Raises:
            ValueError: If the plot type is not supported.
        """
        if PlotType.BAR == plot_type:
            return BarData(axes, plot, plot_type)
        else:
            raise ValueError("Unsupported plot type: {0}".format(plot_type))
