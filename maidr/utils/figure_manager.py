from __future__ import annotations

from typing import Any

from matplotlib.container import BarContainer
from matplotlib.figure import Figure

from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr import Maidr
from maidr.core.maidr_plot_data_factory import MaidrPlotDataFactory


class FigureManager:
    """
    A helper class responsible for creating and associating `Maidr` objects with
    `Figure` objects.

    Methods
    -------
    create_maidr(fig, plot, plot_type)
        Creates a `Maidr` object with associated plot data based on the plot and its
        type.
    get_figure(artist)
        Retrieves the `Figure` object associated with a given matplotlib `Artist`.

    Warnings
    --------
    End users will typically not have to use this class directly.
    """

    @staticmethod
    def create_maidr(fig: Figure | None, plot: Any, plot_type: list[PlotType]) -> Maidr:
        """
        Creates and returns a Maidr object that encapsulates the figure and its
        associated plot data.

        Parameters
        ----------
        fig : Figure | None
            The figure to which the plot is associated.
        plot : Any
            The plot object containing the plot data.
        plot_type : list[PlotType]
            The list of plot types corresponding to the axes associated with this
            figure.

        Returns
        -------
        Maidr
            The Maidr object.

        Raises
        ------
        ValueError
            - If the figure, axes, plot, or plot type is not found.
            - If the lengths of plots and their types do not match.
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
                f"Lengths of plots {len(fig.axes)} and their {len(plot_type)} types do \
                not match"
            )

        maidr_data = [
            MaidrPlotDataFactory.create(ax, plot, plt_type)
            for ax, plt_type in zip(fig.axes, plot_type)
        ]
        return Maidr(fig, maidr_data)

    @staticmethod
    def get_figure(artist: BarContainer | None) -> Figure | None:
        """
        Retrieves the `Figure` object associated with a given matplotlib `Artist`.

        Parameters
        ----------
        artist : BarContainer | None
            The artist for which to retrieve the figure.

        Returns
        -------
        Figure | None
            The figure associated with the artist, or None if the artist is None or no
            figure is found.
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
