#Algoritmo de correlacion sin utilizar Numpy 

def zeros(z):
    zeros_list = [0] * (z - 1)
    return zeros_list

def correlacion(x,h):
    
    #Arreglo de salida de la correlacion
    rc = zeros(len(x) + len(h))

    #Señal enviada con ceros agregados al inicio y al final
    cx = zeros(len(h))
    cx.extend(x)
    cx.extend(zeros(len(h)))

    #Ciclo for para calculo de valores
    for n in range(len(rc)):
        for j in range(len(h)):
            idcx = n + j
            rc[n] = rc[n] + h[j] * cx[idcx]

    return rc 

h = [1,5,-8]

x = [3,2,1,6,-7]

result = correlacion(x,h)


