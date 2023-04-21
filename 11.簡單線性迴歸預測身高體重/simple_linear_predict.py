# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:22:55 2023

@author: Wantzu
"""

#匯入套件
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

height = np.array([147, 163, 159, 155, 163, 158, 172, 161, 153, 161])
weight = np.array([41, 60, 47, 53, 48, 55, 58.5, 49, 46, 52.5])

x = pd.DataFrame(height, columns=["Height"])
y = pd.DataFrame(weight, columns=["Weight"])

lm1 = LinearRegression()
lm2 = LinearRegression()
lm1.fit(x, y)
lm2.fit(y, x)


new_height = pd.DataFrame(np.array([155, 165, 180]), columns=["Height"])
predicted_weight = lm1.predict(new_height)
print("1.")
print("預測的三組體重:")
print("身高 預測體重\n155 : %.1f \n165 : %.1f \n180 : %.1f"%(predicted_weight[0], predicted_weight[1], predicted_weight[2]))
#for i in range(len(predicted_weight)):
#    print("{:.1f}".format(float(predicted_weight[i])))
print("迴歸係數:", lm1.coef_)
print("截距:", lm1.intercept_)
print('='*40)

new_weight = pd.DataFrame(np.array([55, 65, 70]), columns=["Weight"])
predicted_height = lm2.predict(new_weight)
print("2.")
print("預測的三組身高:")
print("體重 預測身高\n55 : %d \n65 : %d \n70 : %d"%(predicted_height[0], predicted_height[1], predicted_height[2]))
#for i in range(len(predicted_height)):
#    print(int(predicted_height[i]))
plt.scatter(weight, height)
regression_height = lm2.predict(y)
plt.plot(weight, regression_height, color="blue")
plt.plot(new_weight, predicted_height, color="red", marker="o", markersize=10)
plt.show()
