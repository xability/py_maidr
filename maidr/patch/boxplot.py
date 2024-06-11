from __future__ import annotations

import contextlib
import contextvars
import wrapt

from matplotlib.axes import Axes

from maidr.core.context_manager import ContextManager
from maidr.core.enum import PlotType
from maidr.core.figure_manager import FigureManager
from maidr.core.plot.boxplot import BoxPlotContainer


class BoxplotContextManager(ContextManager):
    _bxp_context = contextvars.ContextVar("bxp_context", default=BoxPlotContainer())

    @classmethod
    @contextlib.contextmanager
    def set_internal_context(cls):
        with super(BoxplotContextManager, cls).set_internal_context():
            token = cls._bxp_context.set(BoxPlotContainer())
            try:
                yield cls.get_bxp_context()
            finally:
                cls._bxp_context.reset(token)

    @classmethod
    def get_bxp_context(cls) -> BoxPlotContainer:
        return cls._bxp_context.get()

    @classmethod
    def add_bxp_context(cls, bxp_context: dict) -> None:
        cls.get_bxp_context().add_artists(bxp_context)


@wrapt.patch_function_wrapper(Axes, "bxp")
def mpl_box(wrapped, _, args, kwargs) -> dict:
    # Don't proceed if the call is made internally by the patched function.
    if BoxplotContextManager.is_internal_context():
        plot = wrapped(*args, **kwargs)
        BoxplotContextManager.add_bxp_context(plot)
        return plot

    # Set the internal context to avoid cyclic processing.
    with ContextManager.set_internal_context():
        # Patch `ax.boxplot()` and `ax.bxp()`.
        plot = wrapped(*args, **kwargs)

    # Extract the boxplot data points for MAIDR from the plot.
    ax = FigureManager.get_axes(plot)
    FigureManager.create_maidr(ax, PlotType.BOX, bxp_stats=plot)

    # Return to the caller.
    return plot


@wrapt.patch_function_wrapper("seaborn", "boxplot")
def sns_box(wrapped, _, args, kwargs) -> Axes:
    # Set the internal context to avoid cyclic processing.
    with BoxplotContextManager.set_internal_context() as bxp_context:
        # Patch `ax.boxplot()` and `ax.bxp()`.
        plot = wrapped(*args, **kwargs)
        bxp_container = bxp_context

    # Extract the boxplot data points for MAIDR from the plot.
    ax = FigureManager.get_axes(bxp_container.bxp_stats())
    FigureManager.create_maidr(ax, PlotType.BOX, bxp_stats=bxp_container.bxp_stats())

    # Return to the caller.
    return plot
