from __future__ import annotations

from matplotlib.axes import Axes
from matplotlib.collections import PathCollection
from matplotlib.lines import Line2D

from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_plot_data import MaidrPlotData
from maidr.exception.extraction_error import ExtractionError


class ScatterPlotData(MaidrPlotData):
    def __init__(self, axes: Axes) -> None:
        super().__init__(axes, PlotType.SCATTER)

    def _extract_maidr_data(self) -> dict:
        plt_type = self.type.value
        ax = self.axes

        maidr = {
            MaidrKey.TYPE.value: plt_type,
            MaidrKey.TITLE.value: ax.get_title(),
            MaidrKey.AXES.value: {
                MaidrKey.X.value: {
                    MaidrKey.LABEL.value: ax.get_xlabel(),
                },
                MaidrKey.Y.value: {
                    MaidrKey.LABEL.value: ax.get_ylabel(),
                },
            },
            MaidrKey.DATA.value: self.__extract_data(),
        }

        return maidr

    def __extract_data(self) -> list[dict]:
        ax = self.axes
        plot = None
        data = None

        if isinstance(ax, Axes):
            plot = ScatterPlotData.__extract_path_collection(ax)
        if isinstance(plot, PathCollection):
            data = ScatterPlotData.__extract_point_data(plot)

        if data is None:
            raise ExtractionError(self.type, plot)

        return data

    @staticmethod
    def __extract_point_data(plot: PathCollection) -> list[dict] | None:
        if plot is None:
            return None

        data = []
        for point in plot.get_offsets().data:
            x, y = point
            data.append(
                {
                    MaidrKey.X.value: float(x),
                    MaidrKey.Y.value: float(y),
                }
            )
        return data

    @staticmethod
    def __extract_path_collection(plot: Axes) -> PathCollection | None:
        for collection in plot.collections:
            if isinstance(collection, PathCollection):
                return collection
