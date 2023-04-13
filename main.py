import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

#reading the data
df = pd.read_csv('villagers.csv')
df.head(20)

#counting the values of Name
df['Name'].count()

#produces a pie chart presenting the relationship between personality and population
Personalities = df.Personality.value_counts().plot(kind='pie', autopct='%.2f')
plt.ylabel(None)
plt.title("Personality Count")
plt.show()

#produces a bar graph showing the relationship beteen gender and personality
sns.catplot(x="Personality",  kind="count", hue='Gender', data=df)
plt.xlabel("Different Personalities")
plt.ylabel("Quantity")
plt.title("Gender X Personality")
plt.show()

#produces a bar graph showing the number of species
species = df.Species.value_counts().plot(kind='bar', color="Pink", figsize=(12,6))
plt.xlabel("Different Species")
plt.ylabel("Count")
plt.title("Species Count")
plt.show()

#produces bar graph showing relationship between personality and species
compare = sns.catplot(x='Species', kind='count', hue='Personality',height=25, aspect=12/9,data = df)
plt.title("Personality X Species")
plt.xticks(rotation = 90)
plt.show()