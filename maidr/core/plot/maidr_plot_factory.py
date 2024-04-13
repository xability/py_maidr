from __future__ import annotations

from matplotlib.axes import Axes

from maidr.core.enum import PlotType
from maidr.core.plot.maidr_plot import MaidrPlot
from maidr.core.plot.bar_plot import BarPlot
from maidr.core.plot.box_plot import BoxPlot
from maidr.core.plot.heat_plot import HeatPlot
from maidr.core.plot.hist_plot import HistPlot
from maidr.core.plot.line_plot import LinePlot
from maidr.core.plot.scatter_plot import ScatterPlot
from maidr.core.plot.grouped_bar_plot import GroupedBarPlot


class MaidrPlotFactory:
    """
    A factory for creating instances of ``maidr.core.maidr.MaidrPlot`` based on the
    plot type.

    Warnings
    --------
    End users will typically not have to use this class directly.

    See Also
    --------
    MaidrPlot : The base class for MAIDR plot data objects.
    PlotType : An enumeration of types of plots supported within MAIDR.
    """

    @staticmethod
    def create(ax: Axes, plot_type: PlotType, **kwargs) -> MaidrPlot:
        if PlotType.BAR == plot_type:
            return BarPlot(ax)
        elif PlotType.BOX == plot_type:
            return BoxPlot(ax, **kwargs)
        elif PlotType.HEAT == plot_type:
            return HeatPlot(ax, **kwargs)
        elif PlotType.HIST == plot_type:
            return HistPlot(ax)
        elif PlotType.LINE == plot_type:
            return LinePlot(ax)
        elif PlotType.SCATTER == plot_type:
            return ScatterPlot(ax)
        elif PlotType.DODGED == plot_type or PlotType.STACKED == plot_type:
            return GroupedBarPlot(ax, plot_type)
        else:
            raise TypeError(f"Unsupported plot type: {plot_type}.")
