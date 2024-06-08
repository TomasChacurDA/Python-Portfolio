
# Ejercicio 5.3 Búsquedas de un elemento

def devolver(lista, e):
    if e in lista:
        respuesta = lista.index(e)
        
    else:
        respuesta = -1
    return respuesta
    
devolver([2, 4, 6, 4, 9], 4)


# Ejercicio 5.3: Búsquedas de un elemento

def busqueda_u_elemento(lista, e):
    pos = -1
    cantidad = 0
    for i, z in enumerate(lista):
        if z == e:
            pos = i
            cantidad += 1
    return {f"El elemento {e} aparece en la posición {pos}, aparece {cantidad} vez/ces"}
    
busqueda_u_elemento([2, 4, 6, 9, 2, 2, 2, 2, 2, 2], 2)

# Ejercicio 5.4: Búsqueda de máximo y mínimo

def maximo(lista):
    mayor = 0
    for n in lista:
        if n > mayor and n >= 0:
            mayor = n
    return mayor
            
maximo([-8, -5, 6])




            