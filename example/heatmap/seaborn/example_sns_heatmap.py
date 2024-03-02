import os

import matplotlib.pyplot as plt
import maidr
import seaborn as sns


def get_filepath(filename: str) -> str:
    current_file_path = os.path.abspath(__file__)
    directory = os.path.dirname(current_file_path)
    return os.path.join(directory, filename)


def plot():
    # Load an example dataset from seaborn
    glue = sns.load_dataset("glue").pivot(index="Model", columns="Task", values="Score")

    # Plot a heatmap
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(glue, annot=True)
    plt.title("Heatmap of Model Scores by Task")
    plt.show()

    return heatmap


def main():
    heatmap = plot()
    heat_maidr = maidr.heat(heatmap)
    heat_maidr.save(get_filepath("example_sns_heatmap.html"))


if __name__ == "__main__":
    main()
