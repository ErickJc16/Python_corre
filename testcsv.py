from matplotlib import pyplot as plt
import numpy as np


datos = np.loadtxt("Copia_de_pulso_eco_tanque.csv", usecols=(0,1,2),skiprows=5,delimiter=',')

fig, axes = plt.subplots()

x = np.arange(len(datos[:,1]))

axes.plot(x,datos[:,1])

result = np.array([])


