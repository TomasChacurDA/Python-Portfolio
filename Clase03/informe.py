# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:26:12 2024

@author: Tomas
"""
import csv


                                # Ejercicio 3.1: Lista de tuplas


def leer_camion(nombre_archivo):
    
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
    return camion

camion = leer_camion('../Data/camion.csv')


                                # Ejercicio 3.2: Lista de diccionarios

def leer_camion2(nombre_archivo2):
    
    camion2 = []

    with open(nombre_archivo2, 'rt') as f2:
        rows2 = csv.reader(f2)
        headers2 = next(rows2)
        for row in rows2:
            # para cada elemento que hay en cada fila transformalo en diccionario
            lote = {
                    'nombre' : row[0], 
                    'cajones' : int(row[1]), 
                    'precio' : float(row[2])
                    }
            camion2.append(lote)
    return camion2

camion = leer_camion('../Data/camion.csv')

# 'camion' en consola nos devuelva la lista 



                                
                            # Ejercicio 3.3: Diccionarios como contenedores

# A partir del ejercicio 2.7 de la clase 2, creamos un diccionario de ese archivo.

                        
def leer_precios(nombre_archivo3):
    # Inicializa un diccionario vacío para almacenar los precios
    d = {}
    # Abre el archivo especificado en modo de lectura de texto ('rt') con la codificación UTF-8
    with open(nombre_archivo3, 'rt', encoding='utf8') as f3:
        # Crea un objeto csv.reader para leer las filas del archivo
        rows3 = csv.reader(f3)
        # Itera sobre cada fila del archivo
        for row in rows3:
            # Asigna el primer elemento de la fila como clave y el segundo como valor convertido a flotante
            try:
                d[row[0]] = float(row[1])
            except IndexError:
            # En caso de que no haya suficientes elementos en la fila, pasa a la siguiente fila
                continue
        # Devuelve el diccionario con los precios
        return d # Esta línea debe estar fuera del bloque 'with' para que devuelva el diccionario completo


nombre_archivo = '../Data/precios.csv'
diccionario_precios = leer_precios(nombre_archivo)
print(diccionario_precios)


                            # Ejercicio 3.4: Balances

def costo_camion(archivo_camion):
    camion = leer_camion2(archivo_camion)
    costo_total = sum(lote['cajones'] * lote['precio'] for lote in camion)
    return costo_total

def ventas_negocio(archivo_camion, archivo_precios):
    camion = leer_camion2(archivo_camion)
    precios = leer_precios(archivo_precios)
    ingreso_total = sum(lote['cajones'] * precios[lote['nombre']] for lote in camion)
    return ingreso_total

def balance_negocio(archivo_camion, archivo_precios):
    costo = costo_camion(archivo_camion)
    ingresos = ventas_negocio(archivo_camion, archivo_precios)
    balance = ingresos - costo
    return balance

archivo_camion = '../Data/camion.csv'
archivo_precios = '../Data/precios.csv'

balance = balance_negocio(archivo_camion, archivo_precios)

print("Costo del camión:", costo_camion(archivo_camion))
print("Ingresos por ventas:", ventas_negocio(archivo_camion, archivo_precios))
print("Balance:", balance)
if balance > 0:
    print("¡Hubo ganancia!")
else:
    print("Hubo pérdida.")

        
        
        

                

            


