# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 12:31:39 2017

@author: nazar
"""

#functions and inputs

def potatoPrice(potatoType,amount):
    cost=None
    if potatoType==1:
        cost=0.1
        
    if potatoType==2:
        cost=0.12
        
    if potatoType==3:
        cost=0.15
    return(cost*amount)
        
    



potatoType=int(raw_input("Introduce the type (1,2 or 3) of potato that you want to buy: "))
amount=int(raw_input("Introduce de amount of potatoes that you want to buy: "))

price=potatoPrice(potatoType,amount)

print("Your pourchase cost is "+str(price)+" euros.")