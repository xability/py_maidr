from typing import Any

from maidr.core.enum import PlotType


class ExtractionError(Exception):
    """
    Exception raised for errors encountered during the MAIDR data extraction process.

    Parameters
    ----------
    plot_type : PlotType
        The type of plot from which data extraction failed.
    plot : Any
        The plot object that caused the extraction error.
    """

    def __init__(self, plot_type: PlotType, plot: Any):
        self.message = (
            f"Error extracting data for {plot_type.value} plot type from {type(plot)}."
        )
        super().__init__(self.message)
