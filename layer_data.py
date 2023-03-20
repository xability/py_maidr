import pandas as pd

class LayerData:

    def data_plot_count_bar(plot_data):
        
        if not plot_data.has_data():
            return "Plot is Empty!"
        
        data_y = []
        y_vars = plot_data.patches
        for y in y_vars:
            data_y.append(y.get_height())

        data_x = []
        x_vars = plot_data.get_xticklabels()
        for x in x_vars:
            data_x.append(x.get_text())

        data = {}
        data['x'] = data_x
        data['y'] = data_y

        df = pd.DataFrame(data)
        return df
    

    def data_plot_scatter(plot_data):
        if not plot_data.has_data():
            return "Plot is Empty!"
        
        data_y = []
        data_x = []
        data_sc = plot_data.collections[0].get_offsets()
        for points in data_sc:
            data_y.append(points.data[1])
            data_x.append(points.data[0])

        data = {}
        data['x'] = data_x
        data['y'] = data_y
        
        df = pd.DataFrame(data)
        return df
    