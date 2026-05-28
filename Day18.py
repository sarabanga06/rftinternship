import pandas as pd
import matplotlib.pyplot as plt

# Creating Dataset
data = {
    'Movie_Name': ['Inception', 'Avengers', 'Titanic', 'Joker', 'Interstellar',
                   'Frozen', 'Bahubali', 'Dangal', 'Avatar', 'KGF'],
    
    'Rating': [8.8, 8.4, 7.9, 8.5, 8.7,
               7.5, 8.2, 8.4, 7.8, 8.3],
    
    'Genre': ['Sci-Fi', 'Action', 'Romance', 'Drama', 'Sci-Fi',
              'Animation', 'Action', 'Sports', 'Sci-Fi', 'Action'],
    
    'Revenue': [829, 2798, 2187, 1074, 701,
                1280, 650, 310, 2923, 250]
}

# Convert into DataFrame
df = pd.DataFrame(data)

print("Movie Dataset:\n")
print(df)

# Highest Rated Movies
print("\nHighest Rated Movies:")
highest = df.sort_values(by='Rating', ascending=False)
print(highest[['Movie_Name', 'Rating']])

# Most Profitable Genres
print("\nMost Profitable Genres:")
genre_profit = df.groupby('Genre')['Revenue'].sum()
print(genre_profit)

# Top 5 Movies
print("\nTop 5 Movies:")
top5 = df.sort_values(by='Revenue', ascending=False).head(5)
print(top5[['Movie_Name', 'Revenue']])

# Correlation between Rating & Revenue
correlation = df['Rating'].corr(df['Revenue'])
print("\nCorrelation between Rating and Revenue:")
print(correlation)

# Visualization 1 - Genre vs Revenue
plt.figure(figsize=(8,5))
genre_profit.plot(kind='bar')
plt.title("Genre vs Revenue")
plt.xlabel("Genre")
plt.ylabel("Revenue")
plt.show()

# Visualization 2 - Rating Distribution
plt.figure(figsize=(8,5))
plt.hist(df['Rating'], bins=5)
plt.title("Rating Distribution")
plt.xlabel("Ratings")
plt.ylabel("Frequency")
plt.show()