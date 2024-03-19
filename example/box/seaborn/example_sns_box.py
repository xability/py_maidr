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

    # Start a new figure
    plt.figure()

    # Create box plot
    box_plot = sns.boxplot(x="species", y="petal_length", data=iris)

    # Adding labels and title
    plt.title("Box Plot of Petal Length by Iris Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Length (cm)")

    plt.show()

    return box_plot


def main():
    box_plot = plot()
    box_maidr = maidr.box(box_plot)
    box_maidr.save(get_filepath("example_sns_box.html"))


if __name__ == "__main__":
    main()
