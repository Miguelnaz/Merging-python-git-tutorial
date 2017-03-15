# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 15:23:57 2017

@author: nazar
"""

#list, set, dictionary

fileSet={2015,2017,2019}
fileList=[2015,2017,2017]

#In Sets, you can't have repetitive items

fileList=set(fileList)

print(fileList)
print("\n fileList is initialized with \n 2015,2017,2017 valor but \n remove the second 2017")

#Dictionary with key-value items
fileDict={"last year":2016,"this year":2017,"next year":2018}

print(fileDict)
print("\n")
print(fileDict["this year"])