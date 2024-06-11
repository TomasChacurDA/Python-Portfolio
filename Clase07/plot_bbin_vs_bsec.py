

def busqueda_secuencial(lista, x):
    
    pos = -1
    for i,z in enumerate(lista):
        if z == x:
            pos = i
            break
    return pos


def busqueda_secuencial_comps(lista, x):
    
    comps = 0 
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 
        if z == x:
            pos = i
            break
    return pos, comps


lista=[0,1,2,3,5,6,8,9,11,13,15,16,17,18,21,23,26,27]
busqueda_secuencial_comps(lista, 23)



def busqueda_binaria_comps(lista, e, verbose=False):

    if verbose:
        print(f'[DEBUG] izq | der | medio')
    
    comps=0
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

        comps+=1
    
    return pos, comps


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
busqueda_binaria_comps(lista, 5)

busqueda_binaria_comps(lista, 6)


import random

def generar_lista(n, m):
    
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    
    return random.randint(0, m-1)



m = 10000
n = 100
lista = generar_lista(n, m)

x = generar_elemento(m)


comps = busqueda_secuencial_comps(lista, x)[1]


k=1000

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_comps(lista,x)[1]

    comps_prom = comps_tot / k

    return comps_prom

experimento_secuencial_promedio(lista,m,k)


import matplotlib.pyplot as plt
import numpy as np

m = 10000
k = 1000

largos = np.arange(256) + 1 
comps_promedio_secuencial = np.zeros(256)  

for i, n in enumerate(largos):
    lista = generar_lista(n, m) 
    comps_promedio_secuencial[i] = experimento_secuencial_promedio(lista, m, k)


plt.plot(largos,comps_promedio_secuencial,label = 'Secuential Search')
plt.xlabel("List Lenght")
plt.ylabel("Comp Count")
plt.title("Search Complexity")
plt.legend()
plt.show()


def experimento_binario_promedio(lista, m, k):
    
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria_comps(lista, x)[1]

    comps_prom = comps_tot / k

    return comps_prom

comps_promedio_binario = np.zeros(256)


for i, n in enumerate(largos):
    lista = generar_lista(n, m)
    comps_promedio_secuencial[i] = experimento_secuencial_promedio(lista, m, k)
    comps_promedio_binario[i] = experimento_binario_promedio(lista, m, k)



plt.figure(figsize=(10, 6))
plt.plot(largos, comps_promedio_secuencial, label='Secuential Search', color='blue')
plt.plot(largos, comps_promedio_binario, label='Binary Search', color='red')
plt.xlabel("List Lenght")
plt.ylabel("Comp Count")
plt.title("Secuential & Binary Search Com Count")
plt.legend()


plt.xlim(0, 256)
plt.ylim(0, max(comps_promedio_secuencial))
plt.show()




def graficar_bbin_vs_bseq(m, k):

    largos = np.arange(256) + 1 
    comps_promedio_bbin = np.zeros(256) 
    comps_promedio_bseq = np.zeros(256)
    
    for i, n in enumerate(largos):
        
        lista = generar_lista(n, m) 
        comps_promedio_bbin[i] = experimento_binario_promedio(lista, m, k)
        comps_promedio_bseq[i] = experimento_secuencial_promedio(lista, m, k)
        
    
   
    plt.plot(largos, comps_promedio_bbin, label='Binary Search')
    plt.plot(largos, comps_promedio_bseq, label='Secuential Search')
    plt.xlabel('List Lenght')
    plt.ylabel('Comp Count')
    plt.title('Secuential & Binary Search Com Count')
    plt.legend()
    plt.show()


graficar_bbin_vs_bseq(1000, 100)
graficar_bbin_vs_bseq(10000, 1000)
graficar_bbin_vs_bseq(10000, 500)
graficar_bbin_vs_bseq(100000, 10000)











