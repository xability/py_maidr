from __future__ import annotations

from matplotlib.axes import Axes
from matplotlib.container import BarContainer

from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_plot_data import MaidrPlotData
from maidr.exception.extraction_error import ExtractionError


class HistPlotData(MaidrPlotData):
    def __init__(self, axes: Axes) -> None:
        """
        Initializes the HistPlotData object with matplotlib axes with matplotlib axes
        containing the histogram.

        Parameters
        ----------
        axes : Axes
            The axes object associated with the histogram.
        """
        super().__init__(axes, PlotType.HIST)

    def _extract_maidr_data(self) -> dict:
        """
        Extracts and structures histogram data for MAIDR visualization.

        Returns
        -------
        dict
            A dictionary containing the extracted maidr heatmap data.
        """
        plt_type = self.type.value
        ax = self.axes

        maidr = {
            MaidrKey.TYPE.value: plt_type,
            MaidrKey.TITLE.value: ax.get_title(),
            MaidrKey.AXES.value: {
                MaidrKey.X.value: {
                    MaidrKey.LABEL.value: ax.get_xlabel(),
                },
                MaidrKey.Y.value: {
                    MaidrKey.LABEL.value: ax.get_ylabel(),
                },
            },
            MaidrKey.DATA.value: self.__extract_data(),
        }

        return maidr

    def __extract_data(self) -> list[dict]:
        """
        Extracts numerical data from the histogram.

        Returns
        -------
        list[dict]
            A 2D list of numerical data extracted from the heatmap.

        Raises
        ------
        ExtractionError
            If the plot object is incompatible for data extraction.
        """
        ax = self.axes
        plot = None
        data = None

        if isinstance(ax, Axes):
            plot = HistPlotData.__extract_bar_container(ax)
        if isinstance(plot, BarContainer):
            data = HistPlotData.__extract_bar_container_data(plot)

        if data is None:
            raise ExtractionError(self.type, plot)

        return data

    @staticmethod
    def __extract_bar_container_data(plot: BarContainer) -> list[dict] | None:
        """
        Extracts numerical data from the specified ScalarMappable object if possible.

        Parameters
        ----------
        plot : BarContainer
            The BarContainer from which to extract the data.

        Returns
        -------
        list[dict] | None
            A 2D list containing the numerical data extracted from the BarContainer,
            or None if the plot does not contain valid data values or is not a
            BarContainer.
        """
        if plot is None or plot.patches is None:
            return None

        data = list()
        for patch in plot.patches:
            y = float(patch.get_height())
            x = float(patch.get_x())
            width = float(patch.get_width())
            data.append(
                {
                    MaidrKey.Y.value: y,
                    MaidrKey.X.value: x + width / 2,
                    MaidrKey.X_MIN.value: x,
                    MaidrKey.X_MAX.value: x + width,
                    MaidrKey.Y_MIN.value: 0,
                    MaidrKey.Y_MAX.value: y,
                }
            )

        return data

    @staticmethod
    def __extract_bar_container(plot: Axes) -> BarContainer | None:
        """
        Extracts the BarContainer from the given Axes object if possible.

        Parameters
        ----------
        plot : Axes
            The Axes object to search for a BarContainer.

        Returns
        -------
        BarContainer | None
            The first BarContainer found within the given Axes object, or None if no
            BarContainer is present.
        """
        for container in plot.containers:
            if isinstance(container, BarContainer):
                return container
