from __future__ import annotations

import io
import json
from uuid import uuid4

from lxml import etree, html
from matplotlib.figure import Figure

from maidr.core.maidr_data import MaidrData


class Maidr:
    """
    The MAIDR class represents a MAIDR object.

    Parameters
    ----------
    fig : Figure
        The matplotlib Figure object to be used for plotting.
    maidr_data : list[MaidrData]
        A list of MaidrData objects containing the data for MAIDR.

    Attributes
    ----------
    _fig : Figure
        The matplotlib Figure object used for plotting.
    _maidr_data : list[MaidrData]
        A list of MaidrData objects containing the data for MAIDR.
    _html : str
        The HTML string with SVG plot and maidr metadata.

    Methods
    -------
    save(filename: str) -> None:
        Save the MAIDR file as HTML.
    __create_html() -> str:
        Create an HTML string with SVG plot and maidr metadata.
    __unflatten_maidr() -> dict | list[dict]:
        Unflattens the MAIDR data.
    __get_svg() -> str:
        Generate and return the SVG representation of the figure.
    __set_maidr_id(maidr_id: str) -> None:
        Set the maidr_id for all maidr objects in the _maidr_data list.
    __get_unique_id() -> str:
        Generate a unique identifier using UUID.
    __get_html_template() -> str:
        Returns the HTML template for the MAIDR application.
    """

    def __init__(self, fig: Figure, maidr_data: list[MaidrData]) -> None:
        """
        Initialize the MAIDR object.

        Parameters
        ----------
        fig : Figure
            The matplotlib Figure object to be used for plotting.
        maidr_data : list[MaidrData]
            A list of MaidrData objects containing the data for MAIDR.

        Returns
        -------
        None
        """
        self._fig = fig
        self._maidr_data = maidr_data
        self._html = self.__create_html()

    def save(self, filename: str) -> None:
        """
        Save the MAIDR file as HTML.

        Parameters
        ----------
        filename : str
            The name of the file to save.

        Returns
        -------
        None
        """
        with open(filename, "w") as f:
            f.write(self._html)
        print("Successfully saved the MAIDR file to {0}.".format(filename))

    def __create_html(self) -> str:
        """
        Create an HTML string with SVG plot and maidr metadata.

        Returns
        -------
        str
            The HTML string with SVG plot and maidr metadata.
        """
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
        return etree.tostring(tree_html)

    def __unflatten_maidr(self) -> dict | list[dict]:
        """
        Unflattens the MAIDR data.

        Returns
        -------
        dict | list[dict]
            The unflattened MAIDR data.
        """
        maidr = [m_data.data() for m_data in self._maidr_data]
        return maidr if len(maidr) != 1 else maidr[0]

    def __get_svg(self) -> str:
        """
        Generate and return the SVG representation of the figure.

        Returns
        -------
        str
            The SVG representation of the figure.
        """
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
        svg_buffer.write(etree.tostring(root_svg))

        return svg_buffer.getvalue()

    def __set_maidr_id(self, maidr_id: str) -> None:
        """
        Set the maidr_id for all maidr objects in the _maidr_data list.

        Parameters
        ----------
        maidr_id : str
            The maidr_id to be set for all maidr objects.

        Returns
        -------
        None
        """
        for maidr in self._maidr_data:
            maidr.set_id(maidr_id)

    @staticmethod
    def __get_unique_id() -> str:
        """
        Generate a unique identifier using UUID.

        Returns
        -------
        str
            A string representing a unique identifier.
        """
        return str(uuid4())

    @staticmethod
    def __get_html_template() -> str:
        """
        Returns the HTML template for the MAIDR application.

        Returns
        -------
        str
            The HTML template string.
        """
        return (
            '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/><title>MAIDR'
            '</title><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/maidr/'
            'dist/maidr_style.min.css"/><script src="https://cdn.jsdelivr.net/npm/mai'
            'dr/dist/maidr.min.js"><!-- Core Library --></script></head><body><div><!'
            "-- <SVG PLOT> --></div><script><!-- <MAIDR METADATA> --></script></body>"
            "</html>"
        )
