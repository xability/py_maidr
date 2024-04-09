from __future__ import annotations

from matplotlib.axes import Axes
from matplotlib.cm import ScalarMappable
from matplotlib.collections import QuadMesh

from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_plot import MaidrPlot
from maidr.core.mixin.extractor_mixin import (
    LevelExtractorMixin,
    ScalarMappableExtractorMixin,
)
from maidr.core.mixin.merger_mixin import DictMergerMixin
from maidr.exception.extraction_error import ExtractionError


class HeatPlot(
    MaidrPlot, LevelExtractorMixin, ScalarMappableExtractorMixin, DictMergerMixin
):
    def __init__(self, ax: Axes) -> None:
        super().__init__(ax, PlotType.HEAT)

    def _init_maidr(self) -> dict:
        base_maidr = super()._init_maidr()
        heat_maidr = {
            MaidrKey.LABELS: {
                MaidrKey.FILL: "Fill value",
            },
        }
        return self.merge_dict(base_maidr, heat_maidr)

    def _extract_axes_data(self) -> dict:
        base_ax_schema = super()._extract_axes_data()
        heat_ax_schema = {
            MaidrKey.X: {
                MaidrKey.LEVEL: self.extract_level(self.ax, MaidrKey.X),
            },
            MaidrKey.Y: {
                MaidrKey.LEVEL: self.extract_level(self.ax, MaidrKey.Y),
            },
        }
        return self.merge_dict(base_ax_schema, heat_ax_schema)

    def _extract_plot_data(self) -> list[list]:
        plot = self.extract_scalar_mappable(self.ax)
        data = HeatPlot.__extract_scalar_mappable_data(plot)

        if data is None:
            raise ExtractionError(self.type, plot)

        return data

    @staticmethod
    def __extract_scalar_mappable_data(sm: ScalarMappable) -> list[list] | None:
        if sm is None or sm.get_array() is None:
            return None

        array = sm.get_array().data
        if isinstance(sm, QuadMesh):
            # Data gets flattened in ScalarMappable, when the plot is from QuadMesh.
            # So, reshaping the data to reflect the original quadrilaterals
            m, n, _ = sm.get_coordinates().shape
            array = array.reshape(m - 1, n - 1)  # Coordinates shape is (M + 1, N + 1)

        return [list(map(float, row)) for row in array]
