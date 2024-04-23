import csv



def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for n_row, row in enumerate(rows, start=1):
            
            try:
                 Diccionario = {headers[0]:row[0],
                                headers[1]:int(row[1]),
                                headers[2]:float(row[2])
                                 }
                 camion.append(Diccionario)
            except ValueError:
                print(f'Fila {n_row}: No pude interpretar: {row}')
    return(camion)


camion = leer_camion('../Data/camion.csv')



                        
def leer_precios(nombre_archivo3):
    # Inicializa un diccionario vacío para almacenar los precios
    d = {}
    # Abre el archivo especificado en modo de lectura de texto ('rt') con la codificación UTF-8
    with open(nombre_archivo3, 'rt', encoding='utf8') as f3:
        # Crea un objeto csv.reader para leer las filas del archivo
        rows3 = csv.reader(f3)
        # Itera sobre cada fila del archivo
        for row in rows3:
            # Asigna el primer elemento de la fila como clave y el segundo como valor convertido a flotante
            try:
               d[row[0]] = float(row[1])
            except IndexError:
            # En caso de que no haya suficientes elementos en la fila, pasa a la siguiente fila
                continue
        # Devuelve el diccionario con los precios
        return d # Esta línea debe estar fuera del bloque 'with' para que devuelva el diccionario completo




archivo_camion = '../Data/camion.csv'
archivo_precios = '../Data/precios.csv'

camion = leer_camion(archivo_camion)
precio = leer_precios(archivo_precios)

def balance_del_camion(camion, precio):
    costo_total = 0
    ventas = 0 
    for n_fila, diccionario in enumerate(camion, start=1):
        try:
            costo_total += diccionario['cajones'] * diccionario['precio']
            nombre_fruta = diccionario['nombre']
            precio_fruta = precio[nombre_fruta]
            ventas += diccionario['cajones'] * precio_fruta
            balance_total = ventas - costo_total 
        # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {diccionario}')
            
    return balance_total     

balance = balance_del_camion(camion, precio)

def hacer_informe(camion, precio):
    informe = []
    for element in camion:
        nombre  = element['nombre']
        cajones = element['cajones']
        precios = element['precio']
        cambio = precios - precio[nombre]
        informe.append((nombre, cajones, precios, cambio))
    return informe
    

informe = hacer_informe(camion, precio)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

print(f'{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}')
print(f"{('-'*11+'')*len(headers)}")

for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {"$" + str(precio):>10s} {cambio:>10.2f}')
        























