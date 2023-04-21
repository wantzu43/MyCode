# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 16:49:01 2023

@author: Wantzu
"""
import math
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import neighbors, tree
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
target = pd.DataFrame(iris.target, columns=["D"])
y = target["D"]

k = 50

#Q1
print("Q1:請將全部資料使用KNN建立訓練模型(K設定為50)後，查看其模型正確率。並與決策樹(層數設定為4)的模型正確率做比較。\n")

#KNN模型
knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)
print("KNN模型的正確率為:", knn.score(X, y))

#決策樹模型
dtree = tree.DecisionTreeClassifier(max_depth=4)
dtree.fit(X, y)
print("決策樹模型的正確率為:", dtree.score(X, y))

print("="*50)

#Q2
print("Q2:請將資料分割成3:2的訓練資料集及測試資料集(亂數種子設定為50)，並使用KNN演算法。之後選擇您認為最適合的K個個數，並輸入其模型正確率。\n")
XTrain,  XTest, yTrain, yTest = train_test_split(X, y, test_size=0.4, random_state=50)

#找出使準確率最高的K值
score = []
for i in range(1,91,2):
    knn_test = neighbors.KNeighborsClassifier(n_neighbors=i)
    knn_test.fit(XTrain, yTrain)
    
    score.append(knn_test.score(XTest, yTest))

scoredata = pd.DataFrame(score, index=[j for j in range(1,91,2)], columns=["score"])
print(scoredata.sort_values("score", ascending = False).head(10))
#====================================================================================
prepare_k = int(math.sqrt(len(XTrain))) #將樣本數開根號
print("***以樣本數開根號來找適合的K個數為:", prepare_k)
#KNN模型
knn2 = neighbors.KNeighborsClassifier(n_neighbors=prepare_k)
knn2.fit(XTrain, yTrain)
print("K的個數為{}時，KNN模型的正確率為: {}".format(prepare_k, knn2.score(XTest, yTest)))

knn3 = neighbors.KNeighborsClassifier(n_neighbors=5)
knn3.fit(XTrain, yTrain)
print("K的個數為5時，KNN模型的正確率為:", knn3.score(XTest, yTest))

knn4 = neighbors.KNeighborsClassifier(n_neighbors=15)
knn4.fit(XTrain, yTrain)
print("K的個數為15時，KNN模型的正確率為:", knn4.score(XTest, yTest))

print("以計算出的正確率來說k個數越小，正確率比較高，所以選擇適當的K個數為9。")


print("="*50)