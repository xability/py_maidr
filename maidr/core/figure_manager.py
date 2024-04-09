from __future__ import annotations
from typing import Any

from matplotlib.artist import Artist
from matplotlib.axes import Axes
from matplotlib.container import BarContainer
from matplotlib.figure import Figure

from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr import Maidr
from maidr.core.maidr_plot_factory import MaidrPlotFactory


class FigureManager:
    figs = dict()

    @classmethod
    def create_maidr(cls, ax: Axes, plot_type: PlotType, **kwargs) -> Maidr:
        if ax is None:
            raise ValueError("No plot found.")
        if plot_type is None:
            raise ValueError("No plot type found.")
        if ax.get_figure() is None:
            raise ValueError(f"No figure found for axis: {ax}.")

        # convert the plot to MAIDR representation
        maidr = cls.__get_maidr(ax.get_figure())
        plot = MaidrPlotFactory.create(ax, plot_type, **kwargs)
        maidr.add_plot(plot)

        return maidr

    @classmethod
    def __get_maidr(cls, fig: Figure) -> Maidr:
        if fig not in cls.figs.keys():
            cls.figs[fig] = Maidr(fig)
        return cls.figs[fig]

    @staticmethod
    def get_axes(
        artist: Artist | Axes | BarContainer | dict | None,
    ) -> Any:
        """
        Recursively extracts Axes objects from the input artist or collection of artists.
        """
        if artist is None:
            return None
        elif isinstance(artist, Axes):
            return artist
        elif isinstance(artist, BarContainer):
            # Get axes from the first occurrence of any child artist
            return next(
                child_artist.axes
                for child_artist in artist.get_children()
                if isinstance(child_artist.axes, Axes)
            )
        elif isinstance(artist, Artist):
            return artist.axes
        elif isinstance(artist, dict):
            return next(
                _artist.axes
                for _artists in artist.values()
                for _artist in _artists
                if isinstance(_artist.axes, Axes)
            )
