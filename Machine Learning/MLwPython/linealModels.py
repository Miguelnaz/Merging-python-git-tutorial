# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 15:41:07 2017

@author: nazar
"""
import mglearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
"""
cancer=load_breast_cancer()
boston=load_boston()

#Linear models

X,y = mglearn.datasets.load_extended_boston()
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)
ridge=Ridge().fit(X_train,y_train)
lr=LinearRegression().fit(X_train,y_train)
lasso=Lasso().fit(X_train,y_train)

print("training lr set score: %f" % lr.score(X_train, y_train))
print("test lr set score: %f" % lr.score(X_test, y_test))
print("training ridge set score: %f" % ridge.score(X_train,y_train))
print("test set ridge score: %f" % ridge.score(X_test,y_test))

ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)
print("training set score with alpa=0.1: %f" % ridge01.score(X_train, y_train))
print("test set score: %f" % ridge01.score(X_test, y_test))

print("training Lasso set score: %f" % lasso.score(X_train, y_train))
print("test set Lasso score: %f" % lasso.score(X_test, y_test))
print("number of features used: %d" % np.sum(lasso.coef_ != 0))

lasso001 = Lasso(alpha=0.01).fit(X_train, y_train)
print("training set alpha=0.01 score: %f" % lasso001.score(X_train, y_train))
print("test set score: %f" % lasso001.score(X_test, y_test))
print("number of features used: %d" % np.sum(lasso001.coef_ != 0))

lasso00001 = Lasso(alpha=0.0001).fit(X_train, y_train)
print("training set alpha 0.0001 score: %f" % lasso00001.score(X_train, y_train))
print("test set score: %f" % lasso00001.score(X_test, y_test))
print("number of features used: %d" % np.sum(lasso00001.coef_ != 0))

#Linear models for Classification
print("From now it's all lineal classificator")
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

X_train,X_test,y_train,y_test=train_test_split(cancer.data,cancer.target,stratify=cancer.target, random_state=42)
logisticregression=LogisticRegression().fit(X_train,y_train)
print("training logisticregression set score: %f" % logisticregression.score(X_train, y_train))
print("test set score: %f" % logisticregression.score(X_test, y_test))

logisticregression100 = LogisticRegression(C=100).fit(X_train, y_train)
print("training with c= 100 set score: %f" % logisticregression100.score(X_train, y_train))
print("test set score: %f" % logisticregression100.score(X_test, y_test))

logisticregression001 = LogisticRegression(C=0.01).fit(X_train, y_train)
print("training set with c= 0.01 score: %f" % logisticregression001.score(X_train, y_train))
print("test set score: %f" % logisticregression001.score(X_test, y_test))

plt.plot(logisticregression.coef_.T, 'o', label="C=1")
plt.plot(logisticregression100.coef_.T, 'o', label="C=100")
plt.plot(logisticregression001.coef_.T, 'o', label="C=0.001")
plt.xticks(range(cancer.data.shape[1]), cancer.feature_names, rotation=90)
plt.ylim(-5, 5)
plt.legend()

for C in [0.001, 1, 100]:
 lr_l1 = LogisticRegression(C=C, penalty="l1").fit(X_train, y_train)
 print("training accuracy of L1 logreg with C=%f: %f"
 % (C, lr_l1.score(X_train, y_train)))
 print("test accuracy of L1 logreg with C=%f: %f"
 % (C, lr_l1.score(X_test, y_test)))
 plt.plot(lr_l1.coef_.T, 'o', label="C=%f" % C)
plt.xticks(range(cancer.data.shape[1]), cancer.feature_names, rotation=90)
plt.ylim(-5, 5)
plt.legend(loc=2)
"""

#Multiclass classification
"""
from sklearn.datasets import make_blobs
X, y = make_blobs(random_state=42)
plt.scatter(X[:, 0], X[:, 1], c=y, s=60, cmap=mglearn.cm3)
"""
from sklearn.datasets import make_blobs
from sklearn.svm import LinearSVC
X, y = make_blobs(random_state=42)
linear_svm = LinearSVC().fit(X, y)
print(linear_svm.coef_.shape)
print(linear_svm.intercept_.shape)
"""
plt.scatter(X[:, 0], X[:, 1], c=y, s=60, cmap=mglearn.cm3)
line = np.linspace(-15, 15)
for coef, intercept in zip(linear_svm.coef_, linear_svm.intercept_):
    plt.plot(line, -(line * coef[0] + intercept) / coef[1])
plt.ylim(-10, 15)
plt.xlim(-10, 8)
"""
mglearn.plots.plot_2d_classification(linear_svm, X, fill=True, alpha=.7)
plt.scatter(X[:, 0], X[:, 1], c=y, s=60)
line = np.linspace(-15, 15)
for coef, intercept in zip(linear_svm.coef_, linear_svm.intercept_):
    plt.plot(line, -(line * coef[0] + intercept) / coef[1])