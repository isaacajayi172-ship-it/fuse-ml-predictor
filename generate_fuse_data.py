import random
import pandas as pd 

rows = []

for i in range(1000):
    k = random.uniform(50, 500)
    current = random.uniform(1,50)
    time_taken_to_blow = k / (current ** 2)
    print(time_taken_to_blow)
    rows.append({"k": k, "current": current, "time_taken_to_blow": time_taken_to_blow})

data = pd.DataFrame(rows)
print(data.head())
data.to_csv("fuse_data.csv", index = False)

