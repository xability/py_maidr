import os

import maidr
import matplotlib.pyplot as plt
import seaborn as sns


def get_filepath(filename: str) -> str:
    current_file_path = os.path.abspath(__file__)
    directory = os.path.dirname(current_file_path)
    return os.path.join(directory, filename)


def plot():
    # Load the dataset
    iris = sns.load_dataset("iris")

    # Choose a column for the histogram, for example, the 'petal_length'
    data = iris["petal_length"]

    # Create the histogram plot
    _, _, hist_plot = plt.hist(data, bins=20, edgecolor="black")
    plt.title("Histogram of Petal Lengths in Iris Dataset")
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Frequency")

    return hist_plot


def main():
    hist = plot()
    hist_maidr = maidr.hist(hist)
    hist_maidr.save(get_filepath("example_mpl_histogram.html"))


if __name__ == "__main__":
    main()
