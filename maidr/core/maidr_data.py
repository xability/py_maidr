from __future__ import annotations

from abc import ABC, abstractmethod

from matplotlib.axes import Axes

from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType


class MaidrData(ABC):
    def __init__(self, axes: Axes, plot, plot_type: PlotType) -> None:
        # graphic object
        self.axes = axes
        self.plot = plot

        # common maidr data
        self.type = plot_type

        # extract maidr data from `Axes`
        self.maidr = self._extract_maidr()

    @abstractmethod
    def _extract_maidr(self) -> dict:
        pass

    def data(self):
        return self.maidr

    def set_id(self, maidr_id: str) -> None:
        self.maidr[MaidrKey.ID.value] = maidr_id
