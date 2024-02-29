from __future__ import annotations

from matplotlib.axes import Axes
from matplotlib.container import BarContainer

from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_plot_data import MaidrPlotData
from maidr.exception.extraction_error import ExtractionError


class BarPlotData(MaidrPlotData):
    """
    A class encapsulating all the MAIDR representation of the axes in a figure
    along with the plot.

    This class extends `MaidrPlotData` to specifically handle data extraction and
    representation for bar plots. It encapsulates the details required to represent a
    bar plot as a part of an interactive MAIDR visualization, including plot type,
    titles, axes labels, and the plot data itself.

    Parameters
    ----------
    axes : Axes
        The matplotlib axes object on which the bar plot is drawn.

    Warnings
    --------
    End users will typically not have to use this class directly.

    See Also
    --------
    MaidrPlotData : The base class for MAIDR plot data objects.
    """

    def __init__(self, axes: Axes) -> None:
        """
        Initializes the BarPlotData object with matplotlib axes containing the bar plot.

        Parameters
        ----------
        axes : Axes
            The axes object associated with the bar plot.
        """
        super().__init__(axes, PlotType.BAR)

    def _extract_maidr_data(self) -> dict:
        """
        Extracts and structures bar plot data for MAIDR visualization.

        Returns
        -------
        dict
            A dictionary containing the extracted maidr bar plot data.
        """
        plt_type = self.type.value
        ax = self.axes

        maidr = {
            MaidrKey.TYPE.value: plt_type,
            MaidrKey.TITLE.value: ax.get_title(),
            MaidrKey.AXES.value: {
                MaidrKey.X.value: {
                    MaidrKey.LABEL.value: ax.get_xlabel(),
                    MaidrKey.LEVEL.value: self.__extract_level(),
                },
                MaidrKey.Y.value: {
                    MaidrKey.LABEL.value: ax.get_ylabel(),
                },
            },
            MaidrKey.DATA.value: self.__extract_data(),
        }

        return maidr

    def __extract_level(self) -> list:
        """
        Extracts x-axis level values based on tick labels.

        Returns
        -------
        list
            A list of strings representing the x-axis levels.
        """
        return [label.get_text() for label in self.axes.get_xticklabels()]

    def __extract_data(self) -> list:
        """
        Extracts numerical data from the bar plot.

        Returns
        -------
        list
            A list of numerical data extracted from the bar plot.

        Raises
        ------
        ExtractionError
            If the plot object is incompatible for data extraction.
        """
        ax = self.axes
        plot = None
        data = None

        if isinstance(ax, Axes):
            plot = BarPlotData.__extract_bar_container(ax)
        if isinstance(plot, BarContainer):
            data = BarPlotData.__extract_bar_container_data(plot)

        if data is None:
            raise ExtractionError(self.type, plot)

        # noinspection PyTypeChecker
        return data

    @staticmethod
    def __extract_bar_container_data(plot: BarContainer) -> list | None:
        """
        Extracts numerical data from the specified BarContainer object if possible.

        Parameters
        ----------
        plot : BarContainer
            The BarContainer from which to extract the data.

        Returns
        -------
        list | None
            A list containing the numerical data extracted from the BarContainer, or
            None if the plot does not contain valid data values or is not a
            BarContainer.
        """
        if plot.patches is None:
            return None

        return [float(patch.get_height()) for patch in plot.patches]

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
        # TODO
        # If the Axes contains multiple bar plots, track and extract the correct one.
        for container in plot.containers:
            if isinstance(container, BarContainer):
                return container
