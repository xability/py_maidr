from __future__ import annotations

import io
import json
from uuid import uuid4

from lxml import etree, html
from matplotlib.figure import Figure

from maidr.core.maidr_plot_data import MaidrPlotData


class Maidr:
    """
    A container for the figure and its MAIDR data representation.

    This class allows the conversion of matplotlib figures into interactive MAIDR
    visualizations. It handles the generation of SVG representations of the plots,
    assembles the MAIDR data structure, and packages everything into a single HTML file.

    Methods
    -------
    save(filename: str)
        Saves the MAIDR content as an HTML file with the specified filename.

    Notes
    -----
    End users should use the maidr API to create an instance of this class.
    """

    def __init__(self, fig: Figure) -> None:
        """
        Initializes a MAIDR object with the given matplotlib figure and MAIDR data.

        Parameters
        ----------
        fig : Figure
            The matplotlib Figure object to be used for plotting.
        """
        self._fig = fig
        self._maidr_data = list()

    @property
    def fig(self) -> Figure:
        return self._fig

    @property
    def data(self) -> list[MaidrPlotData]:
        return self._maidr_data

    def add_plot(self, maidr_data: MaidrPlotData) -> None:
        self._maidr_data.append(maidr_data)

    def save(self, filename: str) -> None:
        """
        Saves the MAIDR file as HTML.

        The method writes the HTML representation of the MAIDR object, including the SVG
        visualization of the figure, the extracted MAIDR metadata, and the core MAIDR JS
        library, to the specified file.

        Parameters
        ----------
        filename : str
            The name of the file to which the MAIDR HTML content should be saved.
        """
        with open(filename, "w") as f:
            f.write(self.__create_html())
        print(f"Successfully saved the MAIDR file to {filename}.")

    def __create_html(self) -> str:
        """
        Create an HTML string with SVG representation of the plot and MAIDR metadata.

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
        str_html = str_html.replace("<!-- <SVG PLOT> -->", f"\n{self._svg}\n")
        str_html = str_html.replace(
            "<!-- <MAIDR METADATA> -->",
            f"\nlet maidr = {json.dumps(maidr, indent=2)}\n",
        )

        # format html with indentation
        tree_html = html.fromstring(str_html)
        return etree.tostring(tree_html, pretty_print=True, encoding="unicode")  # type: ignore # noqa

    def __unflatten_maidr(self) -> dict | list[dict]:
        """
        Unflatten the MAIDR data into a dictionary format.

        Returns
        -------
        dict | list[dict]
            The JSON structured MAIDR data, potentially as a single dictionary or a
            list of dictionaries.
        """
        maidr = [m_data.data() for m_data in self._maidr_data]
        return maidr if len(maidr) != 1 else maidr[0]

    def __get_svg(self) -> str:
        """
        Creates an SVG representation of the matplotlib figure.

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
        svg_buffer.write(
            etree.tostring(root_svg, pretty_print=True, encoding="unicode")  # type: ignore # noqa
        )

        return svg_buffer.getvalue()

    def __set_maidr_id(self, maidr_id: str) -> None:
        """
        Sets a unique `maidr_id` for all MAIDR objects.

        Parameters
        ----------
        maidr_id : str
            The maidr_id to be set for all maidr objects.
        """
        for maidr in self._maidr_data:
            maidr.set_id(maidr_id)

    @staticmethod
    def __get_unique_id() -> str:
        """
        Create a unique identifier using UUID.

        Returns
        -------
        str
            A unique identifier string.
        """
        return str(uuid4())

    @staticmethod
    def __get_html_template() -> str:
        """
        Retrieves the HTML template for embedding the SVG and MAIDR metadata.

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
