import pandas as pd
import joblib

model = joblib.load("fuse_model.pk1")

k_input = float(input("Enter fuse rating constant (k): "))
current_input = float(input("Enter current flowing through the fuse (A): "))
current_squared_input = current_input ** 2

new_data = pd.DataFrame([[k_input, current_input, current_squared_input]], columns = ["k", "current", "current_squared"])
prediction = model.predict(new_data)

print(f"Predicted time to blow: {prediction[0]:.4f} seconds")
