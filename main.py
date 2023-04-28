import seaborn as sns
from layer_data import LayerData
import matplotlib.pyplot as plt

def count_plot(plot_type, isJson):
    df_cp = sns.load_dataset('titanic')
    plot_data_cp = sns.countplot(x=df_cp["class"])
    ext_data_count = LayerData(plot_data_cp)
    print(ext_data_count.data_plot_count(plot_type, isJson))
    plot_data_cp.clear()


def bar_plot(plot_type, isJson):
    df_bp = sns.load_dataset("penguins")
    plot_data_bp = sns.barplot(data=df_bp, x="island", y="body_mass_g")
    ext_data_bar = LayerData(plot_data_bp)
    
    # plt.savefig("barplot.svg", format="svg")
    print(ext_data_bar.data_plot_bar(plot_type, isJson))
    plot_data_bp.clear()


def scatter_plot(plot_type, isJson):
    df_sc = sns.load_dataset("tips")
    plot_data_sc = sns.scatterplot(data=df_sc, x="total_bill", y="tip")
    ext_data_scatter = LayerData(plot_data_sc)
    print(ext_data_scatter.data_plot_scatter(plot_type, isJson))


def line_plot(plot_type, isJson):
    tips = sns.load_dataset("tips")
    plot_data_lp = sns.lineplot(x="total_bill", y="tip", data=tips)
    ext_data_line = LayerData(plot_data_lp)
    print(ext_data_line.data_plot_line(plot_type, isJson))


def box_plot(plot_type, isJson):
    tips = sns.load_dataset("tips")
    plot_data_bxp = sns.boxplot(x="day", y="total_bill", data=tips)
    # plt.show()


def main():
    # print("countplot data::::")
    # count_plot('count', True)

    print("barplot data::::")
    bar_plot('bar', True)

    # print("scatterplot data::::")
    # scatter_plot('scatter', True)

    # print("lineplot data::::")
    # line_plot('line', True)

    # print("boxplot data::::")
    # box_plot('box', True)


if __name__ == "__main__":
    main()
