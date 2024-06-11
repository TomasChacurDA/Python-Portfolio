import csv
import costo_camion

def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        
        for n_fila, fila in enumerate(filas, start = 1):
            record = dict(zip(encabezados, fila))
            try:
                record['cajones'] = int(record['cajones'])
                record['precio'] = float(record['precio'])
                camion.append(record)
            except ValueError:
                print('Faltan datos en la línea', n_fila, 'del archivo.')

    return camion

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for i, row in enumerate(rows):
        
            
            if row: 
                precios[row[0]] = float(row[1])
    return precios

def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], lote['precio'], cambio)
        lista.append(t)
    return lista





def imprimir_informe(informe):
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
    


def informe_camion(camion_csv, precios_csv):
    camion = leer_camion(camion_csv)
    precios = leer_precios(precios_csv)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

informe_camion('../Data/camion.csv', '../Data/precios.csv')




def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):

    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        registros = []
        if has_headers:
            encabezados = next(filas)

        for fila in filas:
            if not fila:    
                continue

            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                fila = [fila[index] for index in indices]

            if types:
                fila = [func(val) for func, val in zip(types, fila)]

            
            if has_headers:
                registro = dict(zip(encabezados, fila))
            else:
                registro = tuple(fila)

            registros.append(registro)  

    return registros



camion=parse_csv('../Data/camion.csv')
dir_camion ='../Data/camion.csv'
dir_precios = '../Data/precios.csv'

cajones_retenido = parse_csv(dir_camion, select=['nombre','cajones'], types=[str, int])

precios_retenido = parse_csv(dir_precios, types=[str, float], has_headers=False)








