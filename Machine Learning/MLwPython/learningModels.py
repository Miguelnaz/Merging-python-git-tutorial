# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:39:52 2017

@author: nazar
"""

import mglearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
cancer=load_breast_cancer()
boston=load_boston()


#Classification model
"""
X,y = mglearn.datasets.make_forge()
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)
clf=KNeighborsClassifier(n_neighbors=7)
clf.fit(X_train,y_train)
clf.predict(X_test)
print("Precision obteined with "+str(clf.n_neighbors)+" neighbors is: "+str(clf.score(X_test,y_test)))
"""
#plt.scatter(X[:,0],X[:,1],c=y, s=60, cmap=mglearn.cm2)
#print("X.shape: %s" % (X.shape,))


#Regresion model
"""
X, y = mglearn.datasets.make_wave(n_samples=40)
plt.plot(X, y, 'o')
plt.plot(X, -3 * np.ones(len(X)), 'o')
plt.ylim(-3.1, 3.1)
"""
X_train,X_test,y_train,y_test=train_test_split(cancer.data,cancer.target,stratify=cancer.target, random_state=66)
training_accuracy=[]
test_accuracy=[]
#try n neighbors from 1 to 10.
neighbors_settings=range(1,11)

for n_neighbors in neighbors_settings:
    #Build the model
    clf=KNeighborsClassifier(n_neighbors=n_neighbors)
    clf.fit(X_train,y_train)
    #Record training set accuracy
    training_accuracy.append(clf.score(X_train,y_train))
    #Record generalization accuracy
    test_accuracy.append(clf.score(X_test,y_test))
    
plt.plot(neighbors_settings, training_accuracy, label="training accuracy")
plt.plot(neighbors_settings, test_accuracy, label="test accuracy")
plt.legend()
    