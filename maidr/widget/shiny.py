from __future__ import annotations

from typing import Any, Callable, Coroutine, Optional

from shiny.render import ui
from shiny.types import Jsonifiable

import maidr


class render_maidr(ui):
    """
    A custom UI rendering class for Maidr objects in Shiny applications.

    This class extends the Shiny UI rendering functionality to handle Maidr objects.

    Attributes
    ----------
    fn : Callable[[], Coroutine[Any, Any, Optional[Any]]]
        An asynchronous function that returns the value to be rendered.

    Methods
    -------
    render()
        Asynchronously renders the Maidr object.
    """

    def __init__(self, fn: Callable[[], Coroutine[Any, Any, Optional[Any]]]):
        """
        Initialize the render_maidr instance.

        Parameters
        ----------
        fn : Callable[[], Coroutine[Any, Any, Optional[Any]]]
            An asynchronous function that returns the value to be rendered.
        """
        super().__init__(fn)

    async def render(self) -> Optional[Jsonifiable]:
        """
        Asynchronously render the Maidr object.

        This method calls the provided function, renders the result using Maidr,
        and transforms it into a Jsonifiable format.

        Returns
        -------
        Optional[Jsonifiable]
            The rendered and transformed Maidr object, or
            None if the initial value is None.
        """
        initial_value: Optional[Any] = await self.fn()
        if initial_value is None:
            return None

        maidr_rendered: Any = maidr.render(initial_value)
        transformed: Jsonifiable = await self.transform(maidr_rendered)
        return transformed
