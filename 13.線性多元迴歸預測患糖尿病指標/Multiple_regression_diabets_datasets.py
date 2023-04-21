# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:24:18 2023

@author: Wantzu
"""

import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

diabetes = datasets.load_diabetes()

x = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
x1 = x[['age', 'sex', 'bmi', 'bp']]
target = pd.DataFrame(diabetes.target, columns=["MEDV"])
y = target["MEDV"]

#Q1
lm = LinearRegression()
lm.fit(x, y)

predicted_number = lm.predict(x)
print(predicted_number)

plt.scatter(y, predicted_number)
plt.xlabel("Quantitative Measure")
plt.ylabel("Predicted Quantitative Measure")
plt.title("Quantitative Measure vs Predicted Quantitative Measure")
plt.show()

#Q2
lm1 = LinearRegression()
lm1.fit(x1, y)

predicted_number1 = lm1.predict(x1)
print(predicted_number1)

plt.scatter(y, predicted_number1)
plt.xlabel("Quantitative Measure")
plt.ylabel("Predicted Quantitative Measure")
plt.title("Quantitative Measure vs Predicted Quantitative Measure")
plt.show()