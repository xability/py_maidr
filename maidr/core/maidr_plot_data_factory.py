from __future__ import annotations

from matplotlib.axes import Axes

from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_plot_data import MaidrPlotData
from maidr.core.plot_data.bar_plot_data import BarPlotData
from maidr.core.plot_data.box_plot_data import BoxPlotData
from maidr.core.plot_data.heat_plot_data import HeatPlotData
from maidr.core.plot_data.hist_plot_data import HistPlotData
from maidr.core.plot_data.line_plot_data import LinePlotData
from maidr.core.plot_data.scatter_plot_data import ScatterPlotData
from maidr.core.plot_data.stacked_plot_data import StackedPlotData


class MaidrPlotDataFactory:
    """
    A factory for creating instances of `MaidrPlotData` based on the plot type.

    This factory is responsible for instantiating the correct `MaidrPlotData` subclass
    based on the provided plot type.

    Warnings
    --------
    End users will typically not have to use this class directly.

    See Also
    --------
    MaidrPlotData : The base class for MAIDR plot data objects. It defines the common
        interface for all MAIDR data classes.
    PlotType : An enumeration that defines the supported types of plots within MAIDR.
    """

    @staticmethod
    def create(ax: Axes, plot_type: PlotType) -> MaidrPlotData:
        """
        Creates an instance of `MaidrPlotData` based on the provided plot type.

        Parameters
        ----------
        ax : Axes
            The axes object on which the plot is displayed.
        plot_type : PlotType
            The type of plot.

        Returns
        -------
        MaidrPlotData
            An instance of the `MaidrPlotData` subclass corresponding to the specified
            `plot_type`.

        Raises
        ------
        TypeError
            If the provided `plot_type` does not have a corresponding `MaidrPlotData`
            subclass.
        """
        if PlotType.BAR == plot_type:
            return BarPlotData(ax)
        elif PlotType.BOX == plot_type:
            return BoxPlotData(ax)
        elif PlotType.HEAT == plot_type:
            return HeatPlotData(ax)
        elif PlotType.HIST == plot_type:
            return HistPlotData(ax)
        elif PlotType.LINE == plot_type:
            return LinePlotData(ax)
        elif PlotType.SCATTER == plot_type:
            return ScatterPlotData(ax)
        elif PlotType.STACKED == plot_type:
            return StackedPlotData(ax)
        else:
            raise TypeError(f"Unsupported plot type: {plot_type}")
