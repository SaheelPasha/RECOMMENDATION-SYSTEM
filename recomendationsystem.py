from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy
import pandas as pd
ratings_dict = {
    "userID": ["A", "A", "A", "B", "B", "C", "C", "C", "D", "D"],
    "itemID": ["Toy Story", "Jumanji", "Avengers", "Toy Story", "Jumanji", "Avengers", "Titanic", "Toy Story", "Titanic", "Avengers"],
    "rating": [4, 3, 5, 2, 2, 4, 5, 2, 3, 5]
}

df = pd.DataFrame(ratings_dict)
df

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[["userID", "itemID", "rating"]], reader)

trainset, testset = train_test_split(data, test_size=0.2, random_state=42)
model = SVD()
model.fit(trainset)

predictions = model.test(testset)

for prediction in predictions:
    print(f"User: {prediction.uid} | Item: {prediction.iid} | Actual: {prediction.r_ui} | Predicted: {round(prediction.est, 2)}")

rmse = accuracy.rmse(predictions)
