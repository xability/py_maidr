from __future__ import annotations

from matplotlib.axes import Axes

from maidr.core.enum import MaidrKey, PlotType
from maidr.core.plot import MaidrPlot
from maidr.exception import ExtractionError
from maidr.utils.mixin import (
    ContainerExtractorMixin,
    DictMergerMixin,
    LevelExtractorMixin,
)


class BoxPlotContainer(DictMergerMixin):
    def __init__(self):
        self.boxes = []
        self.medians = []
        self.whiskers = []
        self.caps = []
        self.fliers = []

    def __repr__(self):
        return f"<BoxPlotContainer object with {len(self.boxes)} boxes>"

    def add_artists(self, artist: dict):
        for box in artist["boxes"]:
            self.boxes.append(box)
        for median in artist["medians"]:
            self.medians.append(median)
        for whisker in artist["whiskers"]:
            self.whiskers.append(whisker)
        for cap in artist["caps"]:
            self.caps.append(cap)
        for flier in artist["fliers"]:
            self.fliers.append(flier)

    def bxp_stats(self) -> dict:
        return {
            "boxes": self.boxes,
            "medians": self.medians,
            "whiskers": self.whiskers,
            "caps": self.caps,
            "fliers": self.fliers,
        }


class _BoxPlotExtractorMixin:
    @staticmethod
    def extract_whiskers(whiskers: list) -> list[dict]:
        return _BoxPlotExtractorMixin.__extract_extremes(
            whiskers, MaidrKey.Q1, MaidrKey.Q3
        )

    @staticmethod
    def extract_caps(caps: list) -> list[dict]:
        return _BoxPlotExtractorMixin.__extract_extremes(
            caps, MaidrKey.MIN, MaidrKey.MAX
        )

    @staticmethod
    def __extract_extremes(
        extremes: list, start_key: MaidrKey, end_key: MaidrKey
    ) -> list[dict]:
        data = list()

        for start, end in zip(extremes[::2], extremes[1::2]):
            start_data = float(start.get_ydata()[0])
            end_data = float(end.get_ydata()[0])

            data.append(
                {
                    start_key.value: start_data,
                    end_key.value: end_data,
                }
            )

        return data

    @staticmethod
    def extract_medians(medians: list) -> list:
        return [float(median.get_ydata()[0]) for median in medians]

    @staticmethod
    def extract_outliers(fliers: list, caps: list) -> list[dict]:
        data = list()

        for outlier, cap in zip(fliers, caps):
            outliers = [float(outlier) for outlier in outlier.get_ydata()]
            _min, _max = cap.values()

            data.append(
                {
                    MaidrKey.LOWER_OUTLIER.value: sorted(
                        [outlier for outlier in outliers if outlier < _min]
                    ),
                    MaidrKey.UPPER_OUTLIER.value: sorted(
                        [outlier for outlier in outliers if outlier > _max]
                    ),
                }
            )

        return data


class BoxPlot(
    MaidrPlot,
    _BoxPlotExtractorMixin,
    ContainerExtractorMixin,
    LevelExtractorMixin,
    DictMergerMixin,
):
    def __init__(self, ax: Axes, **kwargs) -> None:
        self._bxp_stats = kwargs.pop("bxp_stats", None)
        super().__init__(ax, PlotType.BOX)

    def _extract_axes_data(self) -> dict:
        base_ax_schema = super()._extract_axes_data()
        box_ax_schema = {
            MaidrKey.X.value: {
                MaidrKey.LEVEL.value: self.extract_level(self.ax),
            },
        }
        return self.merge_dict(base_ax_schema, box_ax_schema)

    def _extract_plot_data(self) -> list:
        data = self._extract_bxp_maidr(self._bxp_stats)

        if data is None:
            raise ExtractionError(self.type, self.ax)

        return data

    def _extract_bxp_maidr(self, bxp_stats: dict) -> list[dict] | None:
        if bxp_stats is None:
            return None

        bxp_maidr = list()
        whiskers = self.extract_whiskers(bxp_stats["whiskers"])
        caps = self.extract_caps(bxp_stats["caps"])
        medians = self.extract_medians(bxp_stats["medians"])
        outliers = self.extract_outliers(bxp_stats["fliers"], caps)

        for whisker, cap, median, outlier in zip(whiskers, caps, medians, outliers):
            bxp_maidr.append(
                {
                    MaidrKey.LOWER_OUTLIER.value: outlier["lower_outlier"],
                    MaidrKey.MIN.value: cap["min"],
                    MaidrKey.Q1.value: whisker["q1"],
                    MaidrKey.Q2.value: median,
                    MaidrKey.Q3.value: whisker["q3"],
                    MaidrKey.MAX.value: cap["max"],
                    MaidrKey.UPPER_OUTLIER.value: outlier["upper_outlier"],
                }
            )

        return bxp_maidr
