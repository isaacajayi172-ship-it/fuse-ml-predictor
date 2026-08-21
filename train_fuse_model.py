import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error

data = pd.read_csv("clean_fuse_data.csv")

X = data[["k", "current"]]
y = data["time_taken_to_blow"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

print(X_train.shape)
print(X_test.shape)

model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(predictions[:5])
print(y_test[:5])

mae = mean_absolute_error(y_test, predictions)
mape = mean_absolute_percentage_error(y_test, predictions)
print("MAE:", mae)
print("MAPE:", mape)