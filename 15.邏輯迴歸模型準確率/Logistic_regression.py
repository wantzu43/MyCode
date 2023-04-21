# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:30:18 2023

@author: Wantzu
"""

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, linear_model

breast_cancaer = datasets.load_breast_cancer()
X = pd.DataFrame(breast_cancaer.data, columns=breast_cancaer.feature_names)

target = pd.DataFrame(breast_cancaer.target, columns=["MEDV"])
y = target["MEDV"]
#print(X1.shape)
#print(y.shape)
logistic = linear_model.LogisticRegression()
logistic.fit(X, y)

#Q1
print("Q1:")
#print("迴歸係數:", logistic.coef_)
#print("截距:", logistic.intercept_)
print("混淆矩陣:")
preds = logistic.predict(X)
print(pd.crosstab(y, preds))

print("混淆矩陣算出的準確率:", ((193+346)/(193+346+11+19)))
print("準確率:", logistic.score(X, y))

#Q2
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.3, random_state=10)
logistic2 = linear_model.LogisticRegression()
logistic2.fit(XTrain, yTrain)
print("\nQ2:")
print("混淆矩陣:")
preds2 = logistic2.predict(XTest)
print(pd.crosstab(yTest, preds2))

print("混淆矩陣算出的準確率:", ((56+106)/(56+106+6+3)))
print("準確率:", logistic2.score(XTest, yTest))

#Q3
print("\nQ3:")
coef_abs = pd.DataFrame(breast_cancaer.feature_names, columns=["feature"])
coef_abs["estimatedCoefficients"] = abs(logistic.coef_[0])
print("迴歸係數絕對值前五名:")
print(coef_abs.sort_values("estimatedCoefficients", ascending = False).head(5))
X1 = X[['mean radius','worst radius','worst concavity','worst compactness','worst texture']]
logistic3 = linear_model.LogisticRegression()
logistic3.fit(X1, y)
print("*"*30)
print("混淆矩陣:")
preds3 = logistic3.predict(X1)
print(pd.crosstab(y, preds3))

print("混淆矩陣算出的準確率:", ((197+346)/(197+346+11+15)))
print("準確率:", logistic3.score(X1, y))
print("選擇此五項的原因為:")
print("""將全部資料使用羅集迴歸建立訓練模型所產生的應變數y對應的「迴歸係數」取絕對值後，
再取前五大的迴歸係數絕對值來做為欄位，絕對值後值越大的代表敏感度越高，因此準確率會比較高。""")
print("="*40)