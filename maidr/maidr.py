from __future__ import annotations

from matplotlib.axes import Axes
from matplotlib.container import BarContainer

from .core.maidr import Maidr
from .core.enum.plot_type import PlotType
from .utils.figure_manager import FigureManager


def bar(plot: Axes | BarContainer) -> Maidr:
    fig = FigureManager.get_figure(plot)
    plot_type = [PlotType.BAR for _ in fig.axes] if fig and fig.axes else []
    return FigureManager.create_maidr(fig, plot, plot_type)


def count(plot: Axes | BarContainer) -> Maidr:
    return bar(plot)


def close() -> None:
    pass
