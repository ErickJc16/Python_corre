#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:54:11 2020

@author: erick
"""

import numpy as np
#from matplotlib import pyplot as plt

def correlacion(x,h):
    
    
    #Arreglo de salida de la correlacion
    rc = np.zeros(h.size + x.size - 1 )
    
    #Señal enviada con zeros al inicio y al final 
    cx = np.insert(x,0,np.zeros(h.size - 1)) #zeros al inicio
    cx = np.insert(cx,cx.size,np.zeros(h.size - 1))#zeros al final 
    
    #Ciclos for para calculo de valores
    for n in np.arange(rc.size):
        for j in np.arange(h.size):
            idcx = j + n
            rc[n]= rc[n] + h[j] * cx[idcx]
            
    return rc

h = np.array([1,5,-8]) #Señal Enviada
x = np.array([3,2,1,6,-7]) #Señal Recibida


print(correlacion(x, h))
print(np.correlate(x,h,'full'))



        


