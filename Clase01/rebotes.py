'''
Ejercicio

Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que 
toca el piso salta 3/5 de la altura desde la que cayó. Escribí un programa 
rebotes.py que imprima una tabla mostrando las alturas que alcanza en cada uno 
de sus primeros diez rebotes.
'''

def altura_alcanzada(altura_inicial):
    for i in range(1,11):
        altura_inicial = (altura_inicial * 3) / 5
        print('Rebote ', i, ' Altura alcanzada : ', altura_inicial)
        i = i + 1
        
altura_alcanzada(100)
       
        

   


    
    
    






