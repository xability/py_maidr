from __future__ import annotations

from typing import Iterable

import numpy as np
from matplotlib.axes import Axes
from matplotlib.container import BarContainer

from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_data import MaidrData


class BarData(MaidrData):
    """
    A class representing bar plot data.

    Parameters:
    - axes (Axes): The axes object to plot on.
    - plot: The plot data.
    - plot_type (PlotType): The type of plot.
    """

    def __init__(self, axes: Axes, plot, plot_type: PlotType) -> None:
        """
        Initialize a BarData object.

        Parameters:
        - axes (Axes): The axes object to plot on.
        - plot: The plot data.
        - plot_type (PlotType): The type of plot.

        Returns:
        None
        """
        super().__init__(axes, plot, plot_type)

    def _extract_maidr(self) -> dict:
        """
        Extracts the maidr information from the bar plot.

        Returns:
            dict: A dictionary containing the extracted maidr information.
        """
        plt_type = self.type.value
        ax = self.axes

        maidr = {
            MaidrKey.TYPE.value: plt_type,
            MaidrKey.TITLE.value: ax.get_title(),
            MaidrKey.SELECTOR.value: "TODO: Enter your bar plot selector here",
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

    def __extract_level(self) -> list | None:
        """
        Extracts the level values from the x-axis tick labels.

        Returns:
            list | None: A list of level values extracted from the x-axis tick labels.
                Returns None if no tick labels are found.
        """
        return [label.get_text() for label in self.axes.get_xticklabels()]

    def __extract_data(self) -> list | None:
        """
        Extracts data from the plot.

        Returns:
            list | None: The extracted data from the plot, or None if the plot is not valid.
        """
        plot = self.plot

        if isinstance(plot, BarContainer) and isinstance(plot.datavalues, Iterable):
            bc_data = []
            for value in plot.datavalues:
                if isinstance(value, np.integer):
                    bc_data.append(int(value))
                elif isinstance(value, np.floating):
                    bc_data.append(float(value))
                else:
                    bc_data.append(value)
            data = bc_data
        else:
            # TODO: What would be the right exception? ExtractionError?
            raise TypeError("")

        return data
