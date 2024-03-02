from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType
from maidr.core.plot.bar_plot_data import BarPlotData

import pytest

from tests.core.enum.library import Library


@pytest.mark.parametrize("lib", [Library.MATPLOTLIB, Library.SEABORN])
def test_bar_plot_data(plot_fixture, lib):
    expected_maidr_data = {
        MaidrKey.TYPE.value: PlotType.BAR.value,
        MaidrKey.TITLE.value: f"Test {lib.value} title",
        MaidrKey.AXES.value: {
            MaidrKey.X.value: {
                MaidrKey.LABEL.value: f"Test {lib.value} x label",
                MaidrKey.LEVEL.value: ["1", "2", "3"],
            },
            MaidrKey.Y.value: {
                MaidrKey.LABEL.value: f"Test {lib.value} y label",
            },
        },
        MaidrKey.DATA.value: [4, 5, 6],
    }

    _, ax = plot_fixture(lib, PlotType.BAR)
    actual_maidr = BarPlotData(ax.pop())

    assert actual_maidr.data() == expected_maidr_data
