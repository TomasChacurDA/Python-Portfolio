
# Ejercicio 5.5: Invertir una lista

def inverted_list(lista):
    inverted = []
    for e in lista:
        inverted.insert(0, e)   # Inserta el elemento 'e' al principio de la lista invertida
    return inverted

inverted_list([1, 2, 3, 4, 5])
inverted_list(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
