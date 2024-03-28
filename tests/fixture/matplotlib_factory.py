from __future__ import annotations
from contextlib import contextmanager
from typing import Any

from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from numpy import ndarray

from maidr.core.enum.plot_type import PlotType
from maidr.core.figure_manager import FigureManager
from tests.fixture.library_factory import LibraryFactory


class MatplotlibFactory(LibraryFactory):
    @contextmanager
    def create_plot(self, plot_types: list[PlotType]) -> Any:
        fig, axs = plt.subplots(1, len(plot_types))
        axs = axs if isinstance(axs, ndarray) else [axs]

        for ax, plot_type in zip(axs, plot_types):
            self.plot_on_ax(ax, plot_type)

        try:
            yield fig, FigureManager.get_axes(*axs)
        finally:
            plt.close(fig)

    def plot_on_ax(self, ax: Axes, plot_type: PlotType):
        if plot_type == PlotType.BAR:
            self.create_bar_plot(ax)

    def create_bar_plot(self, ax: Axes) -> Any:
        # TODO: using numbers makes matplotlib to add additional ticks messing with the
        # level extraction
        ax.bar(["1", "2", "3"], [4, 5, 6])
        ax.set_title("Test matplotlib title")
        ax.set_xlabel("Test matplotlib x label")
        ax.set_ylabel("Test matplotlib y label")
