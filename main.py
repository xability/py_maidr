import seaborn as sns
from layer_data import LayerData
import pandas as pd
import matplotlib.pyplot as plt


def count_plot(plot_type, isJson):
    df_cp = sns.load_dataset('titanic')
    plot_data_cp = sns.countplot(x=df_cp["class"])
    ext_data_count = LayerData(plot_data_cp)

    plt.savefig("generated_svg/" + plot_type +"plot.svg", format="svg")
    data = ext_data_count.data_plot_count(plot_type)

    _data = None
    if isJson:
        _data = to_json(plot_type, data[0], data[1])
    else:
        _data = to_df(data[0], data[1])
    print(_data)

    plot_data_cp.clear()


def bar_plot(plot_type, isJson):
    df_bp = sns.load_dataset("penguins")
    plot_data_bp = sns.barplot(data=df_bp, x="island", y="body_mass_g")
    ext_data_bar = LayerData(plot_data_bp)

    plt.savefig("generated_svg/" + plot_type +"plot.svg", format="svg")
    data = ext_data_bar.data_plot_bar(plot_type)

    _data = None
    if isJson:
        _data = to_json(plot_type, data[0], data[1])
    else:
        _data = to_df(data[0], data[1])
    print(_data)

    plot_data_bp.clear()


def scatter_plot(plot_type, isJson):
    df_sc = sns.load_dataset("tips")
    plot_data_sc = sns.scatterplot(data=df_sc, x="total_bill", y="tip")
    ext_data_scatter = LayerData(plot_data_sc)

    plt.savefig("generated_svg/" + plot_type + "plot.svg", format="svg")
    data = ext_data_scatter.data_plot_scatter(plot_type)
    _data = None
    if isJson:
        _data = to_json(plot_type, data[0], data[1])
    else:
        _data = to_df(data[0], data[1])
    print(_data)


def line_plot(plot_type, isJson):
    tips = sns.load_dataset("tips")
    plot_data_lp = sns.lineplot(x="total_bill", y="tip", data=tips)
    ext_data_line = LayerData(plot_data_lp)

    plt.savefig("generated_svg/" + plot_type + "plot.svg", format="svg")
    data = ext_data_line.data_plot_line(plot_type)

    _data = None
    if isJson:
        _data = to_json(plot_type, data[0], data[1])
    else:
        _data = to_df(data[0], data[1])
    print(_data)


def box_plot(plot_type, isJson):
    tips = sns.load_dataset("tips")
    plot_data_bxp = sns.boxplot(x="day", y="total_bill", data=tips)
    # plt.show()


def to_json(name, x_data, y_data):
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


def to_df(x_data, y_data):
    data = pd.DataFrame({'x': x_data, 'y': y_data})
    return data


def main():
    print("countplot data::::")
    count_plot('bar', True)

    # print("barplot data::::")
    # bar_plot('bar', True)

    # print("scatterplot data::::")
    # scatter_plot('scatter', True)

    # print("lineplot data::::")
    # line_plot('line', True)

    # print("boxplot data::::")
    # box_plot('box', True)


if __name__ == "__main__":
    main()
