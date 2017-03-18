# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 09:34:01 2017

@author: nazar
"""
import numpy as np
import pandas as pd

X=[]

#Adding data as a list
for line in open("data_2d.csv"):
    row = line.split(',')
    sample=map(float,row)
    X.append(sample)
#Converting list in a numpy array
X=np.array(X)

#Loading data with pandas

X2=pd.read_csv("data_2d.csv",header=None)

#Show first column

print X2[0]

#Show first and third column (6first rows)
print X2[[0,2]].head(6)

#Show first row

print X2.iloc[0]

print X2.ix[0]

#Show only when first column is lower than five
print X2[X2[0]<5]
