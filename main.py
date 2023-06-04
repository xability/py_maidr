import seaborn as sns
from layer_data import LayerData
import pandas as pd
import matplotlib.pyplot as plt


def countPlot(plot_type, is_json):
    df_cp = sns.load_dataset("titanic")
    plot_data_cp = sns.countplot(x=df_cp["class"])
    ext_data_count = LayerData(plot_data_cp)

    plt.savefig("generated_svg/" + plot_type + "plot.svg", format="svg")
    data = ext_data_count.dataplotCount(plot_type)

    _data = None
    if is_json:
        _data = toJson(plot_type, data[0], data[1])
    else:
        _data = toDf(data[0], data[1])
    print(_data)

    plot_data_cp.clear()


def barPlot(plot_type, is_json):
    df_bp = sns.load_dataset("penguins")
    plot_data_bp = sns.barplot(data=df_bp, x="island", y="body_mass_g")
    ext_data_bar = LayerData(plot_data_bp)

    plt.savefig("generated_svg/" + plot_type + "plot.svg", format="svg")
    data = ext_data_bar.dataplotBar(plot_type)

    _data = None
    if is_json:
        _data = toJson(plot_type, data[0], data[1])
    else:
        _data = toDf(data[0], data[1])
    print(_data)

    plot_data_bp.clear()


def scatterPlot(plot_type, is_json):
    df_sc = sns.load_dataset("tips")
    plot_data_sc = sns.scatterplot(data=df_sc, x="total_bill", y="tip")
    ext_data_scatter = LayerData(plot_data_sc)

    plt.savefig("generated_svg/" + plot_type + "plot.svg", format="svg")
    data = ext_data_scatter.dataplotScatter(plot_type)
    _data = None
    if is_json:
        _data = toJson(plot_type, data[0], data[1])
    else:
        _data = toDf(data[0], data[1])
    print(_data)


def linePlot(plot_type, is_json):
    df_lp = sns.load_dataset("flights")
    may_flights = df_lp.query("month == 'May'")
    plot_data_lp = sns.lineplot(data=may_flights, x="year", y="passengers")
    ext_data_line = LayerData(plot_data_lp)

    plt.savefig("generated_svg/" + plot_type + "plot.svg", format="svg")
    data = ext_data_line.dataplotLine(plot_type)

    _data = None
    if is_json:
        _data = toJson(plot_type, data[0], data[1])
    else:
        _data = toDf(data[0], data[1])
    print(_data)


def boxPlot(plot_type, is_json):
    tips = sns.load_dataset("tips")
    plot_data_bxp = sns.boxplot(x="day", y="total_bill", data=tips)
    # plt.show()


def toJson(name, x_data, y_data):
    values = []
    for i in range(len(x_data)):
        values.append({"x": x_data[i], "y": y_data[i]})

    data = {"type": name, "data": {"datasets": [{"data": values}]}}

    return data


def toDf(x_data, y_data):
    data = pd.DataFrame({"x": x_data, "y": y_data})
    return data


def main():
    # print("countplot data::::")
    # countPlot('bar', True)

    # print("barplot data::::")
    # barPlot('bar', True)

    # print("scatterplot data::::")
    # scatterPlot('scatter', True)

    print("lineplot data::::")
    linePlot("line", True)

    # print("boxplot data::::")
    # boxPlot('box', True)


if __name__ == "__main__":
    main()
