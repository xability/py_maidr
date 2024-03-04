from __future__ import annotations

import numpy as np
from matplotlib.axes import Axes
from matplotlib.collections import QuadMesh
from matplotlib.container import BarContainer
from matplotlib.image import AxesImage
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon
from numpy import ndarray

from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr import Maidr
from maidr.core.figure_manager import FigureManager


def bar(
    plot: Axes | BarContainer | list[Axes | BarContainer] | ndarray,
) -> Maidr | tuple[Maidr]:
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
    axs = FigureManager.get_axes(plot)
    plot_type = [PlotType.BAR for _ in axs]
    return FigureManager.create_maidr(axs, plot_type)


def count(
    plot: Axes | BarContainer | list[Axes | BarContainer] | ndarray,
) -> Maidr | tuple[Maidr]:
    """
    Create a Maidr object for a count plot.

    Parameters
    ----------
    plot : Axes | list[Axes] | BarContainer | list[BarContainer]
        The count plot for which a Maidr object is to be created.

    Returns
    -------
    Maidr
        The created Maidr object representing the count plot.

    Raises
    ------
    ValueError
        If the input `plot` is missing the `matplotlib.figure.Figure` and
        `matplotlib.figure.Axes`.
    TypeError
        If the input `plot` is not a valid count plot.

    See Also
    --------
    Maidr : The core class encapsulating the plot with its MAIDR structure.
    bar : Function to create a Maidr object for matplotlib bar plots, usable as an
    alternative to `count()`.

    Note
    ----
    Since a count plot is a specific case of a bar plot, this function internally uses
    the `bar()` function to process the plot. The `count()` function is provided as a
    convenience to align with the `seaborn.countplot()` method.

    Examples
    --------
        >>> import seaborn as sns
        >>> import maidr
        >>> data = sns.load_dataset("titanic")  # Load the dataset
        >>> count_plot = sns.countplot(x="class", data=data)  # Generate a count plot
        >>> count_maidr = maidr.count(count_plot)  # Convert the plot to a Maidr object
        >>> count_maidr.save("maidr_count_plot.html")  # Save the plot to an HTML file
    """
    return bar(plot)


def heat(
    plot: Axes | AxesImage | QuadMesh | list[Axes | AxesImage | QuadMesh] | ndarray,
) -> Maidr | tuple[Maidr]:
    axs = FigureManager.get_axes(plot)
    plot_type = [PlotType.HEAT for _ in axs]
    return FigureManager.create_maidr(axs, plot_type)


def hist(
    plot: BarContainer | Polygon | list[BarContainer | Polygon] | np.ndarray,
) -> Maidr | tuple[Maidr]:
    axs = FigureManager.get_axes(plot)
    plot_type = [PlotType.HIST for _ in axs]
    return FigureManager.create_maidr(axs, plot_type)


def line(plot: Line2D | list[Line2D]) -> Maidr | tuple[Maidr]:
    axs = FigureManager.get_axes(plot)
    plot_type = [PlotType.LINE for _ in axs]
    return FigureManager.create_maidr(axs, plot_type)


def close() -> None:
    pass
