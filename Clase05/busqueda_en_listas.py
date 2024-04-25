# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:48:28 2024

@author: Tomas
"""

#                       Ejercicio 5.3: Búsquedas de un elemento


l = [1,2,3,4,5,6,7,8,9]

def buscar_posicion_elemento(lista, e):
    pos = -1
    for indice, elemento in enumerate(lista):
        if elemento == e:
            pos = indice
            break
    return pos



l2 = [1,1,2,2,2,3,3,4,4,4,4,5,5,5,6,6,7,7,7,7,7,8,8,9,9,9]
def buscar_n_elemento(lista, e):
     for x in lista:
         x = lista.count(e)
     return x
    
 #                  Ejercicio 5.4: Búsqueda de máximo y mínimo   

l3 = [10,40,14,100,23,69,33]

def maximo(lista): 
    m = 0 
    for e in lista:
         if e > m:
             m = e
             
    return m
maximo(l3)











