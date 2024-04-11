import os


# ASIGNAMOS una variable para guardar el archivo que queremos
#f1 = open('C:/Users/Tomas/Desktop/Lic Ciencia de Datos/Programacion 1/ejercicios_python/Data/camion.csv', 'rt') #read text = leer texto
# ASIGNAMOS una nueva variable para LEER el archivo
#data = f1.read()
# IMPRIMOMPS el archivo 
#print(data)

# Abrir archivos con funcion with open

# with open('C:/Users/Tomas/Desktop/Lic Ciencia de Datos/Programacion 1/ejercicios_python/Data/camion.csv', 'rt', encoding='utf8') as file:
        #data = file.read()
        
#Escribir archivos con Write
with open('C:/Users/Tomas/Desktop/Lic Ciencia de Datos/Programacion 1/ejercicios_python/Data/camion.csv', 'wt') as out:
    print('Hello World', file=out)












'''
CONSULTAS CLASE

Como hacemos para esta lista poder agregarle la 
nueva fruta con su numero de cajon y precio usando la funcion Write()
f2 = open('C:/Users/Tomas/Desktop/Lic Ciencia de Datos/Programacion 1/ejercicios_python/Data/camion.csv', 'wt')
f2.write('Zanahoria')
print(f2)



que hace maxbytes?
data = f.read([maxbytes])
'''