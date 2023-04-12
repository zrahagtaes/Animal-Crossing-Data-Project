import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('villagers.csv')
df.head(20)
df['Name'].count()

Personalities = df.Personality.value_counts().plot(kind='pie', autopct='%.2f')
plt.ylabel(None)
plt.title("Personality Count")
plt.show()

sns.catplot(x="Personality",  kind="count", hue='Gender', data=df)
plt.xlabel("Different Personalities")
plt.ylabel("Quantity")
plt.title("Gender X Personality")
plt.show()

species = df.Species.value_counts().plot(kind='bar', color="Pink", figsize=(12,6))
plt.xlabel("Different Species")
plt.ylabel("Count")
plt.title("Species Count")
plt.show()

compare = sns.catplot(x='Species', kind='count', hue='Personality',height=20, aspect=11.7/8.27,data = df)
plt.legend(title_fontsize='400')
plt.title("Personality X Species")
plt.xticks(rotation = 90)
plt.show()