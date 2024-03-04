from enum import Enum


class PlotType(Enum):
    """
    Enumeration class for different plot types.
    Each plot type corresponds to a different kind of MAIDR representation.
    """

    BAR = "bar"
    HEAT = "heat"
    HIST = "hist"
    LINE = "line"
