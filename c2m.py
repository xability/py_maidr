import io
import os
import tempfile
import webbrowser

import matplotlib.pyplot as plt
import seaborn as sns

# Temp original sns.countplot function to override
original_countplot = sns.countplot


def new_countplot(*args, **kwargs):
    plot_data = original_countplot(*args, **kwargs)
    data_y = []
    data_x = []
    x_vars = plot_data.get_xticklabels()
    for x in x_vars:
        data_x.append(x.get_text())
    y_vars = plot_data.patches
    for y in y_vars:
        data_y.append(y.get_height())
    _data = [data_x, data_y]
    # Create an io.BytesIO object and save the seaborn plot as SVG to it
    svg_file = io.BytesIO()
    plt.savefig(svg_file, format="svg", bbox_inches="tight")
    plt.close()
    # Seek to the beginning of the file and read it into a variable
    svg_file.seek(0)
    svg_ = svg_file.read().decode("utf-8")
    createHtmlTemplate(svg_, "bar", _data, "path", 2)


sns.countplot = new_countplot


def createHtmlTemplate(svg_, name, _data, element, slice_count):
    id_attr = 'id="MyChart"'
    # TODO: string replacement may not be reliable. We need to think about directly modifying DOM tree
    # TODO2: Need to remove opening `<xml>` tag
    svg_ = svg_.replace("<svg ", f"<svg {id_attr}")
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
                    element: document.getElementById("MyChart"),
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
                            Array.from(document.querySelectorAll("#MyChart {element}")).slice({slice_count})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  .forEach((elem) => {{
                                elem.style.fill = "#595959";
                            }})
                            document.querySelectorAll("#MyChart {element}")[index+{slice_count}].style.fill = "cyan";
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
        data_y=_data[1],
        element=element,
        slice_count=slice_count,
    )

    # Save the HTML string to a file in the temp directory
    temp_dir = tempfile.gettempdir()
    html_file_path = os.path.join(temp_dir, "my_plot.html")

    with open(html_file_path, "w") as f:
        f.write(html_template)

    print(f"HTML file saved at: {html_file_path}")

    # Open in the default web browser
    webbrowser.open("file://" + os.path.realpath(html_file_path))
