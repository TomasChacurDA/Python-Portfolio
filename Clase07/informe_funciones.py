import csv
headers=('Nombre', 'Cajones', 'Precio', 'Cambio')

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo, 'rt') as f:
        reader=csv.reader(f)
        headers=next(reader)
        for i,row in enumerate(reader):
            record=dict(zip(headers,row))
            try:
                lote={'nombre':record['nombre'],'cajones':int(record['cajones']),'precio':float(record['precio'])}
                camion.append(lote)
            except ValueError:
                print(f"¡Advertencia! Se detectó un campo vacío en la linea : {row}")
    return camion


def leer_precios_frutas(nombre_archivo):
    precios={}
    with open(nombre_archivo, 'rt') as f:
        archivo=csv.reader(f)
        #header=next(archivo)
        for i,row in enumerate(archivo):
            try:
                precios[row[0]] = float(row[1])
                #print(row)
            except (IndexError, ValueError):
                continue
                #print(f'¡Error detectado en la línea {i}: {row}')
    return precios


def hacer_informe(camion,precios):
    
    informe=[]
    for fruta in camion:
        nombre=fruta['nombre']
        cajones=fruta['cajones']
        precio_compra=fruta['precio']
        if nombre in precios:
            precio_venta=precios[nombre]
            cambio=precio_venta-precio_compra
            informe.append((nombre,cajones,precio_compra,cambio))
    return informe


def imprimir_informe(informe):
    headers_espaciado = [f'{header:>10}' for header in headers]
    string_headers = ' '.join(headers_espaciado)
    headers_lines = []

    for header in headers_espaciado:
        headers_lines.append(len(header)*'-')

    string_lines = ' '.join(headers_lines)

    print(string_headers)
    print(string_lines)

    for nombre, cajones, precio_compra, cambio in informe:
        precio_compra_str=f'${precio_compra:.2f}'
        print(f'{nombre:>10s} {cajones:>10d} {precio_compra_str:>10} {cambio:>10.2f}')


def informe_camion(nombre_archivo_camion,nombre_archivo_precios):
    
    camion=leer_camion(nombre_archivo_camion)
    precios=leer_precios_frutas(nombre_archivo_precios)
    informe=hacer_informe(camion, precios)
    imprimir_informe(informe)


informe_camion('../Data/camion.csv','../Data/precios.csv')
files=['../Data/camion.csv','../Data/camion2.csv']


for name in files:
        print(f'{name:-^43s}')
        informe_camion(name, '../Data/precios.csv')
        print()



