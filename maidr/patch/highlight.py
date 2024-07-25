from __future__ import annotations

import wrapt

from matplotlib.collections import PathCollection, QuadMesh
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.backends.backend_svg import XMLWriter

from maidr.core.context_manager import HighlightContextManager


@wrapt.patch_function_wrapper(XMLWriter, "start")
def inject_maidr_attribute(wrapped, _, args, kwargs):
    if HighlightContextManager.is_maidr_element():
        kwargs["maidr"] = "true"
    return wrapped(*args, **kwargs)


def tag_elements(wrapped, instance, args, kwargs):
    with HighlightContextManager.set_maidr_element(instance):
        return wrapped(*args, **kwargs)


wrapt.wrap_function_wrapper(Patch, "draw", tag_elements)
wrapt.wrap_function_wrapper(QuadMesh, "draw", tag_elements)
wrapt.wrap_function_wrapper(Line2D, "draw", tag_elements)
wrapt.wrap_function_wrapper(PathCollection, "draw", tag_elements)
