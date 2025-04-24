# RECOMMENDATION-SYSTEM

*COMPANY*: CODTECH IT SOLUTIONS  
*NAME*: MOLIGE SAI CHARAN  
*INTERN ID*: CT04WY43  
*DOMAIN*: MACHINE LEARNING  
*DURATION*: 4 WEEKS  
*MENTOR*: NEELA SANTOSH

Movie Recommendation System using Collaborative Filtering (User-Based):

In this task for the CODTECH internship, I developed a basic Recommendation System that suggests movies to users based on the ratings provided by other users with similar tastes. The main goal of this system is to identify users who rate movies similarly and use their preferences to make movie suggestions. This is a classic example of Collaborative Filtering, a technique widely used by platforms like Netflix, Amazon, and YouTube to recommend content.

Tools and Technologies Used:

For this project, I specifically avoided using complex or less accessible third-party libraries and instead focused on building the recommendation system using Python’s built-in and standard data science libraries:

Pandas: Used for handling structured data, creating dataframes, and organizing user-movie ratings into a matrix.

NumPy: Used for numerical operations, especially in calculating cosine similarity between users.

Jupyter Notebook: Used to write and run Python code interactively, which allowed me to test the logic step-by-step and view outputs instantly.

No installation of external machine learning libraries like scikit-surprise or TensorFlow was required, which makes this project simple and beginner-friendly.

How It Works:

The recommendation system is based on User-Based Collaborative Filtering. The core idea is that if two users have rated some movies similarly, they are likely to enjoy similar types of movies.

Here’s a step-by-step explanation of how I built the system:

Data Creation:
I created a small dataset manually, containing movie ratings by a few users. This dataset includes user IDs, movie names, and the corresponding ratings each user gave.

User-Movie Matrix:
Using pandas.pivot_table, I converted the flat data into a User-Movie Matrix, where each row represents a user, each column represents a movie, and each cell shows the rating a user has given to a particular movie. Missing ratings appear as NaN.

Filling Missing Values:
For similarity calculations, I filled missing values with 0, though in real-world systems, more advanced techniques like matrix factorization would be used. But for simplicity, this step was sufficient for a beginner project.

Cosine Similarity:
I used the cosine similarity formula from basic linear algebra to measure how similar users are based on their rating vectors. Cosine similarity gives a score between -1 and 1, where 1 means the users are very similar.

Finding Most Similar User:
I calculated the similarity between the target user and all other users. The user with the highest similarity score was considered the most similar. This user’s watched movies were then considered for recommendation.

Recommendation Logic:
I recommended movies that the most similar user had rated but the target user hadn’t watched yet. This way, we try to suggest only new and likely relevant movies.

Example Output:

In the tested example, I calculated similarities between User 1 and other users. It turned out that User 3 was most similar to User 1 based on the ratings they gave. The system then checked if User 3 had rated any movie that User 1 hadn’t seen, and if so, those were recommended.

Learning Outcome:

As a beginner with no prior experience in building recommendation systems, this project taught me the basics of:

How collaborative filtering works in theory and in code.

How similarity between users or items can be measured using cosine similarity.

How to handle missing data and reshape datasets for analysis.

How to recommend items using simple logic, without relying on black-box machine learning models.

This approach gives a strong foundation and makes it easier to understand more advanced systems in the future, like Matrix Factorization or Deep Learning-based recommendations.

Final Notes:

This recommendation system is basic but functional, and it gives a solid understanding of the logic used by modern recommendation engines.

It is also completely customizable and scalable. With more data or better similarity metrics, it can be extended for larger use cases.

The best part is that I built this from scratch using only basic tools, proving that even beginners can build intelligent systems without relying on complex tools.


#Output

![Image](https://github.com/user-attachments/assets/5aa04c1b-905e-4482-8394-9b640d4a5177)

