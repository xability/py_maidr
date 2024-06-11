from __future__ import annotations

import pytest
from matplotlib import pyplot as plt

from maidr.core.enum.plot_type import PlotType
from maidr.core.enum.library import Library
from tests.fixture.matplotlib_factory import MatplotlibFactory
from tests.fixture.seaborn_factory import SeabornFactory


# setup and teardown
@pytest.fixture
def plot_fixture():
    factories = {
        Library.MATPLOTLIB: MatplotlibFactory(),
        Library.SEABORN: SeabornFactory(),
    }

    def create_plot(lib: Library, plot_type: PlotType | list[PlotType]):
        if lib not in factories:
            raise ValueError(f"Unsupported library: {lib}")
        if not isinstance(plot_type, list):
            plot_type = [plot_type]

        factory = factories[lib]
        with factory.create_plot(plot_type) as plot:
            return plot

    return create_plot


@pytest.fixture
def axes():
    fig, ax = plt.subplots()
    yield ax
    plt.close(fig)
