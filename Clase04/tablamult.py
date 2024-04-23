# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:36:59 2024

@author: Tomas
"""

#                       Ejercicio 4.12: Tablas de multiplicar



def tabla_multiplicar():
    
    print(f"{'':4}", end="")
    for i in range(10):
        print(f"{i:4}", end="")
    print("\n---------------------------------------------")

    
    for i in range(10):
        print(f"{i:2}: ", end="")
        for j in range(10):
            
            producto = 0
            for k in range(j):
                producto += i
            print(f"{producto:4}", end="")
        print()

if __name__ == "__main__":
    tabla_multiplicar()
            
    






