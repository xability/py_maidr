from __future__ import annotations

from matplotlib.axes import Axes
from matplotlib.container import BarContainer

from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_plot import MaidrPlot
from maidr.core.mixin.merger_mixin import DictMergerMixin
from maidr.core.mixin.extractor_mixin import (
    ContainerExtractorMixin,
    LevelExtractorMixin,
)
from maidr.exception.extraction_error import ExtractionError


class BarPlot(MaidrPlot, ContainerExtractorMixin, LevelExtractorMixin, DictMergerMixin):
    def __init__(self, ax: Axes) -> None:
        self.__level = self.extract_level(ax)
        super().__init__(ax, PlotType.BAR)

    def _extract_axes_data(self) -> dict:
        base_schema = super()._extract_axes_data()
        bar_ax_schema = {
            MaidrKey.X: {
                MaidrKey.LEVEL: self.__level,
            },
        }
        return self.merge_dict(base_schema, bar_ax_schema)

    def _extract_plot_data(self) -> list:
        plot = self.extract_container(self.ax, BarContainer, include_all=True)
        data = self.__extract_bar_container_data(plot)

        if data is None:
            raise ExtractionError(self.type, plot)

        return data

    def __extract_bar_container_data(
        self, plot: list[BarContainer] | None
    ) -> list | None:
        if plot is None:
            return None

        # Since v0.13, Seaborn has transitioned from using `list[Patch]` to
        # `list[BarContainers] for plotting bar plots.
        # So, extract data correspondingly based on the level.
        # Flatten all the `list[BarContainer]` to `list[Patch]`.
        plot = [patch for container in plot for patch in container.patches]
        level = self.__level

        if len(plot) != len(level):
            return None

        return [float(patch.get_height()) for patch in plot]
