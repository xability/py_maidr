import os

import matplotlib.pyplot as plt
import maidr
import seaborn as sns


def get_filepath(filename: str) -> str:
    current_file_path = os.path.abspath(__file__)
    directory = os.path.dirname(current_file_path)
    return os.path.join(directory, filename)


def plot():
    # Load the 'tips' dataset from seaborn
    tips = sns.load_dataset("tips")

    # Choose a specific subset of the dataset (e.g., data for 'Thursday')
    subset_data = tips[tips["day"] == "Thur"]

    # Create a line plot
    plt.figure(figsize=(10, 6))
    line_plot = sns.lineplot(
        data=subset_data,
        x="total_bill",
        y="tip",
        markers=True,
        style="day",
        legend=False,
    )
    plt.title("Line Plot of Tips vs Total Bill (Thursday)")
    plt.xlabel("Total Bill")
    plt.ylabel("Tip")

    return line_plot


def main():
    line = plot()
    line_maidr = maidr.line(line)
    line_maidr.save(get_filepath("example_sns_line.html"))


if __name__ == "__main__":
    main()
