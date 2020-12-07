from matplotlib import pyplot as plt
import numpy as np


datos = np.loadtxt("Copia_de_pulso_eco_tanque.csv",usecols=(1,2),skiprows=5,delimiter=',')

h = datos[:,0]

x = datos[:,1]

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


result = np.correlate(x,h,'full')
print(result)
print(len(result))

#result = np.array(correlacion(h, x))

#Graficando informacion
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(result, c= 'red')

plt.show()