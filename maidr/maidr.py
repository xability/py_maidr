from __future__ import annotations

from matplotlib.axes import Axes
from matplotlib.collections import QuadMesh, PathCollection
from matplotlib.container import BarContainer
from matplotlib.image import AxesImage
from matplotlib.lines import Line2D

from maidr.core import Maidr
from maidr.core.enum import PlotType
from maidr.core.figure_manager import FigureManager
from maidr.core.plot.box_plot import BoxPlotContainer


def bar(plot: Axes | BarContainer) -> Maidr:
    r"""
    Create and return a Maidr object representing a bar plot.

    Parameters
    ----------
    plot : Axes | BarContainer
        A matplotlib or seaborn plot containing the bar plot data, either as an
        ``matplotlib.axes.Axes`` object with bar plot elements or directly as a
        ``matplotlib.container.BarContainer`` object.

    Returns
    -------
    Maidr
        An instance of the ``maidr.core.Maidr`` class representing the bar plot.

    Raises
    ------
    ValueError
        If `plot` is missing the ``matplotlib.figure.Figure`` or
        ``matplotlib.figure.Axes``.
    ExtractionError
        If bar plot data is not extractable from `plot`.

    See Also
    --------
    maidr.core.Maidr : The core class encapsulating the plot with its MAIDR structure.
    maidr.count : Function to create a Maidr object for seaborn count plot.

    Notes
    -----
    The input plot must be part of a ``matplotlib.figure.Figure``.

    Examples
    --------
    Matplotlib

    >>> import matplotlib.pyplot as plt
    >>> import maidr
    >>> bar_plot = plt.bar(['A', 'B', 'C'], [1, 2, 3])
    >>> bar_maidr = maidr.bar(bar_plot)
    >>> bar_maidr.show()

    Seaborn

    >>> import seaborn as sns
    >>> import maidr
    >>> tips = sns.load_dataset("tips")
    >>> bar_plot = sns.barplot(x="day", y="total_bill", data=tips)
    >>> bar_maidr = maidr.bar(bar_plot)
    >>> bar_maidr.show()
    """
    ax = FigureManager.get_axes(plot)
    return FigureManager.create_maidr(ax, PlotType.BAR)


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


def box(plot: Axes | dict) -> Maidr:
    r"""
    Create and return a Maidr object representing a box plot.

    Parameters
    ----------
    plot : Axes | dict
        A matplotlib or seaborn plot containing the box plot data, either as a
        ``matplotlib.axes.Axes`` object containing the box plot elements, or as a
        dictionary mapping each component of the boxplot to a list of the
        ``matplotlib.lines.Line2D`` instances created.

        If a dictionary is provided, the dictionary should have the following keys:

        - ``boxes``: the main body of the boxplot showing the quartiles and the
          median's confidence intervals if enabled.

        - ``medians``: horizontal lines at the median of each box.

        - ``whiskers``: the vertical lines extending to the most extreme, non-outlier
          data points.

        - ``caps``: the horizontal lines at the ends of the whiskers.

        - ``fliers``: points representing data that extend beyond the whiskers (fliers).

    Returns
    -------
    Maidr
        An instance of the ``maidr.core.Maidr`` class representing the box plot.

    Raises
    ------
    ValueError
        If `plot` is missing the ``matplotlib.figure.Figure`` or
        ``matplotlib.figure.Axes``.
    ImportError
        If `plot` is created using seaborn and the seaborn version is less than 0.12.
    ExtractionError
        If box plot data is not extractable from `plot`.

    See Also
    --------
    maidr.core.Maidr : The core class encapsulating the plot with its MAIDR structure.

    Warnings
    ________
    This function is dependent on ``seaborn.categorical.BoxPlotContainer``, when using
    seaborn, which requires seaborn version 0.12 or higher.

    Notes
    -----
    The Axes object or dictionary values must be part of a ``matplotlib.figure.Figure``.

    Examples
    ________
    Matplotlib

    >>> import matplotlib.pyplot as plt
    >>> import maidr
    >>> data = [25, 28, 29, 29, 30, 34, 35, 35, 37, 38]
    >>> box_plot = plt.boxplot(data)
    >>> box_maidr = maidr.box(box_plot)
    >>> box_maidr.show()

    Seaborn

    >>> import seaborn as sns
    >>> import maidr
    >>> iris = sns.load_dataset("iris")
    >>> box_plot = sns.boxplot(x="species", y="petal_length", data=iris)
    >>> box_maidr = maidr.box(box_plot)
    >>> box_maidr.show()
    """
    ax = FigureManager.get_axes(plot)
    if not isinstance(plot, dict):
        cntr_type = get_sns_container()
    else:
        ax.add_container(BoxPlotContainer(plot))
        cntr_type = BoxPlotContainer

    return FigureManager.create_maidr(ax, PlotType.BOX, container_type=cntr_type)


def count(plot: Axes) -> Maidr:
    r"""
    Create and return a Maidr object representing a count plot.

    Parameters
    ----------
    plot : Axes
        A `matplotlib.axes.Axes` object containing the count plot elements.

    Returns
    -------
    Maidr
        An instance of the ``maidr.core.Maidr`` class representing the count plot.

    Raises
    ------
    ValueError
        If `plot` is missing the `matplotlib.figure.Figure` or `matplotlib.figure.Axes`.
    ExtractionError
        If count plot data is not extractable from `plot`.

    See Also
    --------
    maidr.core.Maidr : The core class encapsulating the plot with its MAIDR structure.
    maidr.bar : Function to create a Maidr object for matplotlib bar plot.

    Notes
    -----
    - The Axes object must be part of a ``matplotlib.figure.Figure``.
    - Since a count plot is a specific case of a bar plot, this function internally uses
      the `bar()` function to process the plot. The `count()` function is provided as a
      convenience to align with the `seaborn.countplot()` method.

    Examples
    --------
    Seaborn

    >>> import seaborn as sns
    >>> import maidr
    >>> data = sns.load_dataset("titanic")
    >>> count_plot = sns.countplot(x="class", data=data)
    >>> count_maidr = maidr.count(count_plot)
    >>> count_maidr.show()
    """
    return bar(plot)


def heat(plot: Axes | AxesImage | QuadMesh, *, fill_label: str = "Fill value") -> Maidr:
    r"""
    Create and return a Maidr object representing a heatmap.

    Parameters
    ----------
    plot : Axes | AxesImage | QuadMesh
        A matplotlib or seaborn plot containing heatmap data. This can be an
        ``matplotlib.axes.Axes`` instance with heatmap elements, or more directly, an
        ``matplotlib.image.AxesImage`` or ``matplotlib.collections.QuadMesh``.
    fill_label : str, default="Fill value"
        Label describing the fill value in the heatmap, by default "Fill value".

    Returns
    -------
    Maidr
        An instance of the ``maidr.core.Maidr`` class representing the heatmap.

    Raises
    ------
    ValueError
        If `plot` is missing the ``matplotlib.figure.Figure`` or
        ``matplotlib.axes.Axes``.
    ExtractionError
        If heatmap data is not extractable from `plot`.

    See Also
    --------
    maidr.core.Maidr : The core class for encapsulating plots with MAIDR structure.

    Notes
    -----
    The input plot must be part of a ``matplotlib.figure.Figure``.

    Examples
    --------
    Matplotlib

    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> data = np.random.rand(10, 10)
    >>> fig, _ax = plt.subplots()
    >>> heatmap = _ax.imshow(data, cmap='hot')
    >>> heat_maidr = maidr.heat(heatmap)
    >>> heat_maidr.show()

    Seaborn

    >>> import seaborn as sns
    >>> import maidr
    >>> flights = sns.load_dataset("flights")
    >>> flights = flights.pivot("month", "year", "passengers")
    >>> heatmap = sns.heatmap(flights)
    >>> heat_maidr = maidr.heat(heatmap, fill_label="Passenger count")
    >>> heat_maidr.show()
    """
    ax = FigureManager.get_axes(plot)
    return FigureManager.create_maidr(ax, PlotType.HEAT, fill_label=fill_label)


def hist(plot: Axes | BarContainer) -> Maidr:
    r"""
    Create and return a Maidr object representing a histogram plot.

    Parameters
    ----------
    plot : Axes | BarContainer
        A matplotlib or seaborn plot containing the histogram plot data, which can be
        an ``matplotlib.axes.Axes`` object with histogram plot elements, a
        ``matplotlib.container.BarContainer`` which represents the bins of a histogram.

    Returns
    -------
    Maidr
        An instance of the ``maidr.core.Maidr`` class representing the histogram plot.

    Raises
    ------
    ValueError
        If `plot` is missing the ``matplotlib.figure.Figure`` or
        ``matplotlib.figure.Axes``.
    ExtractionError
        If histogram plot data is not extractable from `plot`.

    See Also
    --------
    maidr.core.Maidr : The core class encapsulating the plot with its MAIDR structure.

    Notes
    -----
    The input plot must be part of a ``matplotlib.figure.Figure``.

    Examples
    --------
    Matplotlib

    >>> import matplotlib.pyplot as plt
    >>> import maidr
    >>> import numpy as np
    >>> data = [np.random.normal(0, 100) for _ in range(1, 4)]
    >>> _, _, hist_plot = plt.hist(data, bins=30)
    >>> hist_maidr = maidr.hist(hist_plot)
    >>> hist_maidr.show()

    Seaborn

    >>> import seaborn as sns
    >>> import maidr
    >>> tips = sns.load_dataset("tips")
    >>> hist_plot = sns.histplot(tips['total_bill'], bins=20)
    >>> hist_maidr = maidr.hist(hist_plot)
    >>> hist_maidr.show()
    """
    ax = FigureManager.get_axes(plot)
    return FigureManager.create_maidr(ax, PlotType.HIST)


def line(plot: Axes | list[Line2D]) -> Maidr:
    r"""
    Create and return a Maidr object representing a line plot.

    Parameters
    ----------
    plot : Axes | list[Line2D]
        A matplotlib or seaborn plot containing the line plot data. This can be a
        ``matplotlib.axes.Axes`` object with line plot elements or a list of
        ``matplotlib.lines.Line2D`` objects.

    Returns
    -------
    Maidr
        An instance of the ``maidr.core.Maidr`` class representing the line plot.

    Raises
    ------
    ValueError
        If `plot` is missing the ``matplotlib.figure.Figure`` or
        ``matplotlib.figure.Axes``.
    ExtractionError
        If line plot data is not extractable from `plot`.

    See Also
    --------
    maidr.core.Maidr : The core class encapsulating the plot with its MAIDR structure.

    Notes
    -----
    - The input plot must be part of a ``matplotlib.figure.Figure``.
    - If multiple lines are present, only the last one will be represented with MAIDR
      structure.

    Examples
    --------
    Matplotlib

    >>> import matplotlib.pyplot as plt
    >>> import maidr
    >>> line_plot = plt.plot([1, 2, 3], [4, 5, 6])
    >>> line_maidr = maidr.line(ax)
    >>> line_maidr.save_html("maidr_line_plot.html")
    >>> line_maidr.show()

    Seaborn

    >>> import seaborn as sns
    >>> import maidr
    >>> tips = sns.load_dataset("tips")
    >>> subset_data = tips[tips["day"] == "Thur"]
    >>> line_plot = sns.lineplot(data=subset_data, x="total_bill", y="tip")
    >>> line_maidr = maidr.line(line_plot)
    >>> line_maidr.show()
    """
    ax = FigureManager.get_axes(plot)
    return FigureManager.create_maidr(ax, PlotType.LINE)


def scatter(plot: Axes | PathCollection) -> Maidr:
    r"""
    Create and return a Maidr object representing a scatter plot.

    Parameters
    ----------
    plot : Axes | PathCollection
        A matplotlib or seaborn plot that contains scatter plot data. This can be an
        ``matplotlib.axes.Axes`` instance with a scatter plot or a
        ``matplotlib.collections.PathCollection`` directly.

    Returns
    -------
    Maidr
        An instance of the Maidr class representing the scatter plot.

    Raises
    ------
    ValueError
        If `plot` is missing the ``matplotlib.figure.Figure`` or
        ``matplotlib.figure.Axes``.
    ExtractionError
        If scatter plot data is not extractable from `plot`.

    See Also
    --------
    maidr.core.Maidr : The core class encapsulating the plot with its MAIDR structure.

    Notes
    -----
    The input plot must be part of a ``matplotlib.figure.Figure``.

    Examples
    --------
    Matplotlib

    >>> import matplotlib.pyplot as plt
    >>> import maidr
    >>> x = [1, 2, 3]
    >>> y = [4, 5, 6]
    >>> scatter_plot = plt.scatter(x, y)
    >>> scatter_maidr = maidr.scatter(scatter_plot)
    >>> scatter_maidr.show()

    Seaborn

    >>> import seaborn as sns
    >>> import maidr
    >>> tips = sns.load_dataset("tips")
    >>> scatter_plot = sns.scatterplot(x="total_bill", y="tip", data=tips)
    >>> scatter_maidr = maidr.scatter(scatter_plot)
    >>> scatter_maidr.show()
    """
    ax = FigureManager.get_axes(plot)
    return FigureManager.create_maidr(ax, PlotType.SCATTER)


def stacked(plot: Axes | BarContainer) -> Maidr:
    ax = FigureManager.get_axes(plot)
    return FigureManager.create_maidr(ax, PlotType.STACKED)


def close() -> None:
    pass
