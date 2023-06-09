import datetime
import io
import os
import tempfile
import webbrowser

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from lxml import etree

# Temp original sns.countplot function to override
sns_countplot = sns.countplot


def countplot(*args, **kwargs):
    browse = kwargs.pop("browse", True)
    file = kwargs.pop("file", None)

    plot_data = sns_countplot(*args, **kwargs)

    data_y = []
    data_x = []
    x_vars = plot_data.get_xticklabels()
    for x in x_vars:
        data_x.append(x.get_text())
    y_vars = plot_data.patches
    for y in y_vars:
        data_y.append(y.get_height())
    _data = [data_x, data_y]
    create_html_template("bar", _data, "path", 2, browse=browse, file=file)
    return plot_data


sns.countplot = countplot

# Barplot

# Temp original sns.barplot function to override
sns_barplot = sns.barplot


def barplot(*args, **kwargs):
    browse = kwargs.pop("browse", True)
    file = kwargs.pop("file", None)

    plot_data = sns_barplot(*args, **kwargs)

    # The y values can be extracted as follows:
    data_y = [patch.get_height() for patch in plot_data.patches]

    # The x labels can be extracted using get_xticklabels()
    data_x = [label.get_text() for label in plot_data.get_xticklabels()]

    _data = [data_x, data_y]
    create_html_template("bar", _data, "path", 2, browse=browse, file=file)
    return plot_data


sns.barplot = barplot

# Scatterplot
sns_scatterplot = sns.scatterplot


def scatterplot(*args, **kwargs):
    browse = kwargs.pop("browse", True)
    file = kwargs.pop("file", None)
    plot_data = sns_scatterplot(*args, **kwargs)
    data_y = []
    data_x = []
    data_sc = plot_data.collections[0].get_offsets()
    for points in data_sc:
        data_y.append(points.data[1])
        data_x.append(points.data[0])
    _data = [data_x, data_y]
    create_html_template("scatter", _data, "use", 0, browse=browse, file=file)
    return plot_data


sns.scatterplot = scatterplot

# Lineplot

# lineplot
sns_lineplot = sns.lineplot


def lineplot(*args, **kwargs):
    browse = kwargs.pop("browse", True)
    file = kwargs.pop("file", None)
    plot_data = sns_lineplot(*args, **kwargs)

    data_y = []
    data_x = []
    for data in plot_data.lines:
        y = data.get_ydata()
        data_y.append(y)
        x = data.get_xdata()
        data_x.append(x)
    x = np.array(data_x[0]).tolist()
    y = np.array(data_y[0]).tolist()
    _data = [x, y]
    create_html_template("line", _data, "path", 14, browse=browse, file=file)
    return plot_data


sns.lineplot = lineplot


def create_html_template(name, _data, element, slice_count, browse, file):
    # Create an io.BytesIO object and save the seaborn plot as SVG to it
    svg_file = io.BytesIO()
    plt.savefig(svg_file, format="svg", bbox_inches="tight")
    plt.close()
    # Seek to the beginning of the file and read it into a variable
    svg_file.seek(0)
    svg_data = svg_file.read().decode("utf-8")

    # Parse the SVG data
    svg_tree = etree.fromstring(svg_data.encode("utf-8"))

    # Find and remove all <xml> tags
    for xml_tag in svg_tree.xpath("//xml"):
        xml_tag.getparent().remove(xml_tag)

    # Find the opening <svg> tag and add an id attribute
    # Current date and time
    now = datetime.datetime.now()

    # Create an id
    id = name + now.strftime("%Y%m%d%H%M%S")

    svg_tree.set("id", id)

    # Serialize the modified SVG back into a string
    svg_ = etree.tostring(svg_tree, pretty_print=True, method="xml").decode("utf-8")

    html_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>

            <script src="https://cdn.jsdelivr.net/npm/chart2music"></script>
        </head>
        <body>
            <div>
                {svg}
            </div>
            <div id="cc"></div>

            <script>
                const x = {data_x};
                const err = c2mChart({{
                    type: "{name}",
                    element: document.getElementById("{id}"),
                    cc: document.getElementById("cc"),
                    axes: {{
                        x: {{
                            label: "class",
                            format: (index) => x[index]
                        }},
                        y: {{
                            label: "count",
                            minimum: 0
                        }}
                    }},
                    data: {data_y},
                    options: {{
                        onFocusCallback: ({{index}}) => {{
                            Array.from(document.querySelectorAll("#{id} {element}")).slice({slice_count})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  .forEach((elem) => {{
                                elem.style.fill = "#595959";
                            }})
                            document.querySelectorAll("#{id} {element}")[index+{slice_count}].style.fill = "cyan";
                        }}
                    }}
                }});
                if(err){{
                    console.error(err);
                }}
            </script>
        </body>
        </html>
        """

    html_template = html_template.format(
        svg=svg_,
        data_x=_data[0],
        name=name,
        id=id,
        data_y=_data[1],
        element=element,
        slice_count=slice_count,
    )

    if file is None:
        # Save the HTML string to a file in the temp directory
        temp_dir = tempfile.gettempdir()
        html_file_path = os.path.join(temp_dir, "my_plot.html")
    else:
        html_file_path = file

    with open(html_file_path, "w") as f:
        f.write(html_template)

    # Open in the default web browser
    if browse:
        webbrowser.open("file://" + os.path.realpath(html_file_path))
    else:
        print(f"HTML file saved at: {html_file_path}")
