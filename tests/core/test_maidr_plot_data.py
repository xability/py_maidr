import pytest

from maidr.core.maidr_plot_data import MaidrPlotData


def test_instantiate_abstract_maidr_plot_data(mocker):
    with pytest.raises(TypeError) as e:
        MaidrPlotData(mocker.Mock(), mocker.Mock(), mocker.Mock())  # type: ignore
