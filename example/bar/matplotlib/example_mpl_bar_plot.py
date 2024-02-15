import os

import matplotlib.pyplot as plt
import maidr
import seaborn as sns


def get_filepath(filename: str) -> str:
    current_file_path = os.path.abspath(__file__)
    directory = os.path.dirname(current_file_path)
    return os.path.join(directory, filename)


def plot():
    # Load dataset
    tips = sns.load_dataset("tips")

    # Create a bar plot
    cut_counts = tips["day"].value_counts()
    plt.figure(figsize=(10, 6))
    b_plot = plt.bar(cut_counts.index, list(cut_counts.values), color="skyblue")
    plt.title("The Number of Tips by Day")
    plt.xlabel("Day")
    plt.ylabel("Count")

    return b_plot


def main():
    bar_plot = plot()
    bar_maidr = maidr.bar(bar_plot)
    bar_maidr.save(get_filepath("example_mpl_bar_plot.html"))


if __name__ == "__main__":
    main()
