import seaborn as sns
from layer_data import LayerData


def count_plot():
    df_cp = sns.load_dataset('titanic')
    plot_data_cp = sns.countplot(x=df_cp["class"])
    ext_data_count = LayerData.data_plot_count_bar(plot_data_cp)
    print(ext_data_count)


def bar_plot():
    df_bp = sns.load_dataset("penguins")
    plot_data_bp = sns.barplot(data=df_bp, x="island", y="body_mass_g")
    ext_data_bar = LayerData.data_plot_count_bar(plot_data_bp)
    print(ext_data_bar)


def scatter_plot():
    df_sc = sns.load_dataset("tips")
    plot_data_sc = sns.scatterplot(data=df_sc, x="total_bill", y="tip")
    ext_data_scatter = LayerData.data_plot_scatter(plot_data_sc)
    print(ext_data_scatter)


def main():
    print("countplot data::::")
    count_plot()

    print("scatterplot data::::")
    scatter_plot()

    # print("barplot data::::")
    # bar_plot()


if __name__ == '__main__':
    main()