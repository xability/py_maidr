from __future__ import annotations

from typing import Iterable

import numpy as np
from matplotlib.axes import Axes
from matplotlib.container import BarContainer

from maidr.core.maidr_data import MaidrData
from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType


class BarData(MaidrData):
    def __init__(self, axes: Axes, plot, plot_type: PlotType) -> None:
        super().__init__(axes, plot, plot_type)

    def _extract_maidr(self) -> dict:
        plt_type = self.type.value
        ax = self.axes

        maidr = {
            MaidrKey.TYPE.value: plt_type,
            MaidrKey.TITLE.value: ax.get_title(),
            MaidrKey.SELECTOR.value: "TODO: Enter your bar plot selector here",
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

    def __extract_level(self) -> list | None:
        return [label.get_text() for label in self.axes.get_xticklabels()]

    def __extract_data(self) -> list | None:
        plot = self.plot

        if isinstance(plot, BarContainer) and isinstance(plot.datavalues, Iterable):
            bc_data = []
            for value in plot.datavalues:
                if isinstance(value, np.integer):
                    bc_data.append(int(value))
                elif isinstance(value, np.floating):
                    bc_data.append(float(value))
                else:
                    bc_data.append(value)
            data = bc_data
        else:
            # TODO: What would be the right exception? ExtractionError?
            raise TypeError("")

        return data
