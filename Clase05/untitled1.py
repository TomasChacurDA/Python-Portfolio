# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:08:45 2024

@author: Tomas
"""
import csv
import sys

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
    print(sys.argv[1])
    print(sys.argv)
    
else:
    nombre_archivo = '../Data/users_foro.csv'

def leer_users(archivo):
    lista = []
    with open(archivo, 'rt', encoding = 'utf-8') as f:
        archivocsv = csv.reader(f)
        encabezados = next(archivocsv)
        for linea in archivocsv:
            diccionario = dict(zip(encabezados,linea))
            lista.append(diccionario)
        return lista
leer = leer_users('../Data/users_foro.csv')

def users_reportados(lista_users):
    lista = []
    for diccionario in lista_users:
        if diccionario['reportade'] == 'SI':
            lista.append(diccionario)
    return lista

users_reportados(leer)

def obtener_dominios(lista_users):
    correos = set()
    for diccionario in lista_users:
        correos.add(diccionario['email'])
    return correos

dominios = obtener_dominios(leer)

print(dominios)