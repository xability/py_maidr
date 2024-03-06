from __future__ import annotations

from matplotlib.axes import Axes

from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_plot_data import MaidrPlotData
from maidr.core.plot.bar_plot_data import BarPlotData
from maidr.core.plot.heat_plot_data import HeatPlotData
from maidr.core.plot.hist_plot_data import HistPlotData
from maidr.core.plot.line_plot_data import LinePlotData


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
        elif PlotType.HEAT == plot_type:
            return HeatPlotData(ax)
        elif PlotType.HIST == plot_type:
            return HistPlotData(ax)
        elif PlotType.LINE == plot_type:
            return LinePlotData(ax)
        else:
            raise TypeError(f"Unsupported plot type: {plot_type}")
