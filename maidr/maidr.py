from __future__ import annotations

from typing import List

import matplotlib.pyplot as plt
from matplotlib.container import BarContainer

from .core.enum.plot_type import PlotType
from .core.maidr import Maidr
from .utils.figure_manager import FigureManager


def bar(plot: BarContainer) -> Maidr:
    """
    Create a Maidr object for a bar plot.

    Parameters:
        plot (BarContainer): The bar plot to create a Maidr object for.

    Returns:
        Maidr: The created Maidr object.

    Raises:
        None

    Examples:
        >>> fig, ax = plt.subplots()
        >>> data = [1, 2, 3, 4, 5]
        >>> plot = ax.bar(range(len(data)), data)
        >>> maidr = bar(plot)
    """
    fig = FigureManager.get_figure(plot)
    plot_type = [PlotType.BAR for _ in fig.axes] if fig and fig.axes else []
    return FigureManager.create_maidr(fig, plot, plot_type)


def close() -> None:
    """
    Closes the current connection.

    This function closes the current connection and performs any necessary cleanup.

    Parameters:
        None

    Returns:
        None
    """
    pass
