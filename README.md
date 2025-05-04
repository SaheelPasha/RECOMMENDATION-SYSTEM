# RECOMMENDATION-SYSTEM

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: Saheel Pasha

**INTERN ID**: CT04WT62

**DOMAIN**:  Machine Learning

**DURATION**: 4 WEEKS

**MENTOR**: NEELA SANTOSH

# DESCRIPTION

# What is a Recommendation System?
A Recommendation System is a type of intelligent system that suggests items to users based on their preferences or behavior. These systems are widely used in platforms like Amazon (for products), Netflix (for movies), Spotify (for music), and even YouTube (for videos). Their main goal is to predict what a user would like and show relevant options to improve engagement and satisfaction.
Imagine going to a shopping website and seeing a list titled “Recommended for You”. This list is generated using a recommendation system that analyzes what you have liked or interacted with before.

# Types of Recommendation Systems
There are mainly three types of recommendation systems:
1. Content-Based Filtering
Works by analyzing the features of the items.
For example, if you like action movies, it recommends other action movies.
It matches user preferences with item characteristics.
2. Collaborative Filtering
Based on user behavior and interactions.
Recommends items based on what similar users liked.
Doesn’t need item details—just user ratings or history.
This is the most popular and commonly used method.
3. Hybrid Systems
Combines both content-based and collaborative filtering.
More accurate but also more complex.

# How Collaborative Filtering Works
Collaborative filtering assumes:
If User A and User B liked the same things in the past,
Then what B likes now might also interest A.
There are two common methods:
User-based Collaborative Filtering: Recommends items liked by users who are similar to you.
Item-based Collaborative Filtering: Recommends items similar to what you’ve liked before.
For example:
User A likes [Movie 1, Movie 2]
User B likes [Movie 1, Movie 2, Movie 3]
So, Movie 3 is likely recommended to User A.

# Matrix Factorization
To handle large datasets, we use Matrix Factorization techniques like SVD (Singular Value Decomposition). It converts the user-item interaction matrix into smaller, dense matrices that are easier to compute and make predictions from.
Let’s say we have a table of users and their ratings for movies. Most cells will be empty (not every user rated every movie). Matrix factorization helps in filling these gaps with estimated values (predicted ratings).

# Tools and Libraries
To build a recommendation system in Python, common libraries include:
Pandas (for data manipulation)
Scikit-Surprise (specialized for building collaborative models)
SciKit-learn (for general ML tools)
TensorFlow/PyTorch (if using deep learning approaches)

# Evaluation of Recommendation Systems
After building the model, we test its accuracy. Common evaluation metrics:
RMSE (Root Mean Square Error): Measures how close predicted ratings are to actual ratings.
Precision and Recall: Used in top-N recommendations to check how many relevant items were suggested.
A good recommendation system should:
Be accurate (predict well)
Be scalable (work with many users/items)
Handle cold start (new users or items with no data)

# Real-life Examples
Netflix recommends shows based on your past viewing history and what similar users watched.
Amazon suggests products based on your browsing and purchases, and others’ activities.
Spotify creates playlists like Discover Weekly based on what others with similar music taste liked.

# Conclusion
A recommendation system is a powerful tool that helps users discover new content and helps companies increase engagement and revenue. By using collaborative filtering, machine learning, or deep learning, these systems can provide personalized experiences across industries. Understanding how to build one using libraries like Surprise in Python is a great starting point for any data science or machine learning enthusiast.

# OUTPUT 1
![Image](https://github.com/user-attachments/assets/31b28b14-f413-4750-b6f2-6b8cb13f7fd4)

# OUTPUT 2
![Image](https://github.com/user-attachments/assets/0cd267c8-476d-4f3a-92a9-d828314d49f7)

# OUTPUT




