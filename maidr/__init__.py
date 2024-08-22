__version__ = "0.6.0"

from .core import Maidr
from .core.enum import PlotType
from .patch import (
    barplot,
    boxplot,
    clear,
    heatmap,
    highlight,
    histogram,
    lineplot,
    scatterplot,
)
from .api import close, save_html, show, stacked

__all__ = [
    "close",
    "save_html",
    "show",
    "stacked",
]
