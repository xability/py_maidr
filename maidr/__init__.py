__version__ = (
    "0.1.0"  # __version__ will be automatically updated by python-semantic-release
)

from .core import Maidr
from .core.enum import PlotType
from .maidr import bar, box, count, heat, hist, line, scatter, stacked

__all__ = [
    "bar",
    "box",
    "count",
    "heat",
    "hist",
    "line",
    "scatter",
    "stacked",
]
