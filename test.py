# import matplotlib.pyplot as plt
import pydataset
import seaborn as sns

import c2m

# # Let's say you have a barplot
# df = pydataset.data("diamonds")
# sns.countplot(df, x="cut", file="jy.html")
# df = pydataset.data("economics")
# Line plot
# sns.lineplot(df, x="date", y="pop", file="jy.html")

# Test scatterplot
df = pydataset.data("mpg")
sns.scatterplot(df, x="displ", y="hwy")
