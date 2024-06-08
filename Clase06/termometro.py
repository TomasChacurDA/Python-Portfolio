

import random

def medir_temp(n):
    temperatura = []
    for i in range(n):
        variante = random.normalvariate(0, 0.2)
        variante = round(variante, 2) + 37.5
        temperatura.append(variante)
    orden = sorted(temperatura)
    minimo = min(orden)
    maximo = max(orden)
    promedio = sum(orden) / len(orden)
    promedio = round(promedio, 2)
    if n % 2 == 0:
        mediana = (orden[n//2 - 1] + orden[n//2]) / 2
        mediana = round(mediana, 2)
    else:
        mediana = orden[n/2]
        mediana = round(mediana, 2)
    
    return (maximo, minimo, promedio, mediana)

medir_temp(6)

    
    