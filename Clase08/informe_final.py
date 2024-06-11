
import sys
import fileparse

headers=('Nombre', 'Cajones', 'Precio', 'Cambio')


def leer_camion(nombre_archivo):
    camion = fileparse.parse_csv(nombre_archivo, types=[str, int, float])
    return camion

def leer_precios_frutas(nombre_archivo):
    precios = {}
    datos = fileparse.parse_csv(nombre_archivo, types=[str, float], has_headers=False)
    for nombre, precio in datos:
        precios[nombre] = precio
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




def f_principal(parametros):

    if len(parametros)!=3:
        print(f'Uso adecuado: {parametros[0]} archivo_camion archivo_precios')
        sys.exit(1)

    nombre_archivo_camion=parametros[1]
    nombre_archivo_precios=parametros[2]
    informe_camion(nombre_archivo_camion, nombre_archivo_precios)

if __name__=='__main__':
    f_principal(sys.argv)

