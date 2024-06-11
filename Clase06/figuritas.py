import numpy as np
import random
# Ejercicio 6.13: Crear

figus_total = 670

crear_album = lambda figus_total: np.zeros(figus_total)


# Ejercicio 6.14: Incompleto

album_incompleto = lambda A: True if np.any(A == 0) else False


# Ejercicio 6.15: Comprar

def comprar_figu(figus_total):
    figu = []
    for i in range(6):
        figu.append(random.randint(0, figus_total - 1))
    return figu



# Ejercicio 6.16: Cantidad de compras


def cuantas_figus(figus_total):
    compradas = 0
    nuevo_album = crear_album(figus_total)
    while album_incompleto(nuevo_album):
        figu = comprar_figu(1)
        nuevo_album[figu] += 1
        compradas += 1
        
    return compradas

comprar_figu(figus_total)


# Ejercicio 6.17

figus_total = 6
n_repeticiones = 1000
compradas = 0

for i in range(n_repeticiones):
    nuevo_album = crear_album(figus_total)
    while album_incompleto(nuevo_album):
        figu = comprar_figu(figus_total)
        nuevo_album[figu] += 1
        compradas += 1
    
promedio = compradas // n_repeticiones

print(promedio)






figus_total = 670
n_repeticiones = 1000
compradas = 0

for i in range(n_repeticiones):
    nuevo_album = crear_album(figus_total)
    while album_incompleto(nuevo_album):
        figu = comprar_figu(figus_total)
        nuevo_album[figu] += 1
        compradas += 1
    
prom = compradas // n_repeticiones

print(prom)

# Ejercicio 6.18

figus_total = 670
n_repeticiones = 100

def experimento_figus(n_repeticiones, figus_total):
    
    album_completo = 0
    
    for i in range(n_repeticiones):
        nuevo_album = crear_album(figus_total)
        figu_prom = 0
        while album_incompleto(nuevo_album) and figu_prom < 800:
            figu = comprar_figu(figus_total)
            figu_prom += 1
            nuevo_album[figu] += 1
            if album_incompleto(nuevo_album) == False:
                album_completo += 1
        
    
    return album_completo

experimento_figus(n_repeticiones, figus_total)