import pandas as pd

#Loading the data
df = pd.read_csv("series_data.csv")
print(df)

#We going to remove column "Poster_Link" because there is nothing to analyse
df = df.drop('Poster_Link', axis=1)
print(df)

#Finding average ratings of series
Average_rating = df['IMDB_Rating'].mean().round(2)
print("Average rating:", Average_rating)

#Finding maximum IMDB rating along with series title
max_row = df.loc[df['IMDB_Rating'].idxmax()]
max_series_name = max_row['Series_Title']
max_imdb = max_row['IMDB_Rating']

print(f"Series: {max_series_name}, IMDB: {max_imdb}")

#Finding minimum IMDB rating along with series title
min_row = df.loc[df['IMDB_Rating'].idxmin()]
min_series = min_row['Series_Title']
min_imdb = min_row['IMDB_Rating']

print(f"Series: {min_series}, IMDB: {min_imdb}")

#To get full data about the highest and lowest series
max_row = df.loc[df['IMDB_Rating'].idxmax()]
max_series_name = max_row['Series_Title']
max_imdb = max_row['IMDB_Rating']

min_row = df.loc[df['IMDB_Rating'].idxmin()]
min_series = min_row['Series_Title']
min_imdb = min_row['IMDB_Rating']

print(max_row, min_row, sep=' ')

#Finding which series has highest votes
max_votes = df.loc[df['No_of_Votes'].idxmax()]
a = max_votes['Series_Title']
b = max_votes['No_of_Votes']
print(max_votes)

#Finding which series has lowest votes
min_votes = df.loc[df['No_of_Votes'].idxmin()]
x = min_votes['Series_Title']
y = min_votes['No_of_Votes']
print(min_votes)

#finding which genres has highest number of votes
df.set_index('Genre', inplace=True)

max_votes_genre = df.groupby('Genre')['No_of_Votes'].sum().idxmax()
max_votes_count = df.groupby('Genre')['No_of_Votes'].sum().max()
print("Genre with the highest number of votes:")
print(f"Genre: {max_votes_genre}")
print(f"Total No. of Votes: {max_votes_count}")

#To get particular genre
df.loc[df['Genre']=="Action"] 
#to figure out series using star's name
df.loc[df['Star1']=="Charlie Cox"]

#finding which cattegory of certificate has 8.0+ imdb ratings
df.loc[(df['Certificate']=='A')&(df['IMDB_Rating']>8.0)]
#Output notes: There are 23 series with an 'A' certificate and ratings exceeding 8.0.

df.loc[(df['Certificate']=='18+') & (df['IMDB_Rating']>8.0)]
#Output notes: There are 23 series with a '18+' certificate and ratings exceeding 8.0.

df.loc[(df['Certificate']=='13+') & (df['IMDB_Rating']>8.0)]
#Output notes: There are 4 series with a '13+' certificate and ratings exceeding 8.0.

df.loc[(df['Certificate']=='U') & (df['IMDB_Rating']>8.0)]
#Output notes: There are 18 series with an 'U' certificate and ratings exceeding 8.0.

df.loc[(df['Certificate']=='UA') & (df['IMDB_Rating']>8.0)]
#Output notes: There are 8 series with an 'UA' certificate and ratings exceeding 8.0.

df.loc[(df['Certificate']=='15') & (df['IMDB_Rating']>8.0)]
#Output notes: There are 2 series with a '15' certificate and ratings exceeding 8.0.

df.loc[(df['Certificate']=='18') & (df['IMDB_Rating']>8.0)]
#Output notes: With a significant difference, the series with an '18' certificate has the highest number of 8.0 ratings and 'Breaking bad' being top rated with 9.5.

#finding which genre is more sucesful in netflix
df.loc[(df['Genre']=='Drama') & (df['IMDB_Rating']>8.0)]
#Output notes: There are 28 'Drama' genre series exceeding 8.0 rating and the highest is 'West Wing' with 8.8

df.loc[(df['Genre']=='Thriller') & (df['IMDB_Rating']>8.0)]
#Output notes: There is only 1 'Thriller' genre series exceeding 8.0 rating

df.loc[(df['Genre']=='Crime, Drama, Thriller') & (df['IMDB_Rating']>8.0)]
#Output notes: There are 25 'Crime, Drama, Thriller' genre series exceeding 8.0 rating and the highest is 'Breaking Bad' with 9.5

df.loc[(df['Genre']=='Action, Drama, Thriller') & (df['IMDB_Rating']>8.0)]
#Output notes: There are 5 'Action, Drama, Thriller' genre series exceeding 8.0 rating and the highest is 'Aranyelet' with 8.8

df.loc[(df['Genre']=='Animation, Action, Adventure') & (df['IMDB_Rating']>8.0)]
#Output notes: There are 61 'Animation, Action, Adventure' genre series exceeding 8.0 rating which makes the largest list in my analysis and the highest rated series is 'Avatar: the last airbender' with 9.2

#Conclusion: Based on my analysis, the 'Animation, Action, Adventure' genre is the most binge-worthy and liked genre among the Netflix community.
