from __future__ import annotations
from typing import Any

import numpy as np
from matplotlib.artist import Artist
from matplotlib.axes import Axes
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
    create_maidr(axs, plot_types)
        Creates a `Maidr` object with associated plot data based on the plot and its
        type.
    get_axes(artist)
        Retrieves the `Axes` object associated with a given matplotlib `Artist`.

    Warnings
    --------
    End users will typically not have to use this class directly.
    """

    figs = dict()

    @classmethod
    def create_maidr(
        cls, axs: list[Axes | None], plot_types: list[PlotType]
    ) -> Maidr | tuple[Maidr]:
        if not axs:
            raise ValueError("No plots found.")
        if None in axs:
            raise ValueError("NoneType found in plots.")
        if plot_types is None:
            raise ValueError("No plot types found.")
        if len(axs) != len(plot_types):
            raise ValueError(
                f"Lengths of plots {len(axs)} and their {len(plot_types)} types do "
                "not match."
            )

        ordered_maidrs = list()
        visited_maidrs = set()

        for ax, plot_type in zip(axs, plot_types):
            fig = ax.get_figure()  # type: ignore
            if fig is None:
                raise ValueError(f"No figure found for axis: {ax}.")

            # maintain the order of unique MAIDRs as extracted from the axes
            maidr = cls.__get_maidr(fig)
            if fig not in visited_maidrs:
                ordered_maidrs.append(maidr)
                visited_maidrs.add(fig)

            # convert the plot to MAIDR representation
            maidr_data = MaidrPlotDataFactory.create(ax, plot_type)  # type: ignore
            maidr.add_plot(maidr_data)

        if len(ordered_maidrs) == 1:
            return ordered_maidrs[0]
        else:
            return tuple(*ordered_maidrs)

    @classmethod
    def __get_maidr(cls, fig: Figure) -> Maidr:
        if fig not in cls.figs.keys():
            cls.figs[fig] = Maidr(fig)
        return cls.figs[fig]

    @staticmethod
    def get_axes(plot: Any) -> list[Axes | None]:
        """
        Extracts axes from various types of matplotlib artists or collections thereof.
        Always returns a list of Axes objects, which may include None if an axes object
        cannot be found for a given artist.
        """
        axs = FigureManager.__get_axes(plot)
        # Ensure output is a flat list of Axes objects
        return axs if isinstance(axs, list) else [axs]

    @staticmethod
    def __get_axes(
        artist: Artist | Axes | BarContainer | list | np.ndarray | None,
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
                (
                    child_artist.axes
                    for child_artist in artist.get_children()
                    if isinstance(child_artist.axes, Axes)
                ),
                None,
            )
        elif isinstance(artist, Artist):
            return artist.axes
        elif isinstance(artist, (list, np.ndarray)):
            # Flatten list to avoid nested lists
            flat_list = []
            for a in artist:
                extracted_axes = FigureManager.__get_axes(a)
                if isinstance(extracted_axes, list):
                    flat_list.extend(extracted_axes)
                else:
                    flat_list.append(extracted_axes)
            return flat_list
