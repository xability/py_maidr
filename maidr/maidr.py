from __future__ import annotations

from matplotlib.axes import Axes
from matplotlib.container import BarContainer

from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr import Maidr
from maidr.utils.figure_manager import FigureManager


def bar(plot: Axes | BarContainer) -> Maidr:
    """
    Create a Maidr object for a bar plot.

    Parameters
    ----------
    plot : Axes | BarContainer
            The bar plot for which a Maidr object is to be created.

    Returns
    -------
    Maidr
        The created Maidr object representing the bar plot.

    Raises
    ------
    ValueError
        If the input `plot` is missing the `matplotlib.figure.Figure` and
        `matplotlib.figure.Axes`.
    TypeError
        If the input `plot` is not a valid bar plot.

    See Also
    --------
    Maidr : The core class encapsulating the plot with its MAIDR structure.

    Examples
    --------
        >>> import matplotlib.pyplot as plt
        >>> import maidr
        >>> bar_plot = plt.bar(5, [1, 2, 3, 4, 5])  # Generate a bar plot
        >>> bar_maidr = maidr.bar(bar_plot)  # Convert the plot to a Maidr object
        >>> bar_maidr.save("maidr_bar_plot.html")  # Save the plot to an HTML file
    """
    fig = FigureManager.get_figure(plot)
    plot_type = [PlotType.BAR for _ in fig.axes] if fig and fig.axes else []
    return FigureManager.create_maidr(fig, plot, plot_type)


def close() -> None:
    pass
