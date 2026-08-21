import pandas as pd

data = pd.read_csv("fuse_data.csv")

print(data.isna().sum())
print(data.shape)

data = data.dropna()
print(data.shape)

data.to_csv("clean_fuse_data.csv", index = False)