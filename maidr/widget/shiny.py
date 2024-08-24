from __future__ import annotations

from shiny.render import ui
from shiny.types import Jsonifiable

import maidr


class render_maidr(ui):
    """
    A custom UI rendering class for Maidr objects in Shiny applications.

    This class extends the Shiny UI rendering functionality to handle Maidr objects.

    Methods
    -------
    render()
        Asynchronously renders the Maidr object.
    """

    async def render(self) -> Jsonifiable:
        """Return maidr rendered object for a given plot."""
        initial_value = await self.fn()
        if initial_value is None:
            return None

        maidr_rendered = maidr.render(initial_value)
        transformed = await self.transform(maidr_rendered)
        return transformed
