# import matplotlib.pyplot as plt
import pydataset
import seaborn as sns

import c2m

# # Let's say you have a barplot
mpg = pydataset.data("mpg")

# # Count `class` column
mpg["class"].value_counts().index

# # Create a barplot
sns.barplot(x="class", y="hwy", data=mpg)

# sns.countplot(mpg, x="class")
