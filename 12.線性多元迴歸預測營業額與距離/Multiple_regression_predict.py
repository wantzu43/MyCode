# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:37:47 2023

@author: Wantzu
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

area_distance = np.array([[10,80],[8,30],[8,200],[5,200],[7,300],[8,230],[7,50],[9,20],[6,330],[9,180]])
sale = np.array([46, 36, 37, 20, 24, 29, 36, 43, 20, 36])

x = pd.DataFrame(area_distance, columns=["Area","Distance"])
y = pd.DataFrame(sale, columns=["Sale"])

lm = LinearRegression()
lm.fit(x,y)

new_area_distance = pd.DataFrame(np.array([[10,100],[15,80]]), columns=["Area","Distance"])
predicted_sale = lm.predict(new_area_distance)
print("Q1:")
print("店面積 : 10、距捷運 : 100\n預測月營收為 : {} 萬元".format(predicted_sale[0]))
print("店面積 : 15、距捷運 : 80\n預測月營收為 : {} 萬元".format(predicted_sale[1]))

print('='*20)

area_sale = np.array([[10,46],[8,36],[8,37],[5,20],[7,24],[8,29],[7,36],[9,43],[6,20],[9,36]])
distance = np.array([80, 30, 200, 200, 300, 230, 50, 20, 330, 180])

x1 = pd.DataFrame(area_sale, columns=["Area","Sale"])
y1 = pd.DataFrame(distance, columns=["Distance"])

lm2 = LinearRegression()
lm2.fit(x1,y1)

new_area_sale = pd.DataFrame(np.array([[8,40],[6,22]]), columns=["Area","Sale"])
predicted_distance = lm2.predict(new_area_sale)
print("Q2:")
print("店面積 : 8、月營收 : 40\n預測距捷運為 : {} 公尺".format(predicted_distance[0]))
print("店面積 : 6、月營收 : 22\n預測距捷運為 : {} 公尺".format(predicted_distance[1]))