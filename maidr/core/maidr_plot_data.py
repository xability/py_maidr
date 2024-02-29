from __future__ import annotations
from abc import ABC, abstractmethod

from matplotlib.axes import Axes

from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType


class MaidrPlotData(ABC):
    """
    An abstract base class for encapsulating data associated with plots in MAIDR
    structure.

    This class serves as a foundation for subclasses that specialize in handling
    different types of plots by extracting and storing relevant MAIDR data.

    Parameters
    ----------
    axes : Axes
        The axes object on which the plot is displayed.
    type : PlotType
        The type of the plot.

    Attributes
    ----------
    axes : Axes
        The axes object on which the plot is displayed.
    type : PlotType
        The type of the plot.
    maidr_data : dict
        A dictionary containing the extracted MAIDR data.

    Methods
    -------
    data()
        Retrieves the extracted MAIDR data.
    set_id(maidr_id)
        Assigns a unique MAIDR ID to the plot data.

    Warnings
    --------
    End users will typically not have to use this class directly.

    See Also
    --------
    BarData : Subclass of `MaidrPlotData` specialized for bar plots.
    """

    def __init__(self, axes: Axes, plot_type: PlotType) -> None:
        """
        Initialize the MaidrData object.

        Parameters
        ----------
        axes : Axes
            The axes object on which the plot is displayed.
        """
        # graphic object
        self.axes = axes

        self.type = plot_type

        # extract maidr data from `Axes`
        self.maidr_data = self._extract_maidr_data()

    @abstractmethod
    def _extract_maidr_data(self) -> dict:
        """
        Abstract method to be implemented by subclasses for extracting specific MAIDR
        data from the plot.

        Returns
        -------
        dict
            A dictionary containing the extracted MAIDR data based on the plot type.
        """
        pass

    def data(self) -> dict:
        """
        Returns the maidr data.

        Returns
        -------
        dict
            The dictionary containing extracted MAIDR data based on the plot type.
        """
        return self.maidr_data

    def set_id(self, maidr_id: str) -> None:
        """
        Sets the MAIDR id.

        Parameters
        ----------
        maidr_id : str
            The unique identifier to be associated with this MAIDR data instance.
        """
        self.maidr_data[MaidrKey.ID.value] = maidr_id
