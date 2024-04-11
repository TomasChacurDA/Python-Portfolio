# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:24:36 2024

@author: Tomas
"""

                            
                        # Ejercicios de errores en el código
#%%                       
                                # Ejercicio 3.5 Semántica
                                
"""def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1
"""


#    El error era indentacion 
#    Lo corregí quitando el else y moviendo el return False fuera del if.
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False
tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
#%%
                                # Ejercicio 3.6: Sintaxis
'''
def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i<n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
'''
#    El error era de Sintaxis  
#    Lo corregímos agregando ':' a la definicion de la funcion, al while y al if.
#    Cambiando el 'Falso' por False.
#    Y por ultimo agregamos un '=' mas al if para que no sea asignacion sino comparacion.   
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%                           
                                   # Ejercicio 3.7: Tipos
'''                                      
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene
'''

                                     


'''
Funcion con error de Tipo porque la función espera una cadena de texto como argumento, 
pero se le proporciona un número entero (int). 
La función len() espera un objeto iterable como una cadena o una lista, 
pero no puede calcular la longitud de un número.
'''
def tiene_uno(expresion):
    if not isinstance(expresion, str):  # Verifica si expresion no es una cadena
        return False  # Si no es una cadena, devuelve False
    n = len(expresion)
    i = 0
    tiene = False
    while (i < n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)  




#%% 

                    # Ejercicio 3.8: Alcances
'''
def suma(a,b):
    c = a + b
    
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
'''

# El error esta en que la funcion no esta devolviendo nada
# Solucionamos esto agregando el return

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")    

#%% 
                            # Ejercicio 3.9: Pisando memoria
              
'''
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
'''    

# El error es que estamos sobreescribiendo una misma posicion dentro del diccionario
# Lo solucionamos moviendo la inicializacion del registro en el bucle for
                     
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)






