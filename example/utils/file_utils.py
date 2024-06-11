import os


def example_path(filename: str) -> str:
    current_file_path = os.path.abspath(__file__)
    directory = os.path.dirname(current_file_path)
    return os.path.join(directory, filename)


import matplotlib.pyplot as plt
import seaborn as sns
import maidr


fig, ax = plt.subplots()
# box = sns.boxplot(data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], ax=ax)
# ax.set_title("Test seaborn box title")
# ax.set_xlabel("Test seaborn x label")
# ax.set_ylabel("Test seaborn y label")
#
# plt.show()

ax.boxplot([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
ax.set_title("Test matplotlib box title")
ax.set_xlabel("Test matplotlib box x label")
ax.set_ylabel("Test matplotlib box y label")

plt.show()
