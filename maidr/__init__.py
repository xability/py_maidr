__version__ = "0.4.2"

from .core import Maidr
from .core.enum import PlotType
from .patch import barplot, boxplot, clear, heatmap, histogram, lineplot, scatterplot
from .maidr import close, save_html, show, stacked

__all__ = [
    "close",
    "save_html",
    "show",
    "stacked",
]
