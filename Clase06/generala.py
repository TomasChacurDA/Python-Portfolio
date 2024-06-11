# Ejercicio 6.2: Generala no necesariamente servida

import random
from collections import Counter

def tirar(cant_dados):  
    tirada = [] 
    for dado in range(cant_dados): 
        tirada.append(random.randint(1, 6)) 
    return tirada 

def es_generala(tirada): 
    if max(tirada) == min(tirada) and len(set(tirada)) == 1: 
        return True
    else:
        return False 
    
    
def prob_generala(N): 
    generala = 0 
    for turno in range(N): 
        tiros = 1 
        dados = 5 
        tirada = tirar(dados) 
        dados_a_guardar = []
        while es_generala(tirada) != True and tiros <= 3: 
            tiros += 1 
            contar = Counter(tirada) 
            num_mas_repetido, cantidad = contar.most_common(1)[0] 
            
            dados_a_guardar = [num_mas_repetido] * cantidad 
            dados = 5 - cantidad 
            tirada = tirar(dados) + dados_a_guardar 
            
            
            
        if es_generala(tirada) == True and len(tirada) == 5: 
            generala += 1
            
    probabilidad_generala = (generala/N) * 100
    print(f"La probabilidad de una generala en {N} turnos es de {probabilidad_generala}%")
    
    
prob_generala(100000)