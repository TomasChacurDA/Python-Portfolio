import csv

def precio_cajon(fruta, existe_fruta =True):
    precio = None
    with open('../Data/camion.csv','rt', encoding= 'utf-8') as archivo:
        camion_csv = csv.reader(archivo)
        for linea in camion_csv:
            if linea:
                if linea[0] == fruta:
                    precio = float(linea[1])
    
    if existe_fruta:
        if precio != None:
            print(f'El precio de un cajon de {fruta} es: {precio}')
        else:
            print(f'{fruta} no figura en el listado de precios.')
    return precio
