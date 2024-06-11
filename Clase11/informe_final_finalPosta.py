import fileparse
import lote
import formato_tabla

def leer_camion(nombre_archivo):
    with open(nombre_archivo) as f:
        camion = fileparse.parse_csv(f, select = ['nombre', 'cajones', 'precio'], types = [str, int, float], has_headers = True)
        objetos_camion = [lote.Lote(dic['nombre'], dic['cajones'], dic['precio']) for dic in camion]
    return objetos_camion

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types = [str, float], has_headers = False)
    return precios

def hacer_informe(objetos_camion, precios):
    lista = []
    for objeto in objetos_camion:
        cambio = precios[objeto.nombre] - objeto.precio
        t = (objeto.nombre, objeto.cajones, objeto.precio, cambio)
        lista.append(t)
    return lista

def imprimir_informe(informe, formateador):
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in informe:
        rowdata = [nombre, str(cajones),f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)


def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt):
    objetos_camion = leer_camion(nombre_archivo_camion)
    lista_precios = leer_precios(nombre_archivo_precios)
    precios = dict(lista_precios)
    informe = hacer_informe(objetos_camion, precios)
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(informe, formateador)


def f_principal(argumentos):
    informe_camion(argumentos[1], argumentos[2], argumentos[3])

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    






