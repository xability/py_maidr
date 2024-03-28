from __future__ import annotations

from matplotlib.axes import Axes
from matplotlib.cm import ScalarMappable
from matplotlib.lines import Line2D

from maidr.core.enum.maidr_key import MaidrKey


class ContainerExtractorMixin:
    @staticmethod
    def extract_container(
        ax: Axes,
        container_type: type,
        include_all: bool = False,
    ) -> type | list[type] | None:
        if ax is None or ax.containers is None:
            return None

        if include_all:
            return [
                container
                for container in ax.containers
                if isinstance(container, container_type)
            ]

        return next(
            container
            for container in ax.containers
            if isinstance(container, container_type)
        )


class LevelExtractorMixin:
    @staticmethod
    def extract_level(ax: Axes, key: MaidrKey = MaidrKey.X) -> list | None:
        if ax is None:
            return None

        level = None
        if MaidrKey.X == key:
            level = [label.get_text() for label in ax.get_xticklabels()]
        elif MaidrKey.Y == key:
            level = [label.get_text() for label in ax.get_yticklabels()]
        elif MaidrKey.FILL == key:
            level = [container.get_label() for container in ax.containers]

        return level


class LineExtractorMixin:
    @staticmethod
    def extract_line(ax: Axes) -> Line2D | None:
        if ax is None or ax.get_lines() is None:
            return None

        return ax.get_lines()[-1]


class CollectionExtractorMixin:
    @staticmethod
    def extract_collection(ax: Axes, collection_type: type) -> type | None:
        if ax is None or ax.collections is None:
            return None

        for collection in ax.collections:
            if isinstance(collection, collection_type):
                return collection


class ScalarMappableExtractorMixin:
    @staticmethod
    def extract_scalar_mappable(ax: Axes) -> ScalarMappable | None:
        if ax is None or ax.get_children() is None:
            return None

        for sm in ax.get_children():
            if isinstance(sm, ScalarMappable):
                return sm
