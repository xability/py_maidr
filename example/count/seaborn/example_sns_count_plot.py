import os

import matplotlib.pyplot as plt
import maidr
import seaborn as sns


def get_filepath(filename: str) -> str:
    current_file_path = os.path.abspath(__file__)
    directory = os.path.dirname(current_file_path)
    return os.path.join(directory, filename)


def plot():
    # Load the Titanic dataset
    titanic = sns.load_dataset("titanic")

    # Create a countplot
    count_plot = sns.countplot(x="class", data=titanic)

    # Set the title and show the plot
    plt.title("Passenger Class Distribution on the Titanic")

    return count_plot


def main():
    count_plot = plot()
    count_maidr = maidr.count(count_plot)
    count_maidr.save(get_filepath("example_sns_count_plot.html"))


if __name__ == "__main__":
    main()
