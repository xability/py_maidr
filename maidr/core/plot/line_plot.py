from __future__ import annotations

from matplotlib.axes import Axes
from matplotlib.lines import Line2D

from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_plot import MaidrPlot
from maidr.core.mixin.extractor_mixin import LineExtractorMixin
from maidr.exception.extraction_error import ExtractionError


class LinePlot(MaidrPlot, LineExtractorMixin):
    def __init__(self, ax: Axes) -> None:
        super().__init__(ax, PlotType.LINE)

    def _extract_plot_data(self) -> list[dict]:
        plot = self.extract_line(self.ax)
        data = LinePlot.__extract_line_data(plot)

        if data is None:
            raise ExtractionError(self.type, plot)

        return data

    @staticmethod
    def __extract_line_data(plot: Line2D) -> list[dict] | None:
        if plot is None or plot.get_xydata() is None:
            return None

        return [
            {
                MaidrKey.X.value: float(x),
                MaidrKey.Y.value: float(y),
            }
            for x, y in plot.get_xydata()
        ]
