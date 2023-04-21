# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 13:44:32 2023

@author: Wantzu
"""

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import linear_model, tree, neighbors, cluster
import sklearn.metrics as sm

wine = datasets.load_wine()

X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = wine.target



#Q1
k=3
kmeans = cluster.KMeans(n_clusters=k, random_state=12)
kmeans.fit(X)
#print(kmeans.labels_)
#print(y)
#修正標籤 0 要改成1、 1要改成0
pred_y = np.choose(kmeans.labels_, [1,0,2]).astype(np.int64)
#print(pred_y)
print("Q1:根據紅酒種類資料集，請使用K-Means分類演算法，分成三類，輸出其正確率。")
print("Answer: ")
print("K-Means演算法正確率為(績效矩陣): ", sm.accuracy_score(y, pred_y))

print()
print("*"*60)
print()

#Q2
print("Q2:請以目前所學的，選擇您認為最適當的分類演算法，輸出其正確率，並與K-Means演算法進行比較。")
print("Answer: ")
target = pd.DataFrame(wine.target, columns=["MEDV"])
y1 = target["MEDV"]

#線性迴歸
lm = linear_model.LinearRegression()
lm.fit(X, y1)
print("複迴歸正確率為 : ", lm.score(X, y1))

#邏輯迴歸
logistic = linear_model.LogisticRegression()
logistic.fit(X, y1)
print("邏輯迴歸正確率為 : ", logistic.score(X, y))

#決策樹
#======找適當max_depth值
"""
score = []
for i in range(1,10):
    dtree_test = tree.DecisionTreeClassifier(max_depth = i, random_state=100)
    dtree_test.fit(X, y1)
    score.append(dtree_test.score(X, y1))
scoredata = pd.DataFrame(score, index=[j for j in range(1,10)], columns=["score"])
print(scoredata.sort_values("score", ascending = False).head(10))
#適當的值為5
"""
#======找適當max_depth值
dtree = tree.DecisionTreeClassifier(max_depth = 5, random_state=100)
dtree.fit(X, y1)
print("決策樹正確率為 : ", dtree.score(X, y1))

#KNN
#======找適當n_neighbors值
"""
score = []
for i in range(1,179,2):
    knn_test = neighbors.KNeighborsClassifier(n_neighbors=i)
    knn_test.fit(X, y1)
    score.append(knn_test.score(X, y1))
scoredata = pd.DataFrame(score, index=[j for j in range(1,179,2)], columns=["score"])
print(scoredata.sort_values("score", ascending = False).head(10))

適當的值為3
"""
#======找適當n_neighbors值
knn = neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y1)
print("KNN正確率為 : ", knn.score(X, y1))

#K-Means
print("K-Means演算法正確率為 : ", sm.accuracy_score(y, pred_y))


#總結
print("總結 : 由於複迴歸屬於數值，邏輯迴歸也只適用於二元分類，所以只須比較決策樹與KNN，決策樹準確率較高，而決策樹是監督式學習，K-Means演算法是非監督式學習，所以K-Means準確率較低屬正常的")
print()
print("*"*60)
print()