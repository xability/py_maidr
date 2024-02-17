from __future__ import annotations

from matplotlib.container import BarContainer
from matplotlib.figure import Figure

from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr import Maidr
from maidr.core.maidr_data_factory import MaidrDataFactory


class FigureManager:
    """
    A class that manages figures and creates Maidr objects.

    Methods:
    - create_maidr(fig, plot, plot_type): Create a Maidr object.
    - get_figure(artist): Get the figure associated with the given artist.
    """

    @staticmethod
    def create_maidr(
        fig: Figure | None, plot, plot_type: list[PlotType] | None
    ) -> Maidr:
        """
        Create a Maidr object.

        Parameters:
        - fig (Figure | None): The figure object.
        - plot: The plot object.
        - plot_type (list[PlotType] | None): The list of plot types.

        Returns:
        - Maidr: The Maidr object.

        Raises:
        - ValueError: If the figure, axes, plot, or plot type is not found.
        - ValueError: If the lengths of plots and their types do not match.
        """
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
        """
        Get the figure associated with the given artist.

        Parameters:
            artist (BarContainer | None): The artist for which to retrieve the figure.

        Returns:
            Figure | None: The figure associated with the artist, or None if the artist is None or no figure is found.
        """
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
