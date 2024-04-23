# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 12:46:35 2024

@author: Tomas
"""

import sys



def altura_alcanzada(altura_inicial):
    param1 = int(sys.argv[1])
    for i in range(1,11):
        altura_inicial = (altura_inicial * 3) / 5
        print('Rebote ', i, ' Altura alcanzada : ', altura_inicial)
        i = i + 1
    return altura_alcanzada(param1)    

       