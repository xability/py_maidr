from typing import Any

from maidr.core.enum.plot_type import PlotType


class ExtractionError(Exception):
    """
    Exception raised for errors encountered during the MAIDR data extraction process.

    Parameters
    ----------
    plot_type : PlotType
        The type of plot from which data extraction failed.
    plot : Any
        The plot object that caused the extraction error.

    Attributes
    ----------
    message : str
        A human-readable message describing the error. Includes information about
        the plot type and the type of the plot object involved in the extraction error.

    Examples
    --------
    >>> from matplotlib.pyplot import figure
    >>> fig = figure()
    >>> ax = fig.add_subplot(111)
    >>> bar_plot = ax.bar([1, 2, 3], [3, 2, 1])
    >>> raise ExtractionError(PlotType.BAR, bar_plot)
    ExtractionError: Error extracting data for bar plot type from <class 'matplotlib.container.BarContainer'>.  # noqa: E501 (ignore line length warning)

    Notes
    -----
    This exception is intended to be used within the data extraction functions or
    methods of the MAIDR framework to facilitate error handling and debugging when
    processing different types of plots.
    """

    def __init__(self, plot_type: PlotType, plot: Any):
        self.message = (
            f"Error extracting data for {plot_type.value} plot type from {type(plot)}."
        )
        super().__init__(self.message)
