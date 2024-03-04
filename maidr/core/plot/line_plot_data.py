from __future__ import annotations

from matplotlib.axes import Axes
from matplotlib.lines import Line2D

from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_plot_data import MaidrPlotData
from maidr.exception.extraction_error import ExtractionError


class LinePlotData(MaidrPlotData):
    last_extracted_id = -1

    def __init__(self, axes: Axes) -> None:
        super().__init__(axes, PlotType.LINE)

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
            self.last_extracted_id += 1
            plot = LinePlotData.__extract_line(ax, self.last_extracted_id)
        if isinstance(plot, Line2D):
            data = LinePlotData.__extract_line_data(plot)

        if data is None:
            raise ExtractionError(self.type, plot)

        return data

    @staticmethod
    def __extract_line_data(plot: Line2D) -> list[dict] | None:
        if plot is None:
            return None

        return [
            {
                MaidrKey.X.value: float(x),
                MaidrKey.Y.value: float(y),
            }
            for x, y in plot.get_xydata()
        ]

    @staticmethod
    def __extract_line(plot: Axes, line_id: int) -> Line2D | None:
        if plot is None or plot.get_lines() is None:
            return None

        return plot.get_lines()[line_id]
