from __future__ import annotations
from abc import ABC, abstractmethod

from matplotlib.axes import Axes

from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType


class MaidrPlot(ABC):
    def __init__(self, ax: Axes, plot_type: PlotType) -> None:
        # graphic object
        self.ax = ax

        # MAIDR data
        self.type = plot_type
        self._schema = self._init_maidr()

    def _init_maidr(self) -> dict:
        return {
            MaidrKey.TYPE: self.type,
            MaidrKey.TITLE: self.ax.get_title(),
            MaidrKey.AXES: self._extract_axes_data(),
            MaidrKey.DATA: self._extract_plot_data(),
        }

    def _extract_axes_data(self) -> dict:
        return {
            MaidrKey.X: {
                MaidrKey.LABEL: self.ax.get_xlabel(),
            },
            MaidrKey.Y: {
                MaidrKey.LABEL: self.ax.get_ylabel(),
            },
        }

    @abstractmethod
    def _extract_plot_data(self) -> list | dict:
        raise NotImplementedError()

    @property
    def schema(self) -> dict:
        return self._schema

    def set_id(self, maidr_id: str) -> None:
        self._schema[MaidrKey.ID.value] = maidr_id
