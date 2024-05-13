import pytest

from maidr.core.plot.maidr_plot import MaidrPlot


def test_instantiate_abstract_maidr_plot_data(mocker):
    with pytest.raises(TypeError) as _:
        MaidrPlot(mocker.Mock(), mocker.Mock(), mocker.Mock())  # type: ignore
