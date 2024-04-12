import os

import maidr
import matplotlib.pyplot as plt
import numpy as np


def get_filepath(filename: str) -> str:
    current_file_path = os.path.abspath(__file__)
    directory = os.path.dirname(current_file_path)
    return os.path.join(directory, filename)


def plot():
    species = (
        "Adelie\n $\\mu=$3700.66g",
        "Chinstrap\n $\\mu=$3733.09g",
        "Gentoo\n $\\mu=5076.02g$",
    )
    weight_counts = {
        "Below": np.array([70, 31, 58]),
        "Above": np.array([82, 37, 66]),
    }
    width = 0.5

    fig, ax = plt.subplots()
    bottom = np.zeros(3)

    for boolean, weight_count in weight_counts.items():
        ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
        bottom += weight_count

    ax.set_title("Number of penguins with above average body mass")
    ax.legend(loc="upper right")
    ax.set_xlabel("Species")
    ax.set_ylabel("Number of Penguins")

    return ax


def main():
    stacked = plot()
    stacked_maidr = maidr.stacked(stacked)
    stacked_maidr.save_html(get_filepath("example_mpl_stacked.html"))
    stacked_maidr.show()


if __name__ == "__main__":
    main()
