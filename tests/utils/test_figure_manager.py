import matplotlib.pyplot as plt
import seaborn as sns

from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr import Maidr
from maidr.utils.figure_manager import FigureManager

import pytest

from tests.core.enum.library import Library


# test cases for invalid inputs
def test_get_figure_from_none():
    assert FigureManager.get_figure(None) is None


def test_create_maidr_with_none_figure(mocker):
    with pytest.raises(ValueError) as e:
        FigureManager.create_maidr(None, mocker.Mock(), mocker.Mock())
    assert "Figure not found" == str(e.value)


def test_create_maidr_with_none_plot(mocker):
    with pytest.raises(ValueError) as e:
        FigureManager.create_maidr(mocker.Mock(), None, mocker.Mock())
    assert "Plot not found" == str(e.value)


def test_create_maidr_with_none_plot_type(mocker):
    with pytest.raises(ValueError) as e:
        FigureManager.create_maidr(mocker.Mock(), mocker.Mock(), None)  # type: ignore
    assert "Plot type not found" == str(e.value)


def test_create_maidr_with_mismatched_axes_and_plot_types_length(fig_and_axes):
    fig, ax = fig_and_axes
    with pytest.raises(ValueError) as e:
        FigureManager.create_maidr(fig, ax, [PlotType.BAR, PlotType.BAR])
    assert "Lengths of plots 1 and their 2 types do not match" == str(e.value)


# Parametrize the test to run with different libraries and plot types
@pytest.mark.parametrize(
    "lib, plot_type",
    [
        (Library.MATPLOTLIB, PlotType.BAR),
        (Library.SEABORN, PlotType.BAR),
    ],
)
def test_create_maidr_with_single_axes(plot_fixture, lib, plot_type):
    fig, ax = plot_fixture(lib, plot_type)
    maidr = FigureManager.create_maidr(fig, ax, [plot_type])

    assert isinstance(maidr, Maidr)
    assert maidr.fig is fig

    assert len(maidr.data) == len([plot_type]) == 1
    for m_data, p_type in zip(maidr.data, [plot_type]):
        assert m_data.type == p_type


@pytest.mark.parametrize(
    "lib, plot_types",
    [
        (Library.MATPLOTLIB, [PlotType.BAR, PlotType.BAR]),
        (Library.SEABORN, [PlotType.BAR, PlotType.BAR]),
    ],
)
def test_create_maidr_with_multiple_same_axes(plot_fixture, lib, plot_types):
    fig, ax = plot_fixture(lib, plot_types)
    maidr = FigureManager.create_maidr(fig, plot_fixture, plot_types)

    assert isinstance(maidr, Maidr)
    assert maidr.fig is fig

    assert len(maidr.data) == len(plot_types)
    for m_data, p_type in zip(maidr.data, plot_types):
        assert m_data.type == p_type


# group tests related to matplotlib
class TestMatplotlibFigureManager:
    # test `get_figure()` for matplotlib plots
    def test_get_figure_from_subplot_axes(self, fig_and_axes):
        fig, ax = fig_and_axes
        assert FigureManager.get_figure(ax) is fig

    def test_get_figure_from_bar_container(self, fig_and_axes):
        fig, _ = fig_and_axes
        bar = plt.bar([1, 2, 3], [4, 5, 6])
        assert FigureManager.get_figure(bar) is fig


# group tests related to seaborn
class TestSeabornFigureManager:
    # test `get_figure()` for seaborn plots
    def test_get_figure_from_barplot_axes(self, fig_and_axes):
        fig, _ = fig_and_axes
        bar_ax = sns.barplot(x=[1, 2, 3], y=[4, 5, 6])
        assert FigureManager.get_figure(bar_ax) is fig

    def test_get_figure_from_countplot_axes(self, fig_and_axes):
        fig, _ = fig_and_axes
        count_ax = sns.countplot(x=[1, 2, 2, 3, 3, 3])
        assert FigureManager.get_figure(count_ax) is fig
