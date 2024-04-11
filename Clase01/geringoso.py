                        '''1.14 Extraer caracteres individuales y subcadenas'''
frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'
frutas[0]
frutas[1]
frutas[2]
frutas[-1]        # Último caracter.
frutas[-2]        # Índices negativos se cuentan desde el final.

                        '''1.15 Concatenación de cadenas'''

# Agregamos Pera al final de la cadena.
frutas = frutas + ',Pera'


# Agregamos Melon al principio de la cadena.
frutas = 'Melon,' + frutas 
print(frutas)
                        
                        '''1.16 Testeo de pertenencia'''
                        
print('Naranja' in frutas)
print('nana' in frutas)
print('Lima' in frutas)

# ¿Por qué la verificación de 'nana' dió True?.
    # Porque es parte del String 'Banana'.
    
                        '''1.17 Iteración sobre cadenas'''
                        
cadena = "Ejemplo con for"
for c in cadena:
    print('caracter :', c)

# Modificamos el codigo del ejercicio 1.17 para que cuente las 'o'.

cadena = "Ejemplo con for"
contar_o = 0
for c in cadena:
    if c == 'o':
        contar_o += 1
# Pongo el print fuera del bucle para que no se repita todo el tiempo.
print('Cantidad de letras o :', contar_o)    
    
                        '''1.18 Geringoso'''

# Agregamos 'pa', 'pe', 'pi', 'po', 'pu' luego de cada vocal.
cadena = 'Geringoso'
capadepenapa = ''
vocales = 'aeiouAEIOU'

for c in cadena:
    capadepenapa += c
    if c in vocales:
        # Agregar la silaba
        if c.lower() == 'a':
            capadepenapa += 'pa'
        elif c.lower() == 'e':
            capadepenapa += 'pe'
        elif c.lower() == 'i':
            capadepenapa += 'pi'
        elif c.lower() == 'o':
            capadepenapa += 'po'
        elif c.lower() == 'u':
            capadepenapa += 'pu'

print(capadepenapa)


        
        