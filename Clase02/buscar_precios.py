# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:17:16 2024

@author: Tomas
"""
import csv

def buscar_precio(fruta, existe_fruta =True):
    precio = None
    with open('../Data/precios.csv','rt', encoding= 'utf-8') as archivo:
        frutas_csv = csv.reader(archivo)
        for linea in frutas_csv:
            if linea:
                if linea[0] == fruta:
                    precio = float(linea[1])
    
    if existe_fruta:
        if precio != None:
            print(f'El precio de {fruta} es: {precio}')
        else:
            print(f'{fruta} no figura en el listado de precios.')
    return precio
        

