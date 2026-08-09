import pandas as pd

# Load data
df = pd.read_csv("data/student-por.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())
df["internet"] = df["internet"].map({
    "yes": 1,
    "no": 0
})
df["higher"] = df["higher"].map({"yes": 1, "no": 0})
df["schoolsup"] = df["schoolsup"].map({"yes": 1, "no": 0})
df["famsup"] = df["famsup"].map({"yes": 1, "no": 0})

# Select features
X = df[[
    "health",
    "internet",
    "traveltime",
    "higher",
    "schoolsup",
    "famsup",
    "studytime",
    "failures",
    "absences",
    "G1",
    "G2"
]]


# Target
y = df["G3"]

# Spliting dataset
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Creating model
from sklearn.linear_model import LinearRegression

model = LinearRegression()

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)
print("R2  :", r2)


# Predict a new student
new_student = pd.DataFrame({
    "health": [5],
    "internet": [1],
    "traveltime": [2],
    "higher": [1],
    "schoolsup": [0],
    "famsup": [1],
    "studytime": [3],
    "failures": [0],
    "absences": [2],
    "G1": [12],
    "G2": [13]
})


result = model.predict(new_student)

print("\nPredicted Final Grade:")
print(result[0]) 