from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

import numpy as np
from matplotlib.axes import Axes

from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType


class MaidrData(ABC):
    """
    Abstract base class for MAIDR data objects.

    Parameters
    ----------
    axes : Axes
        The axes object associated with the plot.
    plot : object
        The plot object.
    plot_type : PlotType
        The type of the plot.

    Attributes
    ----------
    axes : Axes
        The axes object associated with the plot.
    plot : object
        The plot object.
    type : PlotType
        The type of the plot.
    maidr : dict
        A dictionary containing the extracted MAIDR data.

    Methods
    -------
    data()
        Returns the MAIDR data.
    set_id(maidr_id)
        Sets the MAIDR ID.
    _extract_maidr()
        Abstract method to extract the MAIDR data.
    """

    def __init__(self, axes: Axes, plot: Any, plot_type: PlotType) -> None:
        """
        Initialize the MaidrData object.

        Parameters
        ----------
        axes : Axes
            The axes object associated with the plot.
        plot : object
            The plot object.
        plot_type : PlotType
            The type of the plot.

        Returns
        -------
        None
        """
        # graphic object
        self.axes = axes
        self.plot = plot

        # common maidr data
        self.type = plot_type

        # extract maidr data from `Axes`
        self.maidr = self._extract_maidr()

    @abstractmethod
    def _extract_maidr(self) -> dict:
        """
        Extracts the MAIDR data.

        Returns
        -------
        dict
            A dictionary containing the extracted MAIDR data.
        """
        pass

    def data(self) -> np.ndarray:
        """
        Returns the maidr data.

        Returns
        -------
        numpy.ndarray
            The maidr data.
        """
        return np.array(self.maidr)

    def set_id(self, maidr_id: str) -> None:
        """
        Sets the MAIDR ID.

        Parameters
        ----------
        maidr_id : str
            The MAIDR ID to be set.

        Returns
        -------
        None
        """
        self.maidr[MaidrKey.ID.value] = maidr_id
