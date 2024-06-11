import pytest

from maidr.core.enum.library import Library
from maidr.core.enum.maidr_key import MaidrKey
from maidr.core.enum.plot_type import PlotType
from maidr.core.figure_manager import FigureManager


@pytest.mark.parametrize("lib", [Library.MATPLOTLIB, Library.SEABORN])
def test_box_plot_data(plot_fixture, lib):
    x_level = ["1", "2", "3"] if lib == Library.MATPLOTLIB else ["0", "1", "2"]
    expected_maidr_data = {
        MaidrKey.TYPE: PlotType.BOX,
        MaidrKey.TITLE: f"Test {lib.value} box title",
        MaidrKey.AXES: {
            MaidrKey.X: {
                MaidrKey.LABEL: f"Test {lib.value} box x label",
                MaidrKey.LEVEL: x_level,
            },
            MaidrKey.Y: {
                MaidrKey.LABEL: f"Test {lib.value} box y label",
            },
        },
        MaidrKey.DATA: [
            {
                MaidrKey.LOWER_OUTLIER: [],
                MaidrKey.MIN: 1.0,
                MaidrKey.Q1: 1.5,
                MaidrKey.Q2: 2.0,
                MaidrKey.Q3: 2.5,
                MaidrKey.MAX: 3.0,
                MaidrKey.UPPER_OUTLIER: [],
            },
            {
                MaidrKey.LOWER_OUTLIER: [],
                MaidrKey.MIN: 4.0,
                MaidrKey.Q1: 4.5,
                MaidrKey.Q2: 5.0,
                MaidrKey.Q3: 5.5,
                MaidrKey.MAX: 6.0,
                MaidrKey.UPPER_OUTLIER: [],
            },
            {
                MaidrKey.LOWER_OUTLIER: [],
                MaidrKey.MIN: 7.0,
                MaidrKey.Q1: 7.5,
                MaidrKey.Q2: 8.0,
                MaidrKey.Q3: 8.5,
                MaidrKey.MAX: 9.0,
                MaidrKey.UPPER_OUTLIER: [],
            },
        ],
    }

    fig, _ = plot_fixture(lib, PlotType.BOX)
    actual_maidr = FigureManager.get_maidr(fig)

    assert actual_maidr.plots[0].schema == expected_maidr_data
