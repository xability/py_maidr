from __future__ import annotations

import io
import json
import uuid
from typing import Literal

from htmltools import HTML, HTMLDocument, Tag, tags
from lxml import etree
from matplotlib.figure import Figure

from maidr.core.context_manager import HighlightContextManager
from maidr.core.plot import MaidrPlot
from maidr.util.environment import Environment


class Maidr:
    """
    A class to handle the rendering and interaction of matplotlib figures with additional metadata.

    Attributes
    ----------
    _fig : Figure
        The matplotlib figure associated with this instance.
    _plots : list[MaidrPlot]
        A list of MaidrPlot objects which hold additional plot-specific configurations.

    Methods
    -------
    render(lib_prefix=None, include_version=True)
        Creates and returns a rendered HTML representation of the figure.
    save_html(file, lib_dir=None, include_version=True)
        Saves the rendered HTML representation to a file.
    show(renderer='auto')
        Displays the rendered HTML content in the specified rendering context.
    """

    def __init__(self, fig: Figure) -> None:
        """Create a new Maidr for the given ``matplotlib.figure.Figure``."""
        self._fig = fig
        self._plots = []

    @property
    def fig(self) -> Figure:
        """Return the ``matplotlib.figure.Figure`` associated with this object."""
        return self._fig

    @property
    def plots(self) -> list[MaidrPlot]:
        """Return the list of plots extracted from the ``fig``."""
        return self._plots

    def render(self) -> Tag:
        """Return the maidr plot inside an iframe."""
        return self._create_html_tag()

    def save_html(
        self, file: str, *, lib_dir: str | None = "lib", include_version: bool = True
    ) -> str:
        """
        Save the HTML representation of the figure with MAIDR to a file.

        Parameters
        ----------
        file : str
            The file to save to.
        lib_dir : str, default="lib"
            The directory to save the dependencies to
            (relative to the file's directory).
        include_version : bool, default=True
            Whether to include the version number in the dependency folder name.
        """
        html = self._create_html_doc()
        return html.save_html(file, libdir=lib_dir, include_version=include_version)

    def show(self, renderer: Literal["auto", "ipython", "browser"] = "auto") -> object:
        """
        Preview the HTML content using the specified renderer.

        Parameters
        ----------
        renderer : Literal["auto", "ipython", "browser"], default="auto"
            The renderer to use for the HTML preview.
        """
        html = self._create_html_tag()
        if Environment.is_interactive_shell() and not Environment.is_notebook():
            return html.show("browser")
        return html.show(renderer)

    def clear(self):
        self._plots = []

    def destroy(self) -> None:
        del self._plots
        del self._fig

    def _create_html_tag(self) -> Tag:
        """Create the MAIDR HTML using HTML tags."""
        tagged_elements = [element for plot in self._plots for element in plot.elements]
        with HighlightContextManager.set_maidr_elements(tagged_elements):
            svg = self._get_svg()
        maidr = f"\nlet maidr = {json.dumps(self._flatten_maidr(), indent=2)}\n"

        # Inject plot's svg and MAIDR structure into html tag.
        return Maidr._inject_plot(svg, maidr)

    def _create_html_doc(self) -> HTMLDocument:
        """Create an HTML document from Tag objects."""
        return HTMLDocument(self._create_html_tag(), lang="en")

    def _flatten_maidr(self) -> dict | list[dict]:
        """Return a single plot schema or a list of schemas from the Maidr instance."""
        maidr = [plot.schema for plot in self._plots]
        return maidr if len(maidr) != 1 else maidr[0]

    def _get_svg(self) -> HTML:
        """Extract the chart SVG from ``matplotlib.figure.Figure``."""
        svg_buffer = io.StringIO()
        self._fig.savefig(svg_buffer, format="svg")
        str_svg = svg_buffer.getvalue()

        etree.register_namespace("svg", "http://www.w3.org/2000/svg")
        tree_svg = etree.fromstring(str_svg.encode(), parser=None)
        root_svg = None
        # Find the `svg` tag and set unique id if not present else use it.
        for element in tree_svg.iter(tag="{http://www.w3.org/2000/svg}svg"):
            if "id" not in element.attrib:
                element.attrib["id"] = Maidr._unique_id()
            root_svg = element
            self._set_maidr_id(element.attrib["id"])
            break

        svg_buffer = io.StringIO()  # Reset the buffer
        svg_buffer.write(
            etree.tostring(
                root_svg, pretty_print=True, encoding="unicode"  # type: ignore
            )
        )

        return HTML(svg_buffer.getvalue())

    def _set_maidr_id(self, maidr_id: str) -> None:
        """Set a unique identifier to each ``MaidrPlot``."""
        for maidr in self._plots:
            maidr.set_id(maidr_id)

    @staticmethod
    def _unique_id() -> str:
        """Generate a unique identifier string using UUID4."""
        return str(uuid.uuid4())

    @staticmethod
    def _inject_plot(plot: HTML, maidr: str) -> Tag:
        """Embed the plot and associated MAIDR scripts into the HTML structure."""
        base_html = tags.html(
            tags.head(
                tags.meta(charset="UTF-8"),
                tags.title("MAIDR"),
                tags.link(
                    rel="stylesheet",
                    href="https://cdn.jsdelivr.net/npm/maidr/dist/maidr_style.min.css",
                ),
                tags.script(
                    type="text/javascript",
                    src="https://cdn.jsdelivr.net/npm/maidr/dist/maidr.min.js",
                ),
            ),
            tags.body(
                tags.div(plot),
            ),
            tags.script(maidr),
        )

        unique_id = "iframe_" + Maidr._unique_id()

        # Embed the rendering into an iFrame for proper working of JS library.
        base_html = tags.iframe(
            id=unique_id,
            srcdoc=str(base_html.get_html_string()),
            width="100%",
            height="100%",
            scrolling="auto",
            style="background-color: #fff",
            frameBorder=0,
            onload="""
                this.style.height = this.contentWindow.document.body.scrollHeight +
                100 + 'px';
            """
            + Environment.initialize_llm_secrets(unique_id),
        )

        return base_html
