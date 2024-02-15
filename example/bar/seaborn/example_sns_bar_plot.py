import os

import matplotlib.pyplot as plt
import maidr
import seaborn as sns


def get_filepath(filename: str) -> str:
    current_file_path = os.path.abspath(__file__)
    directory = os.path.dirname(current_file_path)
    return os.path.join(directory, filename)


def plot():
    # Load the penguins dataset
    penguins = sns.load_dataset("penguins")

    # Create a bar plot showing the average body mass of penguins by species
    plt.figure(figsize=(10, 6))
    b_plot = sns.barplot(
        x="species", y="body_mass_g", data=penguins, errorbar="sd", palette="Blues_d"
    )
    b_plot.bar
    plt.title("Average Body Mass of Penguins by Species")
    plt.xlabel("Species")
    plt.ylabel("Body Mass (g)")

    return b_plot


def main():
    bar_plot = plot()
    bar_maidr = maidr.bar(bar_plot)
    bar_maidr.save(get_filepath("example_sns_bar_plot.html"))


if __name__ == "__main__":
    main()
