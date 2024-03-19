from __future__ import annotations

from matplotlib.axes import Axes
from matplotlib.container import BarContainer

from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_plot_data import MaidrPlotData
from maidr.exception.extraction_error import ExtractionError


class StackedPlotData(MaidrPlotData):
    def __init__(self, axes: Axes) -> None:
        super().__init__(axes, PlotType.STACKED)

    def _extract_maidr_data(self) -> dict:
        plt_type = self.type.value
        ax = self.axes

        maidr = {
            MaidrKey.TYPE.value: plt_type,
            MaidrKey.LABELS.value: {
                MaidrKey.TITLE.value: ax.get_title(),
            },
            MaidrKey.AXES.value: {
                MaidrKey.X.value: {
                    MaidrKey.LABEL.value: ax.get_xlabel(),
                    MaidrKey.LEVEL.value: self.__extract_x_level(),
                },
                MaidrKey.Y.value: {
                    MaidrKey.LABEL.value: ax.get_ylabel(),
                },
                MaidrKey.FILL.value: {
                    MaidrKey.LABEL.value: "Fill",
                    MaidrKey.LEVEL.value: self.__extract_fill_level(),
                },
            },
            MaidrKey.DATA.value: self.__extract_data(),
        }

        return maidr

    def __extract_x_level(self):
        return [label.get_text() for label in self.axes.get_xticklabels()]

    def __extract_data(self):
        ax = self.axes
        plot = None
        data = None

        if isinstance(ax, Axes):
            plot = StackedPlotData.__extract_bar_containers(ax)
        if isinstance(plot, list):
            data = self.__extract_stacked_data(plot)

        if data is None:
            raise ExtractionError(self.type, plot)

        return data

    def __extract_fill_level(self):
        return [container.get_label() for container in self.axes.containers]

    @staticmethod
    def __extract_bar_containers(ax: Axes) -> list[BarContainer] | None:
        if ax is None or ax.containers is None:
            return None

        return ax.containers

    def __extract_stacked_data(self, plot: list[BarContainer]) -> list[dict] | None:
        x_level = self.__extract_x_level()
        data = list()

        for container in plot:
            if len(x_level) != len(container.patches):
                return None

            for x, y in zip(x_level, container.patches):
                data.append(
                    {
                        MaidrKey.X.value: x,
                        MaidrKey.FILL.value: container.get_label(),
                        MaidrKey.Y.value: float(y.get_height()),
                    }
                )

        return data
