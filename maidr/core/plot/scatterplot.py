from __future__ import annotations

from matplotlib.axes import Axes
from matplotlib.collections import PathCollection

from maidr.core.enum import MaidrKey, PlotType
from maidr.core.plot import MaidrPlot
from maidr.exception import ExtractionError
from maidr.utils.mixin import CollectionExtractorMixin


class ScatterPlot(MaidrPlot, CollectionExtractorMixin):
    def __init__(self, ax: Axes) -> None:
        super().__init__(ax, PlotType.SCATTER)

    def _extract_plot_data(self) -> list[dict]:
        plot = self.extract_collection(self.ax, PathCollection)
        data = ScatterPlot._extract_point_data(plot)

        if data is None:
            raise ExtractionError(self.type, plot)

        return data

    @staticmethod
    def _extract_point_data(plot: PathCollection | None) -> list[dict] | None:
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
