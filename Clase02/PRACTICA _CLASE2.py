#%%
                                # Ejercicio 2.1 Clase 2


#with open('../Data/camion.csv', 'rt') as f:
        #for line in f:
            # 'end = ' Lo que escribamos dentro de las comillas se agrega
            # Adelante de cada salto de linea.
           # print(line, end = '') 
#-----------------------------------

# Para saltear lineas usamos 'next()' 
# Si no la usamos en un bucle for para cargar una linea especifica que queramos quitar
# Va a quitar la linea en la posicion 0

f1 = open('../Data/camion.csv', 'rt')
# Cargamos el archivo en una nueva variable que imprime la primera linea.
headers = next(f1)
# Usamos 'headers' en la consola para ver el resultado.
# Hacemos de cada linea una lista
for line in f1:
        # separamos a cada elemento de cada fila (row) con ','
    fila1 = line.split(',')
    print(fila1)
#%%        
                            # Ejercicio 2.2 Lectura de un archivo de datos

with open('../Data/camion.csv', 'rt') as f3:
    # Saltamos la primer linea del archivo
    headers = next(f3)
    precio_total  = 0
    for line in f3:
        row = line.split(',')
        cajones_cant = int(row[1])
        precios = float(row[2])
        precio_total += cajones_cant * precios
    
    print(precio_total)
#%%    
                            # Ejercicio 2.3 Precio de la naranja
                            

with open('../Data/precios.csv', 'rt') as f4:
    for linea in f4:
        # Quitamos los espacios y Separamos en listas y elementos.
        filas = linea.strip().split(',')
        # Si encuentra una lista vacia, continua iterando sin hacer nada a esa misma lista vacia
        if filas == ['']:
            continue
        precio_fruta = float(filas[1])
        if filas[0] == 'Naranja':
            print('El precio de la Naranja es de : ',precio_fruta)
         

    
#%%
                           # Ejercicio 2.4: Archivos comprimidos
                           
# Para leer archivos comprimidos podemos usar la siguiente libreria
import gzip
# Probar en consola
with gzip.open('../Data/camion.csv.gz', 'rt') as f:
    for line in f:
        print(line, end = '')
#%%
#%%
                                     # Funciones
                               # Ejemplos de try & except                                       
                               
try:
    s = input('Ingresa un numero :')
    n = int(s)
    print(f'su inversa es {1/n:.3f}')
    # Si hay un error de valores va a responder que el usuario no ingreso un numero enteros
except ValueError:
    print('Error, no ingresaste un numero entero.')
except ZeroDivisionError:
    print('Error, no se puede dividir por 0.')

#%%
                                # Una mejor manera de hacerlo
s = input('Ingresa un numero :')
if s.isnumeric():
    n = int(s)
    if n != 0:
        print(f'su inversa es {1/n:.3f}')
    else:
        print('Error, no se puede dividir por 0.')      
else:
    print('Error, no ingresaste un numero entero.')

#%%

# Si no indicamos delante de except el error, va a captar todos los errores por defecto.

numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
        # No especificamos que error queremos exceptuar porque con except solo atrapa todos
    except:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')

#%%
                          # Ejercicio 2.6 Transformar un script en una función

# Definimos la funcion y le damos el parametro para buscar archivo
def costo_camion(nombre_archivo):
    # Dejamos el codigo encapsulado en la funcion igual que antes
    with open(nombre_archivo,'rt') as f3:
        # Saltamos la primer linea del archivo
        headers = next(f3)
        precio_total  = 0
        for line in f3:
            row = line.split(',')
            cajones_cant = int(row[1])
            precios = float(row[2])
            precio_total += cajones_cant * precios
        # Le ponemos return para que devuelva el valor
        return precio_total
# Creamos una variable para poder llamar al archivo y que haga la cuenta con la funcion
costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
 
#%%       
                                        # Ejercicio 2.7: Buscar precios
                                        
def buscar_precio(fruta):
    with open('../Data/precios.csv', 'rt') as f4:
        for linea in f4:
            # Quitamos los espacios y Separamos en listas y elementos.
            filas = linea.strip().split(',')
            # Si encuentra una lista vacia, continua iterando sin hacer nada a esa misma lista vacia
            if filas == ['']:
                continue
            precio_fruta = float(filas[1])
            if filas[0] == fruta:
                return(fruta, precio_fruta)
                
                
        

    

#%%
    
def buscar_fruta(fruta2):
    with open('../Data/precios.csv', 'rt') as f5:
        for linea2 in f5:
            filas2 = linea2.split(',')
            if filas2 == ['']:
                continue
            precio_fruta2 = float(filas2[1])
            if filas2[0] == fruta2:
                return(print('El precio de ', fruta2, 'es de ',precio_fruta2))
            else:
                return(print('La fruta elegida no esta disponible.'))
            
#%%       
                            # Ejercicio 2.8: Administración de errores

def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad


    
#%%
# Exceptuamos el error ValueError y continua pidiendo la edad de cada nombre en la lista.
for nombre in ['Pedro','Juan','Caballero', 'Pepito']:
    try:
        edad = preguntar_edad(nombre)
        print(f'{nombre} tiene {edad} años.')
    except ValueError:
        print(f'{nombre} no ingresó una edad válida.')        


#%%
                                     # Ejercicio 2.8: Administración de errores      
        
def preguntar_edad2(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad    
#%%    

for nombre in ['Pedro','Juan','Caballero']:
    try:
        edad = preguntar_edad(nombre)
        print(f'{nombre} tiene {edad} años.')
    except ValueError:
        print(f'{nombre} no ingresó una edad válida.')  
#%%                                     # 2.8 Costo Camion Try & Except


def costo_camion2(nombre_archivo):
    # Dejamos el codigo encapsulado en la funcion igual que antes
    with open(nombre_archivo,'rt') as f3:
        # Saltamos la primer linea del archivo
        headers = next(f3)
        precio_total  = 0
        for line in f3:
            row = line.split(',')
            try:
                cajones_cant = int(row[1])
            except ValueError:
                print('Warning')
            continue
            precios = float(row[2])
            precio_total += cajones_cant * precios
        # Le ponemos return para que devuelva el valor
        return precio_total
# Creamos una variable para poder llamar al archivo y que haga la cuenta con la funcion
costo = costo_camion2('../Data/missing.csv')
print('Costo total:', costo)
    
#%%        
                                # Ejercicio 2.9: Funciones de la biblioteca

# Importamos la libreria CSV 
import csv

# Modificamos la funcion para que lea archivos CSV 
# Asi nos ahorramos pasos como el de transformar las lineas en listas y separarlas 
def costo_camion3(nombre_archivo):
    # Dejamos el codigo encapsulado en la funcion igual que antes
    with open(nombre_archivo,'rt') as f3:
        f3 = csv.reader(f3)
        # Saltamos la primer linea del archivo
        headers = next(f3)
        precio_total  = 0
        for line in f3:
            cajones_cant = int(row[1])
            precios = float(row[2])
            precio_total += cajones_cant * precios
        # Le ponemos return para que devuelva el valor
        return precio_total
# Creamos una variable para poder llamar al archivo y que haga la cuenta con la funcion
costo = costo_camion3('../Data/camion.csv')
print('Costo total:', costo)        

#%% 
                                         # Tuplas

s = ('Manzana', 100, 409.10)
frutita, cajoncito, preciecito = s
print('Costo:', cajoncito * preciecito)

t = {
         'Tomas' : 28,
         'Sebas' : 20,
         'Lean'  : 30
     }
print(t['Tomas'], t['Sebas'])

                                        # Ejercicio 2.10: Tuplas
                                
                                        
with open('../Data/camion.csv', 'rt') as f7:
    # Cargamos el csv en la variable f7
    f7 = csv.reader(f7)
    # Saltamos la primera fila
    next(f7)
    f7 = next(f7)
    # Convertimos la lista en una tupla con los '()'. #
    # Dentro de la tupla, dejamos el valor en la posicion 0 igual.  
    # El valor de la posicion 1 lo cambiamos a entero
    # El valor de la posicion 2 lo cambiamos a float
    t = (f7[0], int(f7[1]), float(f7[2]))
    # Para cada linea que hay en el archivo
    for line in f7:
        # Creamos la variable costo que multiplica el elemento 1ro por el 2do
        cost = t[1] * t[2]
        # Imprimimos el valor total
    print(cost)
        
#%% 
                    # Ejercicio 2.11: Diccionarios como estructuras de datos

# Una alternativa a la tupla es un diccionario.

d = {
        'nombre'  : fila[0],
        'cajones' : int(fila[1]),
        'precio'  : float(fila[2])
    }

cost = d['cajones'] * d['precio']

print(cost)

# A diferencia de las tuplas, los diccionarios se pueden modificar libremente.
d['fecha'] = (14, 8, 2020)
d['cuenta'] = 12345
print(d)

                        # Ejercicio 2.12: Más operaciones con diccionarios
                        
# Podemos iterar el diccionario para obtener las claves

for clave in d:
    print('Clave = ', clave)
    
# Podemos obtener Clave y Valor 

for clave in d:
    print(clave, ' = ', d[clave])

#%%
    
# Una manera más elegante de trabajar con claves y valores simultáneamente es usar el método items(). 
# Esto te devuelve una lista de tuplas de la forma (clave,valor) sobre la que podés iterar.

items = d.items()
print(items)

# De la siguiente manera podemos obtener clave y valor

for k, v in d.items():
        print(k, '=', v)


#%%
                            # Ejercicio 2.13: Diccionario geringoso.
