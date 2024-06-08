
# Ejercicio 5.15: Lectura de todos los árboles

import csv

def leer_parque(archivo):
    with open(archivo, "rt", encoding= "utf-8") as arboles:
        file = csv.reader(arboles)
        headers = next(file)
        empty_list = []
        for row in file:
            pares = dict(zip(headers, row))
            empty_list.append(pares)
    return empty_list

arboleda = leer_parque("../Data/arbolado-en-espacios-verdes.csv")

arboleda


# Ejercicio 5.16: Lista de altos de Jacarandá

height = [float(arbol["altura_tot"]) for arbol in arboleda]

height



# Ejercicio 5.17: Lista de altos y diámetros de Jacarandá

height_diam = [(float(arbol["altura_tot"]), float(arbol["diametro"])) for arbol in arboleda]

height_diam


# Ejercicio 5.18: Diccionario con medidas

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies, arboleda):
    return {especie: [(arbol["altura_tot"], arbol["diametro"]) for arbol in arboleda if arbol["nombre_gen"] == especie] for especie in especies}

medidas_de_especies(especies, arboleda)