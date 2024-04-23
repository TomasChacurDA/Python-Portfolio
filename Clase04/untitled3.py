# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 13:07:44 2024

@author: Tomas
"""

import csv

def costo_camion(nombre_archivo):
    
    with open(nombre_archivo, 'rt', encoding = 'utf-8') as f:
        costo_total = 0
        archivo = csv.reader(f)
        encabezados = next(archivo)
        for n_fila, fila in enumerate(archivo, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        return costo_total
 

# 4.4 
# Copio las funciones de informe.py
# 

def leer_precios(nombre_archivo1):
    d = {}
    with open(nombre_archivo1, 'rt', encoding='utf8') as f3:
        rows3 = csv.reader(f3)
        for row in rows3:
            try:
                d[row[0]] = float(row[1])
            except IndexError:
                continue
        return d 


def leer_camion(nombre_archivo):
    
    camion = []

    with open(nombre_archivo, 'rt') as f:
        file = csv.reader(f)
        headers = next(file)
        for n_row, row in enumerate(file):
            lote = dict(zip(headers, row))
            camion.append(lote)
    return camion

camion = leer_camion('../Data/fecha_camion.csv')
precios = leer_precios('../Data/precios.csv')



# Calcular :
    # Costo del camión 
    # Recaudacion de la venta
    # La diferencia

def resultado_mercado(camion, precios):
    costo_camion = 0
    for i in camion:
        cajones = int(i['cajones'])
        precio_producto = float(i['precio'])
        costo_camion += cajones *  precio_producto
    suma_ventas = 0
    for valor in precios.values():
        suma_ventas += valor 
    diferencia = costo_camion - suma_ventas
    return print(f'El camion costo : {costo_camion} \nRecaudacion de la venta : {suma_ventas} \nDiferencia : {diferencia}')

# Mofico la funcion para que use el metodo zip() y use los encabezados.

archivo_camion = '../Data/camion.csv'
archivo_precio = '../Data/precios.csv'


# Multiplicar cajon por precio









     
    