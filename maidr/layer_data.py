import numpy as np


class LayerData:
    def __init__(self, data):
        self.plot_data = data

    def dataplotCount(self, name):
        if not self.plot_data.has_data():
            return "Plot is Empty!"

        data_y = []
        data_x = []

        x_vars = self.plot_data.get_xticklabels()
        for x in x_vars:
            data_x.append(x.get_text())

        y_vars = self.plot_data.patches
        for y in y_vars:
            data_y.append(y.get_height())

        _data = [data_x, data_y]
        # self.createHtmlTemplate(name, _data, "path", 2)
        self.createMaidrTemplate(name, _data, "path", 2, len(data_y))

        return _data

    def dataplotBar(self, name):
        _data = self.dataplotCount(name)
        self.createMaidrTemplate(name, _data, "path", 2, len(_data[1]))

        return _data

    def dataplotScatter(self, name):
        if not self.plot_data.has_data():
            return "Plot is Empty!"

        data_y = []
        data_x = []
        data_sc = self.plot_data.collections[0].get_offsets()
        for points in data_sc:
            data_y.append(points.data[1])
            data_x.append(points.data[0])

        _data = [data_x, data_y]

        # added for maidr
        data = []
        for i in range(len(data_x)):
            data.append({"x": data_x[i], "y": data_y[i]})

        self.createMaidrTemplateScatter(name, data, "use", 0, len(data_y))

        return _data

    def dataplotLine(self, name):
        if not self.plot_data.has_data():
            return "Plot is Empty!"

        data_y = []
        data_x = []
        for data in self.plot_data.lines:
            y = data.get_ydata()
            data_y.append(y)

            x = data.get_xdata()
            data_x.append(x)

        x = np.array(data_x[0]).tolist()
        y = np.array(data_y[0]).tolist()
        _data = [x, y]
        print(_data)
        self.createHtmlTemplateLine(name, _data, "path", 14)

        return _data

    def dataplotHeat(self, name):
        if not self.plot_data.has_data():
            return "Plot is Empty!"

        x_ticks = self.plot_data.get_xticklabels()

        y_ticks = self.plot_data.get_yticklabels()

        x_labels = []
        for x in x_ticks:
            x_labels.append(x.get_text())

        y_labels = []
        for y in y_ticks:
            y_labels.append(y.get_text())

        print("axes", x_labels, y_labels)

        datapoints = self.plot_data.collections[0].get_array()

        # x_ax_data = {}
        # for i in range(len(x_labels)):
        #     year = []
        #     for j in range(len(y_labels)):
        #         index = j * len(x_labels) + i
        #         data_value = datapoints[index]
        #         year.append(data_value)
        #     x_ax_data.update({y_labels[i]: year})

        x_ax_data = []
        for i in range(len(x_labels)):
            year = []
            for j in range(len(y_labels)):
                index = j * len(x_labels) + i
                data_value = datapoints[index]
                year.append(data_value)
            x_ax_data.append(year)

        _data = []
        data_x = x_labels
        slices = y_labels
        data_y = x_ax_data

        _data = [data_x, slices, data_y]
        self.createMaidrTemplateHeat(
            name, _data, "path", 2, (len(data_x) * len(slices))
        )

        return

    def dataplotBox(self, name):
        if not self.plot_data.has_data():
            return "Plot is Empty!"

        print("Hi", self.plot_data.artists, len(self.plot_data.artists))
        print("Hi", self.plot_data.lines, len(self.plot_data.lines))

        for i in self.plot_data.lines:
            print(i)

        # _data = [data_x, data_y]
        # # print(_data)
        # self.createHtmlTemplateHeatMap(name, _data, "path", 2)

        return

    def createMaidrTemplate(self, name, _data, element, slice_count, index):
        with open("generated_svg/" + name + "plot.svg", "r") as text_file:
            svg_ = text_file.read()

        # id_attr = 'id="MyChart"'
        # svg_ = svg_.replace("<svg ", f"<svg {id_attr}")

        html_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="maidr/example/js/styles.min.css" type="text/css" />

            <script src="maidr/example/js/maidr.min.js"></script>
        </head>
        <body>
            <div class="container mt-3">
                <div id="container" data-plottype="bar">
                    <div id="braille-div">
                    <input id="braille-input" class="braille-input hidden" type="text" />
                    </div>

                    <div id="svg-container">
                        {svg}
                    </div>
                </div>
            </div>
            <script>
                var maidr = {{
                    type: '{name}',
                    title: '{name}',
                    elements: Array.from(document.querySelectorAll('{element}')).slice({slice_count}, {index}+{slice_count}),
                    axes: {{
                    x: {{
                        label: "Cut",
                        format: {data_x},
                    }},
                    y: {{
                        label: "Count",
                    }},
                    }},
                    data: {data_y},
                }};
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
            index=index,
        )

        with open("chart_maidr.html", "w") as f:
            f.write(html_template)

    def createMaidrTemplateScatter(self, name, _data, element, slice_count, index):
        with open("generated_svg/" + name + "plot.svg", "r") as text_file:
            svg_ = text_file.read()

        # id_attr = 'id="MyChart"'
        # svg_ = svg_.replace("<svg ", f"<svg {id_attr}")

        html_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="maidr/example/js/styles.min.css" type="text/css" />

            <script src="maidr/example/js/maidr.min.js"></script>
        </head>
        <body>
            <div class="container mt-3">
                <div id="container" data-plottype="bar">
                    <div id="braille-div">
                    <input id="braille-input" class="braille-input hidden" type="text" />
                    </div>

                    <div id="svg-container">
                        {svg}
                    </div>
                </div>
            </div>
            <script>
                console.log(document.querySelectorAll('use'))
                var maidr = {{
                    type: '{name}',
                    title: '{name}',
                    elements: Array.from(document.querySelectorAll('{element}')).slice({slice_count}, {index}+{slice_count}),
                    axes: {{
                    x: {{
                        label: "Cut",
                    }},
                    y: {{
                        label: "Count",
                    }},
                    }},
                    data: {{data_point_layer:
                        {data}
                    }},
                }};
            </script>
        </body>
        </html>
        """

        html_template = html_template.format(
            svg=svg_,
            data=_data,
            name=name,
            # data_y=_data[1],
            element=element,
            slice_count=slice_count,
            index=index,
        )

        with open("chart_maidr.html", "w") as f:
            f.write(html_template)

    def createMaidrTemplateHeat(self, name, _data, element, slice_count, index):
        with open("generated_svg/" + name + "plot.svg", "r") as text_file:
            svg_ = text_file.read()

        # id_attr = 'id="MyChart"'
        # svg_ = svg_.replace("<svg ", f"<svg {id_attr}")

        html_template = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
                <link rel="stylesheet" href="maidr/example/js/styles.min.css" type="text/css" />

                <script src="maidr/example/js/maidr.min.js"></script>
            </head>
            <body>
                <div class="container mt-3">
                    <div id="container" data-plottype="bar">
                        <div id="braille-div">
                        <input id="braille-input" class="braille-input hidden" type="text" />
                        </div>

                        <div id="svg-container">
                            {svg}
                        </div>
                    </div>
                </div>
                <script>
                    console.log(document.querySelectorAll('{element}'))
                    var maidr = {{
                        type: '{name}',
                        legend_x: 'Island',
                        legend_y: 'Species',
                        title: '{name}',
                        elements: Array.from(document.querySelectorAll('{element}')).slice({slice_count}, {index}+{slice_count}),
                        axes: {{
                        x: {{
                            label: "Island",
                            format: {data_x},
                        }},
                        y: {{
                            label: "Species",
                            format: {slices},
                        }},
                        }},
                        data: {data_y},
                    }};
                </script>
            </body>
            </html>
            """

        html_template = html_template.format(
            svg=svg_,
            data_x=_data[0],
            slices=_data[1],
            name=name,
            data_y=_data[2],
            element=element,
            slice_count=slice_count,
            index=index,
        )

        # <!DOCTYPE html>
        #     <html lang="en">
        #     <head>
        #         <meta charset="UTF-8">
        #         <meta http-equiv="X-UA-Compatible" content="IE=edge">
        #         <meta name="viewport" content="width=device-width, initial-scale=1.0">
        #         <title>Document</title>

        #         <script src="https://cdn.jsdelivr.net/npm/chart2music"></script>
        #     </head>
        #     <body>
        #         <div>
        #             {svg}
        #         </div>
        #         <div id="cc"></div>

        #     <script>
        #         const x = {data_x};
        #         const slices = {slices}
        #         const err = c2mChart({{
        #             type: "{name}",
        #             element: document.getElementById("MyChart"),
        #             cc: document.getElementById("cc"),
        #             axes: {{
        #                 x: {{
        #                     label: "class",
        #                     format: (index) => x[index]
        #                 }},
        #                 y: {{
        #                     label: "count"
        #                 }}
        #             }},
        #             data: {data_y},
        #             options: {{
        #                 onFocusCallback: ({{index, slice}}) => {{
        #                     const rowIndex = slices.indexOf(slice);
        #                     Array.from(document.querySelectorAll("#MyChart {element}")).slice({slice_count})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  .forEach((elem) => {{
        #                         elem.style.fill = "rgb(89, 89, 89)";
        #                     }})
        #                     document.querySelectorAll("#MyChart {element}")[(rowIndex*12)+index+{slice_count}].style.fill = "cyan";
        #                 }}
        #             }}
        #         }});
        #         if(err){{
        #             console.error(err);
        #         }}
        #     </script>
        # </body>
        # </html>

        with open("chart_maidr.html", "w") as f:
            f.write(html_template)

    def createHtmlTemplate(self, name, _data, element, slice_count):
        with open("generated_svg/" + name + "plot.svg", "r") as text_file:
            svg_ = text_file.read()

        id_attr = 'id="MyChart"'
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

        with open("chart.html", "w") as f:
            f.write(html_template)

    def createHtmlTemplate(self, name, _data, element, slice_count):
        with open("generated_svg/" + name + "plot.svg", "r") as text_file:
            svg_ = text_file.read()

        id_attr = 'id="MyChart"'
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

        with open("chart.html", "w") as f:
            f.write(html_template)

    def createHtmlTemplateHeatMap(self, name, _data, element, slice_count):
        with open("generated_svg/" + name + "plot.svg", "r") as text_file:
            svg_ = text_file.read()

        id_attr = 'id="MyChart"'
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
                    const slices = {slices}
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
                                label: "count"
                            }}
                        }},
                        data: {data_y},
                        options: {{
                            onFocusCallback: ({{index, slice}}) => {{
                                const rowIndex = slices.indexOf(slice);
                                Array.from(document.querySelectorAll("#MyChart {element}")).slice({slice_count})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  .forEach((elem) => {{
                                    elem.style.fill = "rgb(89, 89, 89)";
                                }})
                                document.querySelectorAll("#MyChart {element}")[(rowIndex*12)+index+{slice_count}].style.fill = "cyan";
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

        # data: Object.fromEntries(
        #                     {data_y}.map((label, index) => [label, {data_y}[index]])
        #                 ),
        #                 options: {{
        #                     onFocusCallback: ({{index, slice}}) => {{
        #                         const data_ = {data_y}
        #                         Array.from(document.querySelectorAll("#MyChart {element}")).slice({slice_count})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  .forEach((elem) => {{
        #                             elem.style.fill = "rgb(89, 89, 89)";
        #                         }})
        #                         document.querySelectorAll("#MyChart {element}")[index+{slice_count}].style.fill = "cyan";
        #                     }}
        #                 }}

        # onFocusCallback: ({{index}}) => {{
        #                     const data_ = {data_y}
        #                     Array.from(document.querySelectorAll("#MyChart {element}")).slice({slice_count})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  .forEach((elem) => {{
        #                         elem.style.fill = "rgb(89, 89, 89)";
        #                     }})
        #                     const point = data_[Object.keys(data_)[index]];
        #                     point.map((val, ind)=>{{
        #                         console.log(ind, index)
        #                         document.querySelectorAll("#MyChart {element}")[(index*ind)+{slice_count}].style.fill = "cyan";
        #                     }})
        #                 }}

        # Object.keys({data_y})[index].map((value, i) => {{
        # document.querySelectorAll("#MyChart {element}")[index+{slice_count}][i].style.fill = "cyan";
        # }})

        html_template = html_template.format(
            svg=svg_,
            data_x=_data[0],
            slices=_data[1],
            name=name,
            data_y=_data[2],
            element=element,
            slice_count=slice_count,
        )

        with open("chart.html", "w") as f:
            f.write(html_template)

    def createHtmlTemplateLine(self, name, _data, element, slice_count):
        with open("generated_svg/" + name + "plot.svg", "r") as text_file:
            svg_ = text_file.read()

        id_attr = 'id="MyChart"'
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
                    data: {data_y}[0],
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

        with open("chart.html", "w") as f:
            f.write(html_template)

    # def createHtmlTemplateLine2(self, name, _data, element, slice_count):
    #     with open("generated_svg/" + name + "plot.svg", "r") as text_file:
    #         svg_ = text_file.read()

    #     id_attr = 'id="MyChart"'
    #     svg_ = svg_.replace("<svg ", f"<svg {id_attr}")

    #     elements = document.querySelector('input[id^="line2d_"]');

    #     html_template = """
    #     <!DOCTYPE html>
    #     <html lang="en">
    #     <head>
    #         <meta charset="UTF-8">
    #         <meta http-equiv="X-UA-Compatible" content="IE=edge">
    #         <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #         <title>Document</title>

    #         <script src="https://cdn.jsdelivr.net/npm/chart2music"></script>
    #     </head>
    #     <body>
    #         <div>
    #             {svg}
    #         </div>
    #         <div id="cc"></div>

    #         <script>

    #             const coordinates = document.querySelector("#" + elements + " path").getAttribute("d").trim().split("\\n").map((str) => str.substring(2).trim().split(" ").map((n) => +n));

    #             const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    #             circle.setAttribute("cx", coordinates[0][0]);
    #             circle.setAttribute("cy", coordinates[0][1]);
    #             circle.setAttribute("r", "5");
    #             circle.setAttribute("fill", "cyan");

    #             document.querySelector("#figure_1").appendChild(circle);

    #             const x = {data_x};
    #             const err = c2mChart({{
    #                 type: "{name}",
    #                 element: document.getElementById("MyChart"),
    #                 cc: document.getElementById("cc"),
    #                 axes: {{
    #                     x: {{
    #                         label: "class",
    #                         format: (index) => x[index]
    #                     }},
    #                     y: {{
    #                         label: "count",
    #                         minimum: 0
    #                     }}
    #                 }},
    #                 data: {data_y},
    #                 options: {{
    #                     onFocusCallback: ({{index}}) => {{
    #                             circle.setAttribute("cx", coordinates[index][0]);
    #                             circle.setAttribute("cy", coordinates[index][1]);
    #                         }}
    #                 }}
    #             }});
    #             if(err){{
    #                 console.error(err);
    #             }}
    #         </script>
    #     </body>
    #     </html>
    #     """

    #     html_template = html_template.format(
    #         svg=svg_,
    #         data_x=_data[0],
    #         name=name,
    #         data_y=_data[1],
    #         element=element,
    #         slice_count=slice_count,
    #     )

    #     with open("chart.html", "w") as f:
    #         f.write(html_template)
