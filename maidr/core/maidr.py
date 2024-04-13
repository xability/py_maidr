from __future__ import annotations
from typing import Literal

import io
import json
import uuid

from htmltools import HTML, HTMLDocument, RenderedHTML, tags, Tag
from lxml import etree

from matplotlib.figure import Figure

from maidr.core.plot import MaidrPlot


class Maidr:
    def __init__(self, fig: Figure) -> None:
        self._fig = fig
        self._plots = list()

    @property
    def fig(self) -> Figure:
        return self._fig

    @property
    def plots(self) -> list[MaidrPlot]:
        return self._plots

    def render(
        self, *, lib_prefix: str | None = "lib", include_version: bool = True
    ) -> RenderedHTML:
        html = self._create_html_doc()
        return html.render(lib_prefix=lib_prefix, include_version=include_version)

    def save_html(
        self, file: str, *, lib_dir: str | None = "lib", include_version: bool = True
    ) -> str:
        html = self._create_html_doc()
        return html.save_html(file, libdir=lib_dir, include_version=include_version)

    def show(self, renderer: Literal["auto", "ipython", "browser"] = "auto") -> object:
        html = self._create_html_tag()
        return html.show(renderer)

    def _create_html_tag(self) -> Tag:
        svg = self._get_svg()
        maidr = f"\nlet maidr = {json.dumps(self._flatten_maidr(), indent=2)}\n"

        # Inject plot's svg and MAIDR structure into html tag.
        return Maidr._inject_plot(svg, maidr)

    def _create_html_doc(self) -> HTMLDocument:
        return HTMLDocument(self._create_html_tag(), lang="en")

    def _flatten_maidr(self) -> dict | list[dict]:
        maidr = [plot.schema for plot in self._plots]
        return maidr if len(maidr) != 1 else maidr[0]

    def _get_svg(self) -> HTML:
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
            etree.tostring(root_svg, pretty_print=True, encoding="unicode")  # type: ignore # noqa
        )

        return HTML(svg_buffer.getvalue())

    def _set_maidr_id(self, maidr_id: str) -> None:
        for maidr in self._plots:
            maidr.set_id(maidr_id)

    @staticmethod
    def _unique_id() -> str:
        return str(uuid.uuid4())

    @staticmethod
    def _inject_plot(plot: HTML, maidr: str) -> Tag:
        return tags.html(
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
