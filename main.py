import seaborn as sns
from layer_data import LayerData

df = sns.load_dataset('titanic')
plot_data = sns.countplot(x=df["class"]) 

LayerData.display_data(plot_data)
