import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum() 


N = 100000
trayectorias = [randomwalk(N) for i in range(12)]


def encontrar_max_alejamiento(trayectorias):
    max_alejamiento = trayectorias[0]
    max_distancia = max(abs(max_alejamiento))

    for tray in trayectorias:
        distancia = max(abs(tray))
        if distancia > max_distancia:
            max_alejamiento = tray
            max_distancia = distancia
    return max_alejamiento


def encontrar_min_alejamiento(trayectorias):
    
    min_alejamiento = trayectorias[0]
    min_distancia = max(abs(min_alejamiento))
    for tray in trayectorias:
        distancia = max(abs(tray))
        if distancia < min_distancia:
            min_alejamiento = tray
            min_distancia = distancia
    return min_alejamiento


max_alejamiento = encontrar_max_alejamiento(trayectorias)
min_alejamiento = encontrar_min_alejamiento(trayectorias)

fig = plt.figure(figsize=(10, 8))  


plt.subplot(2, 1, 1)
for tray in trayectorias:
    plt.plot(tray)
plt.title('12 Caminatas al Azar')
plt.xlabel('Tiempo')
plt.ylabel('Distancia al Origen')


plt.subplot(3, 3, 7)
plt.plot(max_alejamiento)
plt.title('Mayor Alejamiento')
plt.xlabel('Tiempo')
plt.ylabel('Distancia al Origen')


plt.subplot(3, 3, 9)
plt.plot(min_alejamiento)
plt.title('Menor Alejamiento')
plt.xlabel('Tiempo')
plt.ylabel('Distancia al Origen')

plt.tight_layout()  
plt.show()