from __future__ import annotations

from typing import Any

from matplotlib.axes import Axes

from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_plot_data import MaidrPlotData
from maidr.core.plot.bar_plot_data import BarPlotData


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
    def create(axes: Axes, plot: Any, plot_type: PlotType) -> MaidrPlotData:
        """
        Creates an instance of `MaidrPlotData` based on the provided plot type.

        Parameters
        ----------
        axes : Axes
            The axes object on which the plot is displayed.
        plot : Any
            The plot object.
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
            return BarPlotData(axes, plot)
        else:
            raise TypeError(f"Unsupported plot type: {plot_type}")
