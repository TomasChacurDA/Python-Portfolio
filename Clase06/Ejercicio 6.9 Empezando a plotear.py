
import numpy as np
import matplotlib.pyplot as plt

def plotear_temperaturas():
        temperaturas = np.load('temperaturas.npy')
        temperaturas = temperaturas.flatten()
        plt.hist(temperaturas, bins=25)
        plt.xlabel('Temperatura (°C)')
        plt.ylabel('Frecuencia')
        plt.title('Histograma de Temperaturas Simuladas')
        plt.show()


plotear_temperaturas()
