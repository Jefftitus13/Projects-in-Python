# Visualization through pandas and matplotlib
# Loading the dataset
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("imdb_top_1000.csv")
print(df)

# Code for Barchart
filtered_df = df[(df['Released_Year'] >= '1995') & (df['Released_Year'] <= '2001')]
rated_movies = filtered_df[filtered_df['IMDB_Rating'] > 8.5]
yearly_counts = rated_movies['Released_Year'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.bar(yearly_counts.index, yearly_counts.values, color='red')
plt.title('The Golden Year of Cinema: Films with IMDb Ratings Exceeding 8.5')
plt.xlabel('Year of Release')
plt.ylabel('Number of Movies')
plt.grid(axis='y', linestyle='--', alpha=0.7, color='black')
plt.yticks(range(0, max(yearly_counts.values)+1, 2))

plt.show()

# Code for scatterplot
df = df.dropna(subset=['Genre', 'Meta_score'])
df['Genres_list'] = df['Genre'].str.split(',')
genre_metascore_df = df.explode('Genres_list')[['Genres_list', 'Meta_score']]
genre_metascore_df['Meta_score'] = pd.to_numeric(genre_metascore_df['Meta_score'], errors='coerce')

plt.figure(figsize=(12, 8))
plt.scatter(genre_metascore_df['Genres_list'], genre_metascore_df['Meta_score'], alpha=0.3, c='black')
plt.title('Scatter Plot of Metascore by Genre')
plt.xlabel('Genre')
plt.ylabel('Metascore')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

