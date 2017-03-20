# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 22:43:46 2017

@author: nazar
"""

#Decision trees

import mglearn
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix

"""
mglearn.plots.plot_tree_progressive()
plt.suptitle("tree_building");
"""
cancer=load_breast_cancer()
X_train,X_test,y_train,y_test=train_test_split(
        cancer.data,cancer.target, random_state=0)
tree=DecisionTreeClassifier(max_depth=4,random_state=0) #maz_depth fixes the number os if for the tree
tree.fit(X_train,y_train)


print("accuracy on training set: %f" % tree.score(X_train, y_train))
print("accuracy on test set: %f" % tree.score(X_test, y_test))

pred=tree.predict(X_test)

confusion=confusion_matrix(y_test,pred)
print(confusion)

from sklearn.ensemble import RandomForestClassifier

forest=RandomForestClassifier(n_estimators=100,random_state=0)
forest.fit(X_train,y_train)

print("accuracy on training set: %f" % forest.score(X_train, y_train))
print("accuracy on test set: %f" % forest.score(X_test, y_test))
pred=forest.predict(X_test)

confusion=confusion_matrix(y_test,pred)
print(confusion)

from sklearn.ensemble import GradientBoostingClassifier

gbrt = GradientBoostingClassifier(random_state=0, max_depth=2)
gbrt.fit(X_train, y_train)
print("accuracy on training set: %f" % gbrt.score(X_train, y_train))
print("accuracy on test set: %f" % gbrt.score(X_test, y_test))

pred=gbrt.predict(X_test)

confusion=confusion_matrix(y_test,pred)
print(confusion)