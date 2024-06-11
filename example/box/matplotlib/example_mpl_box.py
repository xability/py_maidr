import matplotlib.pyplot as plt
import maidr
import numpy as np


# Generating random data for three different groups
data_group1 = np.random.normal(100, 10, 200)
data_group2 = np.random.normal(90, 20, 200)
data_group3 = np.random.normal(80, 30, 200)

# Combine these different datasets into a list
data_to_plot = [data_group1, data_group2, data_group3]

# Create a figure instance
fig, ax = plt.subplots()

# Create the boxplot
bp = ax.boxplot(data_to_plot, patch_artist=True)

# Customize the boxplot colors
colors = ["lightblue", "lightgreen", "tan"]
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)

# Adding labels and title
ax.set_xticklabels(["Group 1", "Group 2", "Group 3"])
ax.set_title("Box Plot Example")
ax.set_xlabel("Group")
ax.set_ylabel("Values")

# Show the plot
plt.show()
maidr.show(bp)
