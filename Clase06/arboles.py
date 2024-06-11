import csv

# Ejercicio 5.15: Lectura de todos los árboles

def leer_parque(archivo):
    with open(archivo, "rt", encoding= "utf-8") as arboles:
        filascsv = csv.reader(arboles)
        headers = next(filascsv)
        lista = []
        for row in filascsv:
            pares = dict(zip(headers, row))
            lista.append(pares)
    return lista

arboleda = leer_parque("../Data/arbolado.csv")

arboleda


# Ejercicio 5.16: Lista de altos de Jacarandá

H = [float(arbol["altura_tot"]) for arbol in arboleda]

H



# Ejercicio 5.17: Lista de altos y diámetros de Jacarandá

D = [(float(arbol["altura_tot"]), float(arbol["diametro"])) for arbol in arboleda]

D



# Ejercicio 5.18: Diccionario con medidas

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies, arboleda):
    return {especie: [(arbol["altura_tot"], arbol["diametro"]) for arbol in arboleda if arbol["nombre_gen"] == especie] for especie in especies}

medidas_de_especies(especies, arboleda)


# Ejercicio 6.10: Histograma de altos de Jacarandás
import os
import matplotlib.pyplot as plt

def histograma():
    os.path.join('Data', 'arbolado.csv')
    altos = [H]
    plt.hist(altos,bins=35)
    plt.xlabel('Rango de cantidad')
    plt.ylabel('Cantidad')
    plt.title('Histograma de arboles CABA')
    plt.show()
    
histograma()




# Ejercicio 6.11: Scatterplot (diámetro vs alto) de Jacarandás

def scatter_hd(lista_de_pares):
    os.path.join("Data", "arbolado.csv")
    h, d = zip(*lista_de_pares)
    plt.scatter(d,h, alpha=0.05)
    plt.xlabel('Diameter (cm)')
    plt.ylabel('Height (m)')
    plt.title('Scatter plot of tree heights and diameters')
    plt.show()
    
scatter_hd(D)






