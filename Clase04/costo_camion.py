# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:29:40 2024

@author: Tomas
"""
import csv
       

def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        costo_total = 0
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return costo_total
    
print(costo_camion('Data/camion.csv'))
