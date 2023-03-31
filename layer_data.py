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
