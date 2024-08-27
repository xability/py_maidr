import matplotlib.pyplot as plt
import seaborn as sns

import maidr


penguins = sns.load_dataset("penguins")

# Initialize the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Prepare Scatter plot layer
sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", s=100, ax=ax)

# Prepare Line plot layer
sns.regplot(
    data=penguins,
    x="flipper_length_mm",
    y="body_mass_g",
    scatter=False,
    lowess=True,
    line_kws={"color": "black"},
    ax=ax,
)

ax.set_title("Penguin Flipper Length vs Body Mass (Smoothed)", fontsize=16)
ax.set_xlabel("Flipper Length (mm)", fontsize=14)
ax.set_ylabel("Body Mass (g)", fontsize=14)

# Create a Maidr instance
maidr_plot = maidr.Maidr(fig)

html_string = maidr_plot.render(html=True).get_html_string()

with open("example_scatter_2_layered.html", "w") as f:
    f.write(html_string)
