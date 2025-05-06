# netflix_analysis.py

# Netflix Movies and TV Shows Analysis
# Author: Collins Macharia
# Dataset Source: https://www.kaggle.com/datasets/shivamb/netflix-shows

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Load the dataset
df = pd.read_csv('/storage/emulated/0/pythonproject2/netflix_titles.csv')

# Initial checks
print("Dataset shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())

# Handle missing data
df.dropna(subset=['title', 'type'], inplace=True)
df['director'].fillna("Unknown", inplace=True)
df['country'].fillna("Unavailable", inplace=True)
df['cast'].fillna("Unavailable", inplace=True)
df['rating'].fillna("Unavailable", inplace=True)

# Movies vs TV Shows
sns.countplot(data=df, x='type')
plt.title('Movies vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

# Top 10 Countries
top_countries = df['country'].value_counts().head(10)
top_countries.plot(kind='barh', color='skyblue')
plt.title('Top 10 Countries by Content')
plt.xlabel('Number of Titles')
plt.gca().invert_yaxis()
plt.show()

# Most Common Genres
genres = df['listed_in'].str.split(', ')
flat_list = [genre for sublist in genres.dropna() for genre in sublist]
genre_counts = Counter(flat_list).most_common(10)
labels, values = zip(*genre_counts)

plt.barh(labels, values, color='lightgreen')
plt.title('Top 10 Most Common Netflix Genres')
plt.xlabel('Number of Titles')
plt.gca().invert_yaxis()
plt.show()