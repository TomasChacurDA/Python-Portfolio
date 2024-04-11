

def traducir_a_geringoso(palabra):
    geringoso = ''
    for letra in palabra:
        if letra.lower() in 'aeiouáéíóú':
            geringoso += letra + 'p' + letra
        else:
            geringoso += letra
    return geringoso

def diccionario_geringoso(lista_palabras):
    diccionario = {}
    for palabra in lista_palabras:
        diccionario[palabra] = traducir_a_geringoso(palabra)
    return diccionario

# Ejemplo de uso
palabras = ['banana', 'manzana', 'mandarina', 'cadena', 'sebastian']
dicc_geringoso = diccionario_geringoso(palabras)
print(dicc_geringoso)
