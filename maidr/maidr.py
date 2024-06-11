from __future__ import annotations

from typing import Literal, Any

from matplotlib.axes import Axes
from matplotlib.container import BarContainer

from maidr.core import Maidr
from maidr.core.enum import PlotType
from maidr.core.figure_manager import FigureManager


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


def test_enum_comparison():
    print(
        f"PlotType.COUNT == PlotType.BAR: {PlotType.COUNT == PlotType.BAR}"
    )  # Should be False
    print(
        f"PlotType.COUNT is PlotType.BAR: {PlotType.COUNT is PlotType.BAR}"
    )  # Should be False
    print(
        f"PlotType.COUNT == PlotType.COUNT: {PlotType.COUNT == PlotType.COUNT}"
    )  # Should be True
    print(
        f"PlotType.BAR == PlotType.BAR: {PlotType.BAR == PlotType.BAR}"
    )  # Should be True
    print(
        f"PlotType.COUNT is PlotType.COUNT: {PlotType.COUNT is PlotType.COUNT}"
    )  # Should be True
    print(f"PlotType.BAR is PlotType.BAR: {PlotType.BAR is PlotType.BAR}")
