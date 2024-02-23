import pytest

import matplotlib.pyplot as plt
import seaborn as sns

from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr import Maidr
from maidr.utils.figure_manager import FigureManager


# setup and teardown
@pytest.fixture()  # create new fig, ax for each test
def fig_and_axes():
    fig, ax = plt.subplots()
    yield fig, ax
    plt.close(fig)  # close the figure automatically after each test


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


# group tests related to matplotlib
class TestMatplotlibFigureManager:
    # test `create_maidr()` for matplotlib plots
    def test_create_maidr_with_single_axes(self, fig_and_axes):
        fig, ax = fig_and_axes
        bc = ax.bar([1, 2, 3], [4, 5, 6])
        assert_create_maidr_with_single_axes(fig, bc)

    def test_create_maidr_with_multiple_same_axes(self):
        fig, axs = plt.subplots(1, 2)
        axs[0].bar([1, 2, 3], [1, 2, 3])
        axs[1].bar([4, 5, 6], [4, 5, 6])
        assert_create_maidr_with_multiple_axes(fig, axs)

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
    # test `create_maidr()` for matplotlib plots
    def test_create_maidr_with_single_axes(self, fig_and_axes):
        fig, _ = fig_and_axes
        ax = sns.barplot(x=[1, 2, 3], y=[4, 5, 6])
        assert_create_maidr_with_single_axes(fig, ax)

    def test_create_maidr_with_multiple_same_axes(self):
        fig, axs = plt.subplots(1, 2)
        sns.barplot(x=[1, 2, 3], y=[1, 2, 3], ax=axs[0])
        sns.barplot(x=[4, 5, 6], y=[4, 5, 6], ax=axs[1])
        assert_create_maidr_with_multiple_axes(fig, axs)

    # test `get_figure()` for seaborn plots
    def test_get_figure_from_barplot_axes(self, fig_and_axes):
        fig, _ = fig_and_axes
        bar_ax = sns.barplot(x=[1, 2, 3], y=[4, 5, 6])
        assert FigureManager.get_figure(bar_ax) is fig

    def test_get_figure_from_countplot_axes(self, fig_and_axes):
        fig, _ = fig_and_axes
        count_ax = sns.countplot(x=[1, 2, 2, 3, 3, 3])
        assert FigureManager.get_figure(count_ax) is fig


# common tests
def assert_create_maidr_with_single_axes(fig, plot):
    plot_type = [PlotType.BAR]
    maidr = FigureManager.create_maidr(fig, plot, plot_type)

    assert isinstance(maidr, Maidr)
    assert maidr.fig is fig

    assert len(maidr.data) == len(plot_type) == 1
    for m_data, p_type in zip(maidr.data, plot_type):
        assert m_data.type == p_type


def assert_create_maidr_with_multiple_axes(fig, plots):
    plot_types = [PlotType.BAR, PlotType.BAR]
    maidr = FigureManager.create_maidr(fig, plots, plot_types)

    assert isinstance(maidr, Maidr)
    assert maidr.fig is fig

    assert len(maidr.data) == len(plot_types)
    for m_data, p_type in zip(maidr.data, plot_types):
        assert m_data.type == p_type
