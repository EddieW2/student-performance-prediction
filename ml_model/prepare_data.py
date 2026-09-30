import pandas as pd


data = pd.read_csv("ml_model/student-mat.csv", sep=";")

print(data.head())

print("\nColumns:")
print(data.columns)

print("\nDataset size:")
print(data.shape)