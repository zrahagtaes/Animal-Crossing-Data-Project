import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('villagers.csv')
df.head(20)



df['Name'].count()

sns.catplot(x="Personality",  kind="count", hue='Gender', data=df)
plt.show()

Species = df.Species.value_counts().plot(kind = 'bar', color= "Blue", figsize = (12, 6))
plt.xlabel("Different Species")
plt.ylabel= ("quantity")
plt.show()


