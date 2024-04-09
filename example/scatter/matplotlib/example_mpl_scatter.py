import os

import maidr
import matplotlib.pyplot as plt
import seaborn as sns


def get_filepath(filename: str) -> str:
    current_file_path = os.path.abspath(__file__)
    directory = os.path.dirname(current_file_path)
    return os.path.join(directory, filename)


def plot():
    # Load the Iris dataset
    iris = sns.load_dataset("iris")

    # Plot sepal_length vs sepal_width
    plt.figure(figsize=(10, 6))  # Optional: Sets the figure size
    scatter_plot = plt.scatter(
        iris["sepal_length"], iris["sepal_width"], c="blue", label="Iris Data Points"
    )
    plt.title("Iris Dataset: Sepal Length vs Sepal Width")  # Title of the plot
    plt.xlabel("Sepal Length (cm)")  # X-axis label
    plt.ylabel("Sepal Width (cm)")  # Y-axis label
    plt.legend()  # Shows the legend

    return scatter_plot


def main():
    scatter = plot()
    scatter_maidr = maidr.scatter(scatter)
    scatter_maidr.save_html(get_filepath("example_mpl_scatter.html"))


if __name__ == "__main__":
    main()
