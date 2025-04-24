# Step 1: Import libraries
import pandas as pd
import numpy as np

# Step 2: Create sample ratings data
# (user_id, movie_title, rating)
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4],
    'movie': ['Avengers', 'Inception', 'Titanic', 'Avengers', 'Titanic', 'Inception', 'Avengers', 'Titanic'],
    'rating': [5, 4, 3, 5, 2, 4, 4, 5]
}
df = pd.DataFrame(data)

# Step 3: Create a user-movie matrix
user_movie_matrix = df.pivot_table(index='user_id', columns='movie', values='rating')
print("User-Movie Matrix:\n", user_movie_matrix)

# Step 4: Fill missing values with 0 (optional for cosine similarity)
filled_matrix = user_movie_matrix.fillna(0)

# Step 5: Calculate similarity between users (cosine similarity)
from numpy.linalg import norm

def cosine_similarity(u, v):
    return np.dot(u, v) / (norm(u) * norm(v))

similarities = {}
target_user_id = 1
target_vector = filled_matrix.loc[target_user_id].values

for user_id in filled_matrix.index:
    if user_id != target_user_id:
        sim = cosine_similarity(target_vector, filled_matrix.loc[user_id].values)
        similarities[user_id] = sim

print("\nSimilarities with User 1:", similarities)

# Step 6: Pick the most similar user
most_similar_user = max(similarities, key=similarities.get)
print("\nMost similar user to User 1 is User", most_similar_user)

# Step 7: Recommend movies that similar user rated but target user hasn't
user1_movies = user_movie_matrix.loc[target_user_id]
similar_user_movies = user_movie_matrix.loc[most_similar_user]

recommend = []
for movie in user_movie_matrix.columns:
    if pd.isna(user1_movies[movie]) and not pd.isna(similar_user_movies[movie]):
        recommend.append((movie, similar_user_movies[movie]))

recommend = sorted(recommend, key=lambda x: x[1], reverse=True)

# Step 8: Show top recommendations
print("\nRecommended Movies for User 1:")
for movie, rating in recommend:
    print(f"{movie} (Predicted rating: {rating})")
