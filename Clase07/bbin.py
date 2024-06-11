#Ejercicio: Búsquedas de un elemento

def busqueda_binaria(lista, e, verbose=False):

    if verbose:
        print(f'[DEBUG] izq | der | medio')
   
    pos = -1
    izq = 0
    der = len(lista)-1

    while izq <= der:
        medio=(izq+der)//2

        if verbose:
            print(f'     Izq: {izq} , Der:{der} , Medio:{medio}')

        if lista[medio]==e:
            pos=medio

        if lista[medio]>e:
            der=medio-1

        else:
            izq=medio+1
    
    return pos

def busqueda_lineal_lordenada(lista, e):
    pos=-1
    for i,num in enumerate(lista):
        if num==e:
            pos=i
            break
        if num>e:
            break
    return pos


def donde_insertar(lista, x):
    izq=0
    der=len(lista)-1
    pos=-1
    while izq <= der:
        medio=(izq + der)//2
        if lista[medio]==x:
            pos=medio
            break
        if lista[medio]>x:
            der=medio-1
        else:
            izq=medio+1
    if pos==-1:
        pos=izq
    return izq




def insertar(lista, x):
    izq=0
    der=len(lista)-1
    pos=-1
    while izq <= der:
        medio=(izq + der)//2
        if lista[medio]==x:
            pos=medio
            break
        if lista[medio]>x:
            der=medio-1
        else:
            izq=medio+1
    
    if pos==-1:
        pos=izq
        lista.insert(pos,x)

    return pos


lista = [1, 2, 3]
print(insertar(lista, 2))  # 1
print(lista)  # [1, 2, 3]
print(insertar(lista, 4))  # 3
print(lista)  # [1, 2, 3, 4]


busqueda_lineal_lordenada([1,2,3,4,5,6,7,8,9],1) 
busqueda_lineal_lordenada([1,2,3,4,5,6,7,8,9],2) 
busqueda_lineal_lordenada([1,2,3,4,5,6,7,8,9],5) 
busqueda_lineal_lordenada([1,2,3,4,5,6,7,8,9],8) 
busqueda_lineal_lordenada([1,2,3,4,5,6,9,10],8)

busqueda_binaria([1, 3, 5], 0, verbose = True)
busqueda_binaria([1, 3, 5], 1, verbose = True)
busqueda_binaria([1, 3, 5], 2, verbose = True)
busqueda_binaria([1, 3, 5], 3, verbose = True)
busqueda_binaria([1, 3, 5], 5, verbose = True)
busqueda_binaria([1, 3, 5], 6, verbose = True)
busqueda_binaria([], 0, verbose = True)
busqueda_binaria([1], 1, verbose = True)
busqueda_binaria([1], 3, verbose = True)
busqueda_binaria([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],18, verbose = True)

donde_insertar([0,2,4,6], 3)
donde_insertar([0,2,4,6,8,10,12,14,16,18,20,22], 17)
donde_insertar([0,2,4,6,7,8,9,10,11,12,13,14,16,17,18,19,20], 15)
donde_insertar([0,2,4,6], 1)
donde_insertar([0,2,4,6], 5)
donde_insertar([0,2,4,5,6], 5)

