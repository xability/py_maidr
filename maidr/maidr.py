from __future__ import annotations

from typing import Literal, Any

import numpy as np
import wrapt
from matplotlib.axes import Axes
from matplotlib.collections import PathCollection
from matplotlib.container import BarContainer
from matplotlib.image import AxesImage
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon

from maidr.core import Maidr
from maidr.core.enum import PlotType
from maidr.core.figure_manager import FigureManager
from maidr.core.plot.box_plot import BoxPlotContainer


def bar(wrapped, _, args, kwargs) -> Axes | BarContainer:
    plot = wrapped(*args, **kwargs)

    ax = FigureManager.get_axes(plot)
    FigureManager.create_maidr(ax, PlotType.BAR)

    return plot


wrapt.wrap_function_wrapper(Axes, "bar", bar)
wrapt.wrap_function_wrapper("seaborn", "barplot", bar)
wrapt.wrap_function_wrapper("seaborn", "countplot", bar)


def get_sns_container() -> type[BoxPlotContainer]:
    """Return the BoxPlotContainer class from seaborn if version >= 0.12, else raise ImportError."""  # noqa
    from packaging import version
    import seaborn.categorical

    min_version = "0.12"
    sns_version = seaborn.__version__  # type: ignore

    if version.parse(sns_version) < version.parse(min_version):
        raise ImportError(
            f"Seaborn>={min_version} is required, but found {sns_version}."
        )
    else:
        return seaborn.categorical.BoxPlotContainer  # type: ignore


def box(wrapped, _, args, kwargs) -> Axes | dict:
    plot = wrapped(*args, **kwargs)

    ax = FigureManager.get_axes(plot)
    if not isinstance(plot, dict):
        cntr_type = get_sns_container()
    else:
        ax.add_container(BoxPlotContainer(plot))
        cntr_type = BoxPlotContainer

    FigureManager.create_maidr(ax, PlotType.BOX, container_type=cntr_type)

    return plot


wrapt.wrap_function_wrapper(Axes, "boxplot", box)
wrapt.wrap_function_wrapper("seaborn", "boxplot", box)


def heat(wrapped, _, args, kwargs) -> Axes | AxesImage:
    fill_label = kwargs.pop("fill_label", "Fill")
    plot = wrapped(*args, **kwargs)

    ax = FigureManager.get_axes(plot)
    FigureManager.create_maidr(ax, PlotType.HEAT, fill_label=fill_label)

    return plot


wrapt.wrap_function_wrapper(Axes, "imshow", heat)
wrapt.wrap_function_wrapper("seaborn", "heatmap", heat)


@wrapt.patch_function_wrapper(Axes, "hist")
def mpl_hist(
    wrapped, _, args, kwargs
) -> tuple[
    np.ndarray | list[np.ndarray],
    np.ndarray,
    BarContainer | Polygon | list[BarContainer | Polygon],
]:
    n, bins, plot = wrapped(*args, **kwargs)

    ax = FigureManager.get_axes(plot)
    FigureManager.create_maidr(ax, PlotType.HIST)

    return n, bins, plot


@wrapt.patch_function_wrapper("seaborn", "histplot")
def sns__hist(wrapped, _, args, kwargs) -> Axes:
    plot = wrapped(*args, **kwargs)

    ax = FigureManager.get_axes(plot)
    FigureManager.create_maidr(ax, PlotType.HIST)

    return plot


def line(wrapped, _, args, kwargs) -> Axes | list[Line2D]:
    plot = wrapped(*args, **kwargs)

    ax = FigureManager.get_axes(plot)
    FigureManager.create_maidr(ax, PlotType.LINE)

    return plot


wrapt.wrap_function_wrapper(Axes, "plot", line)
wrapt.wrap_function_wrapper("seaborn", "lineplot", line)


def scatter(wrapped, _, args, kwargs) -> Axes | PathCollection:
    plot = wrapped(*args, **kwargs)

    ax = FigureManager.get_axes(plot)
    FigureManager.create_maidr(ax, PlotType.SCATTER)

    return plot


wrapt.wrap_function_wrapper(Axes, "scatter", scatter)
wrapt.wrap_function_wrapper("seaborn", "scatterplot", scatter)


def show(plot: Any, renderer: Literal["auto", "ipython", "browser"] = "auto") -> object:
    ax = FigureManager.get_axes(plot)
    maidr = FigureManager.get_maidr(ax.get_figure())
    return maidr.show(renderer)


def save_html(
    plot: Any, file: str, *, lib_dir: str | None = "lib", include_version: bool = True
) -> str:
    ax = FigureManager.get_axes(plot)
    maidr = FigureManager.get_maidr(ax.get_figure())
    return maidr.save_html(file, lib_dir=lib_dir, include_version=include_version)


def stacked(plot: Axes | BarContainer) -> Maidr:
    ax = FigureManager.get_axes(plot)
    return FigureManager.create_maidr(ax, PlotType.STACKED)


def close() -> None:
    pass
