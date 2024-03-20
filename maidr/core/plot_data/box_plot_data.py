from __future__ import annotations

from matplotlib.axes import Axes
from seaborn.categorical import BoxPlotContainer

from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_plot_data import MaidrPlotData
from maidr.exception.extraction_error import ExtractionError


class BoxPlotData(MaidrPlotData):
    def __init__(self, axes: Axes) -> None:
        super().__init__(axes, PlotType.BOX)

    def _extract_maidr_data(self) -> dict:
        plt_type = self.type.value
        ax = self.axes

        maidr = {
            MaidrKey.TYPE.value: plt_type,
            MaidrKey.TITLE.value: ax.get_title(),
            MaidrKey.AXES.value: {
                MaidrKey.X.value: {
                    MaidrKey.LABEL.value: ax.get_xlabel(),
                    MaidrKey.LEVEL.value: self.__extract_level(),
                },
                MaidrKey.Y.value: {
                    MaidrKey.LABEL.value: ax.get_ylabel(),
                },
            },
            MaidrKey.DATA.value: self.__extract_data(),
        }

        return maidr

    def __extract_level(self) -> list:
        return [label.get_text() for label in self.axes.get_xticklabels()]

    def __extract_data(self) -> list:
        ax = self.axes
        plot = None
        data = None

        if isinstance(ax, Axes):
            plot = BoxPlotData.__extract_box_container(ax)
        if isinstance(plot, BoxPlotContainer):
            data = BoxPlotData.__extract_box_container_data(plot)

        if data is None:
            raise ExtractionError(self.type, plot)

        # noinspection PyTypeChecker
        return data

    @staticmethod
    def __extract_whisker_data(whiskers: list) -> list[dict]:
        data = list()
        for q1Line, q3Line in zip(whiskers[::2], whiskers[1::2]):
            q1 = float(q1Line.get_ydata()[0])
            q3 = float(q3Line.get_ydata()[0])
            data.append(
                {
                    "q1": q1,
                    "q3": q3,
                }
            )
        return data

    @staticmethod
    def __extract_cap_data(caps: list) -> list[dict]:
        data = list()
        for minLine, maxLine in zip(caps[::2], caps[1::2]):
            _min = float(minLine.get_ydata()[0])
            _max = float(maxLine.get_ydata()[0])
            data.append(
                {
                    "min": _min,
                    "max": _max,
                }
            )
        return data

    @staticmethod
    def __extract_median_data(medians: list) -> list:
        return [float(median.get_ydata()[0]) for median in medians]

    @staticmethod
    def __extract_flier_data(fliers: list, caps: list) -> list[dict]:
        data = list()
        for flier, cap in zip(fliers, caps):
            outliers = [float(outlier) for outlier in flier.get_ydata()]
            _min, _max = cap.values()
            data.append(
                {
                    "lower_outlier": [
                        outlier for outlier in outliers if outlier < _min
                    ],
                    "upper_outlier": [
                        outlier for outlier in outliers if outlier > _max
                    ],
                }
            )
        return data

    @staticmethod
    def __extract_bxp_maidr(bxpstats: dict) -> list[dict]:
        bxp_maidr = list()
        whiskers = BoxPlotData.__extract_whisker_data(bxpstats["whiskers"])
        caps = BoxPlotData.__extract_cap_data(bxpstats["caps"])
        medians = BoxPlotData.__extract_median_data(bxpstats["medians"])
        outliers = BoxPlotData.__extract_flier_data(bxpstats["fliers"], caps)

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

    @staticmethod
    def __extract_box_container_data(plot: BoxPlotContainer) -> list[dict]:
        bxpstats = {
            "whiskers": plot.whiskers,
            "medians": plot.medians,
            "caps": plot.caps,
            "fliers": plot.fliers,
        }
        return BoxPlotData.__extract_bxp_maidr(bxpstats)

    @staticmethod
    def __extract_box_container(plot: Axes) -> BoxPlotContainer | None:
        for container in plot.containers:
            if isinstance(container, BoxPlotContainer):
                return container
