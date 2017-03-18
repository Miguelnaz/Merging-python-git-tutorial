# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
with open('newFile.txt','r+') as file:
    
    file.write("Some new stuff")
    s=str(file.read())
    file.write("\n" +str(s))

    

