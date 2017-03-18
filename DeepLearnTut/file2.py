# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 18:40:47 2017

@author: nazar
"""

import pandas as pd

df=pd.read_csv("international-airline-passengers.csv",engine="python",skipfooter=3)

df.columns #Show column names or information

df.columns=["month","passengers"] #Reasigns column names

df['passengers'] #Return the columns "passengers"
df.passengers #The same

df['ones']=1 #Add a column whose valor is 1

print df.head(6)