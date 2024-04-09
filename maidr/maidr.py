from __future__ import annotations

from matplotlib.axes import Axes
from matplotlib.collections import QuadMesh, PathCollection
from matplotlib.container import BarContainer
from matplotlib.image import AxesImage
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon

from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr import Maidr
from maidr.core.figure_manager import FigureManager
from maidr.core.plot.box_plot import BoxPlotContainer


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
        >>> bar_maidr.save_html("maidr_bar_plot.html")  # Save the plot to an HTML file
    """
    ax = FigureManager.get_axes(plot)
    return FigureManager.create_maidr(ax, PlotType.BAR)


def get_sns_container():
    from packaging import version
    import seaborn.categorical

    min_version = "0.12"
    sns_version = seaborn.__version__

    if version.parse(sns_version) < version.parse(min_version):
        raise ImportError(
            f"Seaborn>={min_version} is required, but found {sns_version}."
        )
    else:
        return seaborn.categorical.BoxPlotContainer


def box(plot: Axes | dict) -> Maidr:
    ax = FigureManager.get_axes(plot)
    if not isinstance(plot, dict):
        cntr_type = get_sns_container()
    else:
        ax.add_container(BoxPlotContainer(plot))
        cntr_type = BoxPlotContainer

    return FigureManager.create_maidr(ax, PlotType.BOX, container_type=cntr_type)


def count(plot: Axes | BarContainer) -> Maidr:
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
        >>> count_maidr.save_html("maidr_count_plot.html")  # Save the plot to an HTML file
    """
    return bar(plot)


def heat(plot: Axes | AxesImage | QuadMesh) -> Maidr:
    ax = FigureManager.get_axes(plot)
    return FigureManager.create_maidr(ax, PlotType.HEAT)


def hist(plot: BarContainer | Polygon) -> Maidr:
    ax = FigureManager.get_axes(plot)
    return FigureManager.create_maidr(ax, PlotType.HIST)


def line(plot: Line2D) -> Maidr:
    ax = FigureManager.get_axes(plot)
    return FigureManager.create_maidr(ax, PlotType.LINE)


def scatter(plot: PathCollection) -> Maidr:
    ax = FigureManager.get_axes(plot)
    return FigureManager.create_maidr(ax, PlotType.SCATTER)


def stacked(plot: Axes | BarContainer) -> Maidr:
    ax = FigureManager.get_axes(plot)
    return FigureManager.create_maidr(ax, PlotType.STACKED)


def close() -> None:
    pass
