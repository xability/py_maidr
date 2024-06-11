from __future__ import annotations

import wrapt

from matplotlib.axes import Axes
from matplotlib.image import AxesImage

from maidr.core.enum import PlotType
from maidr.core.figure_manager import FigureManager


def heat(wrapped, _, args, kwargs) -> Axes | AxesImage:
    # Check for additional label used by MAIDR heatmap.
    fill_label = kwargs.pop("fill_label", "Fill")

    # Patch `ax.imshow()` and `seaborn.heatmap`.
    plot = wrapped(*args, **kwargs)

    # Extract the heatmap data points for MAIDR from the plots.
    ax = FigureManager.get_axes(plot)
    FigureManager.create_maidr(ax, PlotType.HEAT, fill_label=fill_label)

    # Return to the caller.
    return plot


# Patch matplotlib function.
wrapt.wrap_function_wrapper(Axes, "imshow", heat)

# Patch seaborn function.
wrapt.wrap_function_wrapper("seaborn", "heatmap", heat)
