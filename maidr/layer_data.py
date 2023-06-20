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
        self.createHtmlTemplate(name, _data, "path", 2)

        return _data

    def dataplotBar(self, name):
        _data = self.dataplotCount(name)
        self.createHtmlTemplate(name, _data, "path", 2)

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
        self.createHtmlTemplate(name, _data, "use", 0)

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

        x_ax_data = {}
        for i in range(len(x_labels)):
            year = []
            for j in range(len(y_labels)):
                index = j * len(x_labels) + i
                data_value = datapoints[index]
                year.append(data_value)
            x_ax_data.update({y_labels[i]: year})

        _data = []
        data_x = x_labels
        data_y = x_ax_data

        _data = [data_x, data_y]
        self.createHtmlTemplateHeatMap(name, _data, "path", 2)

        return

    def dataplotBox(self, name):
        if not self.plot_data.has_data():
            return "Plot is Empty!"

        # print(self.plot_data.get_xticklabels())
        # print(self.plot_data.collections)
        # _data = []
        # data_x = x_labels
        # data_y = yearly_data
        # # # data_z = yearly_data

        # _data = [data_x, data_y]
        # # print(_data)
        # self.createHtmlTemplateHeatMap(name, _data, "path", 2)

        return

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
                            onFocusCallback: ({{index}}) => {{
                                Array.from(document.querySelectorAll("#MyChart {element}")).slice({slice_count})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  .forEach((elem) => {{
                                    elem.style.fill = "rgb(89, 89, 89)";
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
            name=name,
            data_y=_data[1],
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
