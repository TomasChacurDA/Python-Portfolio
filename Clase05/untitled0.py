# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:21:13 2024

@author: Tomas
"""

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

rta = tiene_a ('palabra')
print(rta)

# ¿Es correcto esto? ¿Donde está el error? ¿Cómo lo podemos resolver?
    # El error es que el 'if' debe ser if expresion[i] tiene 'a' devolve true