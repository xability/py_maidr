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

    # Select the petal lengths
    petal_lengths = iris["petal_length"]

    # Plot a histogram of the petal lengths
    plt.figure(figsize=(10, 6))
    hist_plot = sns.histplot(petal_lengths, kde=True, color="blue", binwidth=0.5)

    plt.title("Histogram of Petal Lengths in Iris Dataset")
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Frequency")

    return hist_plot


def main():
    hist = plot()
    hist_maidr = maidr.hist(hist)
    hist_maidr.save(get_filepath("example_sns_histogram.html"))


if __name__ == "__main__":
    main()
