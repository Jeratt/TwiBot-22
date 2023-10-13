import pandas as pd

results = pd.read_csv("reproducibility.csv")
print(results)

print(results.mean())
print(results.std())