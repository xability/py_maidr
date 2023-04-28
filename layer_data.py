import pandas as pd

class LayerData:

    def __init__(self, data):
        self.plot_data = data

    def data_plot_count(self, name, is_json):
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

        _data = None
        if is_json:
            _data = self.to_json(name, data_x, data_y)

        else:
            _data = self.to_df(data_x, data_y)

        return _data

    def data_plot_bar(self, name, is_json):
        _data = self.data_plot_count(name, is_json)

        with open("barplot.svg", "r") as text_file:
            svg_ = text_file.read()

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
            {}
            <div id="cc"></div>
            <script>
                const x = ["Torgerson", "Biscoe Island", "Dream"];
                const err = c2mChart({{
                    type: "bar",
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
                    data: [3706.37, 4716.02, 3712.9],
                    options: {{
                        onFocusCallback: (index) => {{
                            Array.from(document.querySelectorAll("#MyChart rect")).slice(5).forEach((elem) => {{
                                elem.style.fill = "#595959";
                            }})
                            document.querySelectorAll("#MyChart rect")[index+5].style.fill = "cyan";
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

        html_template = html_template.format(svg_)

        with open('chart.html', 'w') as f:
            f.write(html_template)

        return _data

    def data_plot_scatter(self, name, is_json):
        if not self.plot_data.has_data():
            return "Plot is Empty!"

        data_y = []
        data_x = []
        data_sc = self.plot_data.collections[0].get_offsets()
        for points in data_sc:
            data_y.append(points.data[1])
            data_x.append(points.data[0])

        _data = None

        if is_json:
            _data = self.to_json(name, data_x, data_y)

        else:
            _data = self.to_df(data_x, data_y)

        return _data

    def data_plot_line(self, name, is_json):
        if not self.plot_data.has_data():
            return "Plot is Empty!"

        data_y = []
        data_x = []

        for data in self.plot_data.lines:
            y = data.get_ydata()
            data_y.append(y)

            x = data.get_xdata()
            data_x.append(x)

        _data = None

        if is_json:
            _data = self.to_json(name, data_x[0], data_y[0])

        else:
            _data = self.to_df(data_x[0], data_y[0])

        return _data

    def to_json(self, name, x_data, y_data):
        values = []
        for i in range(len(x_data)):
            values.append({'x': x_data[i], 'y': y_data[i]})

        data = {
            'type': name,
            'data': {
                'datasets': [{
                    'data': values
                }]
            }
        }

        return data

    def to_df(self, x_data, y_data):
        data = pd.DataFrame({'x': x_data, 'y': y_data})
        return data
