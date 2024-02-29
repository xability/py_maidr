import os

import numpy as np
import matplotlib.pyplot as plt
import maidr
import seaborn as sns


def get_filepath(filename: str) -> str:
    current_file_path = os.path.abspath(__file__)
    directory = os.path.dirname(current_file_path)
    return os.path.join(directory, filename)


# def plot():
#     # Load an example dataset from seaborn
#     glue = sns.load_dataset("glue").pivot(index="Model", columns="Task", values="Score")
#
#     # Plot a heatmap
#     plt.figure(figsize=(10, 8))
#     heatmap = sns.heatmap(glue, annot=True)
#     plt.show()
#
#     return heatmap


def plot():
    # Sample data for line plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Sample data for scatter plot
    scatter_x = np.linspace(0, 10, 25)
    scatter_y = np.cos(scatter_x)

    # Create a line plot
    plt.plot(x, y, "-r", label="Sine Wave")

    # Overlay a scatter plot
    plt.scatter(scatter_x, scatter_y, color="blue", label="Cosine Points")

    # Adding labels and legend
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Line Plot with Scatter Plot")
    plt.legend()

    # Show the combined plot
    plt.show()


def main():
    heatmap = plot()
    # heat_maidr = maidr.heat(heatmap)
    # heat_maidr.save(get_filepath("example_sns_heatmap.html"))


if __name__ == "__main__":
    main()
