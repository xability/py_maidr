from __future__ import annotations

import wrapt

from matplotlib.figure import Figure

from maidr.core.figure_manager import FigureManager


@wrapt.patch_function_wrapper(Figure, "clear")
def clear(wrapped, instance, args, kwargs) -> None:
    wrapped(*args, **kwargs)
    try:
        maidr = FigureManager.get_maidr(instance.get_figure())
    except KeyError:
        return
    maidr.clear()
