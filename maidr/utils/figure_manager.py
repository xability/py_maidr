from __future__ import annotations

from matplotlib.container import BarContainer
from matplotlib.figure import Figure

from maidr.core.maidr import Maidr
from maidr.core.maidr_data_factory import MaidrDataFactory
from maidr.core.enum.plot_type import PlotType


class FigureManager:
    @staticmethod
    def create_maidr(
        fig: Figure | None, plot, plot_type: list[PlotType] | None
    ) -> Maidr:
        if not fig:
            raise ValueError("Figure not found")
        if not fig.axes:
            raise ValueError("Axes not found")
        if not plot:
            raise ValueError("Plot not found")
        if not plot_type:
            raise ValueError("Plot type not found")
        if len(fig.axes) != len(plot_type):
            raise ValueError(
                "Lengths of plots {0} and their {1} types do not match".format(
                    len(fig.axes), len(plot_type)
                )
            )

        maidr_data = [
            MaidrDataFactory.create(ax, plot, plt_type)
            for ax, plt_type in zip(fig.axes, plot_type)
        ]
        return Maidr(fig, maidr_data)

    @staticmethod
    def get_figure(artist: BarContainer | None) -> Figure | None:
        if not artist:
            return None

        fig = None
        # bar container - get figure from the first occurrence of any artist
        if isinstance(artist, BarContainer):
            fig = next(
                (
                    child_artist.get_figure()
                    for child_artist in artist.get_children()
                    if child_artist.get_figure()
                ),
                None,
            )

        return fig
