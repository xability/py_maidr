import pandas as pd
import seaborn as sns
from layer_data import LayerData
import matplotlib.pyplot as plt


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


def line_plot():
    flights = sns.load_dataset("flights")
    may_flights = flights.query("month == 'May'")
    plot_data_lp = sns.lineplot(data=may_flights, x="year", y="passengers")
    ext_data_line = LayerData.data_plot_line(plot_data_lp)
    print(ext_data_line)


def main():
    print("countplot data::::")
    count_plot()

    print("scatterplot data::::")
    scatter_plot()

    print("lineplot data::::")
    line_plot()

    print("\nbarplot data::::")
    bar_plot()


if __name__ == '__main__':
    main()
