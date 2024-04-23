# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:22:03 2024

@author: Tomas
"""
import csv
from collections import Counter
from pprint import pprint

#           Ejercicio 4.13: Lectura de los árboles de un parque

def leer_parque(nombre_archivo, parque):
    listado_arboles = []
    with open(nombre_archivo, 'rt', encoding = 'utf-8') as f:
        archivo = csv.reader(f)
        encabezados = next(archivo)
        for linea in archivo:
            enzipado = dict(zip(encabezados, linea))
            if enzipado['espacio_ve'] == parque:
                listado_arboles.append(enzipado)
                
    return listado_arboles

leer_p = leer_parque('../Data/arbolado-en-espacios-verdes.csv', "GENERAL PAZ" )

pprint(leer_p)


#           Ejercicio 4.14: Determinar las especies en un parque

def especies(lista_arboles):
    nombre_especie = set()
    for arbol in lista_arboles :
        nombre_especie.add(arbol['nombre_com'])
    return nombre_especie

especies_general_paz = especies(leer_p)


#               Ejercicio 4.15: Contar ejemplares por especie

def contar_ejemplares(lista_arboles):
    contador = Counter()
    for arbol in lista_arboles:
        contador[arbol['nombre_com']] += 1
    return contador

contador_ejemplares = contar_ejemplares(leer_p)
print(contador_ejemplares)

def especies_mas_comunes_por_parque(nombre_archivo, parques):
    for parque in parques:
        lista_arboles = leer_parque(nombre_archivo, parque)
        contador_ejemplares = contar_ejemplares(lista_arboles)
        print("Parque:", parque)
        print("Especies más comunes:")
        for especie, cantidad in contador_ejemplares.most_common(5):
            print(f"{especie}: {cantidad}")
        print()

parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'

especies_mas_comunes_por_parque(nombre_archivo, parques)

#               Ejercicio 4.16: Alturas de una especie en una lista

def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alturas.append(float(arbol['altura_tot']))
    return alturas

def calcular_alturas_promedio_maxima(lista_arboles, especie, parques):
    resultados = {}
    for parque in parques:
        alturas = obtener_alturas(lista_arboles[parque], especie)
        max_height = max(alturas)
        promedio = sum(alturas) / len(alturas)
        resultados[parque] = {'max': max_height, 'prom': promedio}
    return resultados


parques_data = {
    'GENERAL PAZ': leer_parque(nombre_archivo, 'GENERAL PAZ'),
    'ANDES, LOS': leer_parque(nombre_archivo, 'ANDES, LOS'),
    'CENTENARIO': leer_parque(nombre_archivo, 'CENTENARIO')
}


alturas_jacarandas = calcular_alturas_promedio_maxima(parques_data, 'Jacarandá', parques)
print("Resultados de alturas de Jacarandás en tres parques:")
print("Medida\tGeneral Paz\tLos Andes\tCentenario")
for medida in ['max', 'prom']:
    print(f"{medida}\t{alturas_jacarandas['GENERAL PAZ'][medida]}\t\t{alturas_jacarandas['ANDES, LOS'][medida]}\t\t{alturas_jacarandas['CENTENARIO'][medida]}")


#           Ejercicio 4.17: Inclinaciones por especie de una lista

def especimen_mas_inclinado(lista_arboles, parques):
    inclinaciones_maximas = {}
    for parque in parques:
        inclinaciones = obtener_inclinaciones(lista_arboles[parque], 'Falso Guayabo')
        if inclinaciones:
            max_inclinacion = max(inclinaciones)
            inclinaciones_maximas[parque] = {'especie': 'Falso Guayabo', 'inclinacion': max_inclinacion}
        else:
            inclinaciones_maximas[parque] = {'especie': 'Falso Guayabo', 'inclinacion': None}
    return inclinaciones_maximas


mas_inclinado = especimen_mas_inclinado(parques_data, parques)
for parque, info in mas_inclinado.items():
    if info['inclinacion'] is not None:
        print(f"En el Parque {parque} hay un {info['especie']} inclinado {info['inclinacion']} grados.")
    else:
        print(f"No se encontraron ejemplares de {info['especie']} en el Parque {parque}.")

#               Ejercicio 4.18: Especie con el ejemplar más inclinado


def especie_promedio_mas_inclinada(lista_arboles, parques):
    promedios_inclinaciones = {}
    for parque in parques:
        inclinaciones = obtener_inclinaciones(lista_arboles[parque], 'Álamo plateado')
        if inclinaciones:
            promedio = sum(inclinaciones) / len(inclinaciones)
            promedios_inclinaciones[parque] = {'especie': 'Álamo plateado', 'promedio': promedio}
        else:
            promedios_inclinaciones[parque] = {'especie': 'Álamo plateado', 'promedio': None}
    return promedios_inclinaciones


promedio_mas_inclinado = especie_promedio_mas_inclinada(parques_data, parques)
for parque, info in promedio_mas_inclinado.items():
    if info['promedio'] is not None:
        print(f"En el Parque {parque} los {info['especie']} tienen un promedio de inclinación de {info['promedio']} grados.")
    else:
        print(f"No se encontraron ejemplares de {info['especie']} en el Parque {parque}.")

#                   Ejercicio 4.19: Especie más inclinada en promedio


def especie_promedio_mas_inclinada(lista_arboles, parques):
    especies_inclinaciones = {}
    
    
    for parque in parques:
        for arbol in lista_arboles[parque]:
            especie = arbol['nombre_com']
            inclinacion = float(arbol['inclinacio'])
            if especie in especies_inclinaciones:
                especies_inclinaciones[especie].append(inclinacion)
            else:
                especies_inclinaciones[especie] = [inclinacion]
    
    
    promedios_inclinaciones = {}
    for especie, inclinaciones in especies_inclinaciones.items():
        promedio = sum(inclinaciones) / len(inclinaciones)
        promedios_inclinaciones[especie] = promedio
    
    
    especie_max_inclinacion = max(promedios_inclinaciones, key=promedios_inclinaciones.get)
    inclinacion_max_promedio = promedios_inclinaciones[especie_max_inclinacion]
    
    return especie_max_inclinacion, inclinacion_max_promedio


especie, promedio = especie_promedio_mas_inclinada(parques_data, parques)

print(f"La especie con el promedio más alto de inclinación es {especie} con un promedio de {promedio} grados.")









