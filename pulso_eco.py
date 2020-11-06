import csv
from matplotlib import pyplot as plt

filename = 'pulso.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #Obteniendo valores  de la primera grafica 
    volts1,volts2,times = [], [],[]

    for row in reader:
        if row[1] == '':
            continue
        
        time1 = float(row[0])
        times.append(time1)

        volt1 = float(row[1])
        volts1.append(volt1)

        volt2 = float(row[2])
        volts2.append(volt2)

    #Graficando informacion
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(times,volts1,c='red')
    plt.plot(times,volts2, c= 'blue')

    #Formateando la grafica
    plt.title("Pulso de Eco", fontsize=20)
    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Volts", fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)

    #print(volts1)
  
    plt.show()
