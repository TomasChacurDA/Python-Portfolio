# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:24:18 2024

@author: Tomas
"""
import csv
#%%
                                    # 3.1 Contenedores
                                    
                                    
# Usamos listas cuando el orden de los datos importa.
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.3),
    ('Limon', 150, 83.44)
]

camion[0]            # ('Pera', 100, 490.1)
camion[2]            # ('Limon', 150, 83.44)                                    

# Crear una lista de tuplas

registros = []  # Empezamos con una lista vacía

# Usamos el .append() para agregar elementos
registros.append(('Pera', 100, 490.10))
registros.append(('Naranja', 50, 91.3))

#%%

                                # Diccionarios como Contenedores

precios = {
   'Pera': 513.25,
   'Limon': 87.22,
   'Naranja': 93.37,
   'Mandarina': 44.12
}
# Podemos buscar claves y valores con precios[elemento que queremos buscar]
# Agregamos elementos llamando al diccionario precios[Clave que queremos agregar] = Valor

#%%

                    # Armar un diccionario a partir del contenido de un archivo.

precios3 = {}  # Empezamos con un diccionario vacío

with open('Data/precios.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        precios3[row[0]] = float(row[1])

#%%
                                    # Claves compuestas

feriados = {
  (1, 1) : 'Año nuevo',
  (1, 5) : 'Día del trabajador',
  (13, 9) : "Día del programador",
}

feriados[(1,5)]

# Las listas, los conjuntos y los diccionarios no pueden ser usados como claves de diccionarios, porque son mutables.




#%%
                                         # Conjuntos
                        
# Un conjunto es una colección de elementos únicos sin orden y sin repetición.
# Los conjuntos eliminan duplicados automaticamente

citricos = set(['Naranja', 'Limon', 'Mandarina'])
# Para agregar datos usamos .add()
citricos.add('Banana')


# A | B                 # Unión de conjuntos A y B
# A & B                 # Intersección de conjuntos
# A - B                 # Diferencia de conjuntos



#%%

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

camion = leer_camion('Data/camion.csv')


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

camion = leer_camion('Data/camion.csv')

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


nombre_archivo = 'Data/precios.csv'
diccionario_precios = leer_precios(nombre_archivo)
print(diccionario_precios)
