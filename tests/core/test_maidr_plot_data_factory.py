import pytest

from maidr.core.enum.plot_type import PlotType
from maidr.core.plot_data.bar_plot_data import BarPlotData
from maidr.core.maidr_plot_data_factory import MaidrPlotDataFactory


# test invalid inputs
def test_create_with_invalid_plot_type(mocker):
    with pytest.raises(TypeError) as e:
        _ = MaidrPlotDataFactory.create(mocker.Mock(), mocker.Mock(), None)  # type: ignore # noqa
        assert "Unsupported plot type: None" == str(e.value)


# test valid inputs
@pytest.mark.parametrize(
    "plot_type, expected_plot_data",
    [
        (PlotType.BAR, BarPlotData),
    ],
)
def test_create_plot_data(mocker, plot_type, expected_plot_data):
    mock_plot_data = mocker.Mock(spec=expected_plot_data)
    mocker.patch(
        f"maidr.core.maidr_plot_data_factory.{expected_plot_data.__name__}",
        return_value=mock_plot_data,
    )

    actual_plot_data = MaidrPlotDataFactory.create(mocker.Mock(), plot_type)

    assert isinstance(actual_plot_data, expected_plot_data)
