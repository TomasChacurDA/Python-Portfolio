'''Volumen de una esfera'''
import math


def calcular_volumen_esfera():
    radio = float(input("Ingrese el radio de la esfera : "))
    resolver_volumen = (4/3) * math.pi * radio**3
    print('El volumen de la esfera es : ',resolver_volumen)
    



calcular_volumen_esfera()