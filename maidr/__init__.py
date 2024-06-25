__version__ = "0.4.1"

from .core import Maidr
from .core.enum import PlotType
from .patch import barplot, boxplot, heatmap, histogram, lineplot, scatterplot
from .maidr import save_html, show, stacked

__all__ = [
    "save_html",
    "show",
    "stacked",
]
