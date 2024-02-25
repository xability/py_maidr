from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from maidr.core.enum.plot_type import PlotType


class LibraryFactory(ABC):
    @abstractmethod
    def create_plot(self, plot_type: list[PlotType]) -> Any:
        raise NotImplementedError()
