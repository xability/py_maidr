import matplotlib.pyplot as plt
import maidr
import seaborn as sns


# Load the Iris dataset
iris = sns.load_dataset("iris")

# Start a new figure
plt.figure()

# Create box plot
box_plot = sns.boxplot(x="species", y="petal_length", data=iris)

# Adding labels and title
plt.title("Box Plot of Petal Length by Iris Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")

plt.show()
maidr.show(box_plot)
