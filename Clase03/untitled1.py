# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 11:25:18 2024

@author: Tomas
"""

import csv



def costo_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    total = 0.0

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
            try:
                ncajones = int(row[1])
                precio = float(row[2])
                total += ncajones * precio
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return total

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as e:
        archivo = csv.reader(e)
        next(archivo)
        for linea in archivo:
            lote = (linea[0], int(linea[1]), float(linea[2]))
            camion.append(lote)
        return camion
    
    
def leer_camion_listdict(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as j:
        archivo = csv.reader(j)
        encabezados = next(archivo)
        for linea in archivo:
            lote = {
                    encabezados[0] : linea[0],   
                    encabezados[1] : linea[1],
                    encabezados[2] : linea[2]   
                    }
            camion.append(lote)
        return camion

camion = leer_camion_listdict('../Data/camion.csv')
# 3.3

def leer_precios_fruv(nombre_archivo, encoding = 'utf-8'):
        diccionario = {}
        with open(nombre_archivo, 'rt') as o:
            archivo = csv.reader(o)
            for linea in archivo:
                try:
                    nombre = linea[0]
                    precio = float(linea[1])
                    diccionario[nombre] = precio
                except IndexError:
                    continue
            return diccionario

precios = leer_precios_fruv('../Data/precios.csv')


# 3.4

def balance_camion (camion, precios):
    costo_camion= 0.0
    venta_negocio=0.0
    for linea in camion:
        costo_camion += int(linea['cajones']) * float(linea['precio'])  # Convertir a int y float
        precio_fruta = precios[linea['nombre']]
        venta_negocio += int(linea['cajones']) * float(precio_fruta)

    balance = venta_negocio - costo_camion
    return balance

camion = leer_camion_listdict('../Data/camion.csv')
precios= leer_precios_fruv('../Data/precios.csv')
print(balance_camion(camion,precios)) 



        

















