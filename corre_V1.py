#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:34:13 2020

@author: erick
"""
import csv
import numpy as np
from matplotlib import pyplot as plt

filename = 'Copia_de_pulso_eco_tanque.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #Obteniendo valores  de la primera grafica 
    volts1,volts2 = [], []

    for row in reader:
        if row[1] == '':
            continue

        volt1 = float(row[1])
        volts1.append(volt1)

        volt2 = float(row[2])
        volts2.append(volt2)
        
    h = np.array(volts1)
        
    x = np.array(volts2)
        
    def correlacion(h,x):
    
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
    
    result = np.array(correlacion(h, x))
    
    #Graficando informacion
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(np.arange(result),result, c= 'red')
    
    #Formateando la grafica
    plt.title("Correlation", fontsize=20)
    plt.xlabel('Samples',fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Value", fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)

    plt.show()
        
        