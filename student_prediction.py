import pandas as pd

data = pd.read_csv('data/student-por.csv')
print(data.head())
print(data.columns)
print(data.describe())
print(data.info())