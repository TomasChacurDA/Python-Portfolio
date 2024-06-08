

# Ejercicio 6.2: Generala no necesariamente servida

import random
from collections import Counter

def tirar(cant_dados): # Defino una función para que me genere x cantidad de números aleatorios. 
    tirada = [] # El resultado de la tirada empezará siendo una lista vacía
    for dado in range(cant_dados): # Para cada número del rango de números que le diga...
        tirada.append(random.randint(1, 6)) # ... agregále a la lista vacía x cantidad de números random entre el 1 y el 6
    return tirada # Devolvé el resultado

def es_generala(tirada): # Defino una función que me diga si hace generala
    if max(tirada) == min(tirada) and len(set(tirada)) == 1: # Si el número maximo es igual al minimo y el tamaño de la lista, sin que ningun numero se repita es 1, devuelve TRUE
        return True
    else:
        return False # De lo contrario, devuelve FALSE
    
    
def prob_generala(N): # Ahora defino una funcion que intente hacer generala entre 3 tiros (como en el juego original) en N tiros
    generala = 0 # acá voy a ir contando cuantas generalas hizo en N turnos
    for turno in range(N): # Entonces, para cada turno de N tiros...
        tiros = 1 # aca guardo cuantos tiros lleva
        dados = 5 # la cantiad de dados que se estan jugando
        tirada = tirar(dados) # Llamo a la función que ya había creado para que haga el trabajo de generar numeros random
        dados_a_guardar = []
        while es_generala(tirada) != True and tiros <= 3: # Mientras no sea generala y los tiros sean menores o iguales a 3...
            tiros += 1 # Le sumamos un tiro
            contar = Counter(tirada) # Llamamos a la función counter() para que cuente la tirada
            num_mas_repetido, cantidad = contar.most_common(1)[0] # num_mas_repetido será el número que más veces salió, y cantidad será las veces que apareció
            # IMPORTANTE!!!
            # el código está escrito de esa manera porque contar es la función Counter(tirada), most_common(1) es quien se encarga de mostrarme solo un encabezado con su valor y [0] es para que dentro de lo que consiguió most_common(1) separe los valores y el primero se lo asigne a num_mas_repetidos y el siguiente a cantidad 
            # EJEMPLO: {1: 3, 6: 1, 4: 1} ----most_common(1)---> {1: 3} -------[0]-----> num_mas_repetidos = 1, cantidad = 3
            dados_a_guardar = [num_mas_repetido] * cantidad # Aca le pido que me guarde el numero mas repetido tantas veces
            dados = 5 - cantidad # Y que la proxima jugada sea solamente de los dados que no fueron repetidos
            tirada = tirar(dados) + dados_a_guardar # Acá hago la tirada de los dados que me faltaron, y le sumo a la tirada los otros dados para que los numeros que mas veces salieron los identifique
            
            # Una vez que haya terminado de hacer todas las tiradas en todos los turnos, se fijará cuantas generalas ha hecho
            
        if es_generala(tirada) == True and len(tirada) == 5: # cuenta cuantas generalas hace
            generala += 1
            
    probabilidad_generala = (generala/N) * 100
    print(f"La probabilidad de una generala en {N} turnos es de {probabilidad_generala}%")
    
    
prob_generala(100000)