from __future__ import annotations

import io
import json
from uuid import uuid4

from lxml import html, etree
from matplotlib.figure import Figure

from maidr.core.maidr_data import MaidrData


class Maidr:
    def __init__(self, fig: Figure, maidr_data: list[MaidrData]) -> None:
        self._fig = fig
        self._maidr_data = maidr_data
        self._html = self.__create_html()

    def save(self, filename: str) -> None:
        with open(filename, "w") as f:
            f.write(self._html)
        print("Successfully saved the MAIDR file to {0}.".format(filename))

    def __create_html(self) -> str:
        # create svg from `Figure` with maidr.id
        self._svg = self.__get_svg()

        # unflatten maidr if there is only one plot
        maidr = self.__unflatten_maidr()

        # inject svg and maidr into html
        str_html = Maidr.__get_html_template()
        str_html = str_html.replace("<!-- <SVG PLOT> -->", "\n{0}\n".format(self._svg))
        str_html = str_html.replace(
            "<!-- <MAIDR METADATA> -->",
            "\nlet maidr = {0}\n".format(json.dumps(maidr, indent=2)),
        )

        # format html with indentation
        tree_html = html.fromstring(str_html)
        return etree.tostring(tree_html, pretty_print=True, encoding="unicode")

    def __unflatten_maidr(self) -> dict | list[dict]:
        maidr = [m_data.data() for m_data in self._maidr_data]
        return maidr if len(maidr) != 1 else maidr[0]

    def __get_svg(self) -> str:
        svg_buffer = io.StringIO()
        self._fig.savefig(svg_buffer, format="svg")
        str_svg = svg_buffer.getvalue()

        etree.register_namespace("svg", "http://www.w3.org/2000/svg")
        tree_svg = etree.fromstring(str_svg.encode(), parser=None)
        root_svg = None
        # find the `svg` tag and set unique id if not present else use it
        for element in tree_svg.iter(tag="{http://www.w3.org/2000/svg}svg"):
            if "id" not in element.attrib:
                element.attrib["id"] = Maidr.__get_unique_id()
            root_svg = element
            self.__set_maidr_id(element.attrib["id"])
            break

        svg_buffer = io.StringIO()  # Reset the buffer
        svg_buffer.write(
            etree.tostring(root_svg, encoding="unicode", pretty_print=True)
        )

        return svg_buffer.getvalue()

    def __set_maidr_id(self, maidr_id: str) -> None:
        for maidr in self._maidr_data:
            maidr.set_id(maidr_id)

    @staticmethod
    def __get_unique_id() -> str:
        return str(uuid4())

    @staticmethod
    def __get_html_template() -> str:
        return (
            '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/><title>MAIDR'
            '</title><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/maidr/'
            'dist/maidr_style.min.css"/><script src="https://cdn.jsdelivr.net/npm/mai'
            'dr/dist/maidr.min.js"><!-- Core Library --></script></head><body><div><!'
            "-- <SVG PLOT> --></div><script><!-- <MAIDR METADATA> --></script></body>"
            "</html>"
        )
