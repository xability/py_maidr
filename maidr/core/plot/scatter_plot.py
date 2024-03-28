from __future__ import annotations

from matplotlib.axes import Axes
from matplotlib.collections import PathCollection

from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_plot import MaidrPlot
from maidr.core.mixin.extractor_mixin import CollectionExtractorMixin
from maidr.exception.extraction_error import ExtractionError


class ScatterPlot(MaidrPlot, CollectionExtractorMixin):
    def __init__(self, ax: Axes) -> None:
        super().__init__(ax, PlotType.SCATTER)

    def _extract_plot_data(self) -> list[dict]:
        plot = self.extract_collection(self.ax, PathCollection)
        data = ScatterPlot.__extract_point_data(plot)

        if data is None:
            raise ExtractionError(self.type, plot)

        return data

    @staticmethod
    def __extract_point_data(plot: PathCollection | None) -> list[dict] | None:
        if plot is None or plot.get_offsets() is None:
            return None

        data = list()
        for point in plot.get_offsets().data:
            x, y = point
            data.append(
                {
                    MaidrKey.X.value: float(x),
                    MaidrKey.Y.value: float(y),
                }
            )

        return data
