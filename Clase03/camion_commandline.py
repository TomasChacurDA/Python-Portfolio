# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:14:33 2024

@author: Tomas
"""

    # Ejercicio 3.11: Ejecución desde la línea de comandos con parámetros
    
#%% 
              
# camion_commandline.py
import csv
import sys


def costo_camion(nombre_archivo):
    # Dejamos el codigo encapsulado en la funcion igual que antes
    with open(nombre_archivo,'rt') as f:
        f = csv.reader(f)
        # Saltamos la primer linea del archivo
        headers = next(f)
        precio_total  = 0
        for line in f:
            try:
                cajones_cant = int(line[1])
                precios = float(line[2])
                precio_total += cajones_cant * precios
            except ValueError:
                continue

        # Le ponemos return para que devuelva el valor
        return precio_total
        
            
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)               















#%% 