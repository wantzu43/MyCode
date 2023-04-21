# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:07:13 2023

@author: Wantzu
"""

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

diabetes = datasets.load_diabetes()

X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
target = pd.DataFrame(diabetes.target, columns=["MEDV"])
y = target["MEDV"]

#Q1
lm = LinearRegression()
lm.fit(X, y)

predicted_number = lm.predict(X)

MSE1 = np.mean((y - predicted_number)**2)
R1 = lm.score(X, y)
print("Q1:不分割資料集，請求出MSE及R平方")
print("MSE:", MSE1)
print("R-squared:", R1)

#Q2
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.25, random_state=100)
lm2 = LinearRegression()
lm2.fit(XTrain, yTrain)

pred_test = lm2.predict(XTest)

MSE2 = np.mean((yTest - pred_test)**2)
R2 = lm2.score(XTest, yTest)
print("\nQ2:請分割成訓練資料集及測試資料集的比率為3:1，亂數種子為100，並求出MSE及R平方")
print("MSE:", MSE2)
print("R-squared:", R2)

#Q3
XTrain1, XTest1, yTrain1, yTest1 = train_test_split(X, y, test_size=0.20, random_state=100)
lm3 = LinearRegression()
lm3.fit(XTrain1, yTrain1)

pred_test1 = lm3.predict(XTest1)

MSE3 = np.mean((yTest1 - pred_test1)**2)
R3 = lm3.score(XTest1, yTest1)
print("\nQ3:請分割成訓練資料集及測試資料集的比率為4:1，亂數種子為100，並求出MSE及R平方")
print("MSE:", MSE3)
print("R-squared:", R3)

#Q4
print("\nQ4:請問您會選擇以上1、2、3哪種方式建立模型?原因為何?")
print("選擇2，資料集解釋能力較高，且誤差值比方法1小，而方法3的誤差值較低但資料集解釋能力卻比較低，屬不合理，用八成跟七成的差距不大，以成本考量會選擇七成。")
