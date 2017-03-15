# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 23:34:05 2017

@author: nazar
"""

pyt1=5
type(pyt1)

pyt1="changing variable"

print(type(pyt1))
print(pyt1)

if isinstance(pyt1,str):
    print("it's a string")
    
data = [123,456,789]
for data in data:
    print data
