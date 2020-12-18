"""
Codigo para leer archivos sin el modulo csv 

"""
from matplotlib import pyplot as plt

filename = "pulso.csv"

with open(filename) as archivo:

    señal_enviada = []
    señal_recibida = []
    for linea in archivo:
        datos = linea.split(',')
        señal_enviada.append(datos[1])
        señal_recibida.append(datos[2])

    señal_enviada.pop(0)
    señal_recibida.pop(0)

    for i in range(len(señal_enviada)):
        señal_enviada[i] = float(señal_enviada[i])
        señal_recibida[i] = float(señal_recibida[i])

    def zeros(z):
        zeros_list = [0] * (z - 1)
        return zeros_list

    def correlacion(x,h):
        #Arreglo de salida de la correlacion
        rc = zeros(len(x) + len(h))

        #Señal enviada con ceros agregado al inicio y al final
        cx = zeros(len(h))
        cx.extend(x)
        cx.extend(zeros(len(h)))

        #Ciclo for para calcular valores
        for n in range(len(rc)):
            for j in range(len(h)):
                idcx = n + j
                rc[n] = rc[n] + h[j] + cx[idcx]
        
        return rc
    
    result = correlacion(señal_recibida,señal_enviada)
    
    #Graficando informacion
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(range(result),result, c= 'red')
    
    #Formateando la grafica
    plt.title("Correlation", fontsize=20)
    plt.xlabel('Samples',fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Value", fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)

    plt.show()


