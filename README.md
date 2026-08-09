# Student Performance Prediction using Linear Regression

## Overview

This project predicts a student's final academic grade (**G3**) using a Machine Learning model based on **Linear Regression**. The model analyzes various academic and personal factors such as study time, travel time, attendance, previous grades, internet access, and family support to estimate the student's final performance.

This project was developed as part of my Machine Learning learning journey to understand the complete workflow of building a predictive model using Python and Scikit-learn.

---

## Problem Statement

Educational institutions often want to identify students who may need additional academic support before their final examinations.

The objective of this project is to predict the final grade (**G3**) of a student based on historical academic performance and other influencing factors.

---

## Dataset

Dataset: Student Performance Dataset (Portuguese Students)

Number of Records: **649**

Number of Features: **33**

Target Variable:

* G3 (Final Grade)

---

## Features Used

The following features were selected for training the model:

* Health
* Internet Access
* Travel Time
* Higher Education Aspiration
* School Support
* Family Support
* Study Time
* Previous Failures
* Absences
* First Period Grade (G1)
* Second Period Grade (G2)

Categorical columns were converted into numerical values before training the model.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* VS Code

---

## Project Workflow

1. Load the dataset using Pandas.
2. Explore the dataset.
3. Check for missing values.
4. Convert categorical data into numerical format.
5. Select important features.
6. Split the dataset into training and testing sets.
7. Train the Linear Regression model.
8. Predict student final grades.
9. Evaluate model performance using the R² Score.

---

## Machine Learning Model

Algorithm Used:

* Linear Regression

Reason for Choosing:

Linear Regression is a simple and effective supervised learning algorithm suitable for predicting continuous numerical values such as student grades.

---

## Model Performance

Evaluation Metric:

* R² Score

Model Accuracy:

* **R² Score: 0.865**

The model explains approximately **86.5% of the variation** in students' final grades based on the selected input features.

---

## Project Structure

```text
Student-Performance-Prediction/
│
├── data/
│   └── student-por.csv
│
├── student_prediction.py
│
├── README.md
│
└── requirements.txt
```

---

## Future Improvements

* Perform Exploratory Data Analysis (EDA)
* Visualize correlations using heatmaps
* Compare multiple Machine Learning algorithms
* Apply Feature Engineering
* Improve model performance using Random Forest Regression
* Build a web application using Flask or Streamlit for predictions

---

## Learning Outcomes

Through this project I learned:

* Data preprocessing using Pandas
* Handling categorical features
* Handling missing values
* Feature selection
* Train-Test Split
* Building a Linear Regression model
* Model evaluation using the R² Score
* Making predictions using Scikit-learn

---

## Author

**Karthikeyan M**

B.Tech Information Technology

Bannari Amman Institute of Technology

GitHub:
https://github.com/KARTHIKEYAN-M-07
