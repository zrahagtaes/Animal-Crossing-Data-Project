import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

#reading the data
df = pd.read_csv('villagers.csv')
df.head(20)

pd.set_option('display.max_columns', None)  # display all columns
pd.set_option('display.max_rows', None)     # display all rows


le = LabelEncoder()
le.fit(pd.concat([df['Species'], df['Personality']]).astype(str))

# encode the 'Species' column and store the result in a new column 'Species_code'
df['Species_code'] = le.transform(df['Species'])
df['Personality_code'] = le.transform(df['Personality'])

# map the encoded values back to their original categorical values
df['Species_name'] = le.inverse_transform(df['Species_code'])
df['Personality_name'] = le.inverse_transform(df['Personality_code'])

# display the result
print(df[['Species', 'Species_code', 'Species_name', 'Personality', 'Personality_code', 'Personality_name']].to_string(index=False, header=True), end="")

species_mean = round(df['Species_code'].mean(), 1)
species_median = round(df['Species_code'].median(), 1)
species_variance = round(df['Species_code'].var(), 0)
species_standard = round(df['Species_code'].std(), 1)

print("")
print("Species Statitics")
print("Species Numerical Mean:", species_mean)
print("Species String Mean: Hippo")
print("Species Numberical Median:", species_median)
print("Species String Median: Gorilla")
print("Species Standard Deviation:", species_standard)
print("Species String Standard Deviation: Dog")
print("Species Variance:", species_variance)


personality_mean = round(df['Personality_code'].mean(), 1)
personality_median = round(df['Personality_code'].median(), 1)
personality_variance = round(df['Personality_code'].var(), 0)
personality_standard = round(df['Personality_code'].std(), 1)
print("")
print("Personality Statistics")
print("Personality Numerical Mean:", personality_mean)
print("Personality String Mean: Lazy")
print("Personality Median:", personality_median)
print("Species String Median: Normal")
print("Personality Standard Deviation:", personality_standard)
print("Personality String Standard Deviation: Cranky")
print("Personality Variance:", personality_variance)


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
