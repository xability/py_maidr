import os

import matplotlib.pyplot as plt
import maidr
import seaborn as sns


def get_filepath(filename: str) -> str:
    current_file_path = os.path.abspath(__file__)
    directory = os.path.dirname(current_file_path)
    return os.path.join(directory, filename)


def plot():
    # Load the Iris dataset
    iris = sns.load_dataset("iris")

    # Create a scatter plot
    scatter_plot = sns.scatterplot(
        data=iris, x="sepal_length", y="sepal_width", hue="species"
    )

    # Adding title and labels (optional)
    plt.title("Iris Sepal Length vs Sepal Width")
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")

    return scatter_plot


def main():
    scatter = plot()
    scatter_maidr = maidr.scatter(scatter)
    scatter_maidr.save(get_filepath("example_sns_scatter.html"))


if __name__ == "__main__":
    main()
