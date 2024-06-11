import csv

def parse_csv(source, select=None, types=None, has_headers=True, silence_errors=False):
    
    if isinstance(source, str):
        f = open(source, 'rt')
        close_file = True
    else:
        f = source
        close_file = False

    filas = csv.reader(f)
    registros = []

    
    if has_headers:
        encabezados = next(filas)

    for num_fila, fila in enumerate(filas, start=1):
        if not fila:    
            continue

        try:
            
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                fila = [fila[index] for index in indices]

            
            if types:
                fila = [func(val) for func, val in zip(types, fila)]

        except ValueError as e:
            
            if not silence_errors:
                print(f'Fila {num_fila}: No se pudo convertir {fila}')
                print(f'Fila {num_fila}: Motivo: {str(e)}')
            continue

        
        registro = dict(zip(encabezados, fila)) if has_headers else tuple(fila)
        registros.append(registro)

    # Si el archivo se abrió dentro de la función, lo cerramos
    if close_file:
        f.close()

    #Devolvemos la lista de registros
    return registros

# acá establezco varios casos de uso
if __name__ == "__main__":
    import fileparse
    import gzip
    # Probamos con la dirección de un archivo (que ingresará al bucle isinstance para ser abierto y asignado a la variable f)
    camion = parse_csv('..\Data\camion.csv', types=[str, int, float])
    print(camion)

    # Probando con un archivo abierto que salteará isinstance y se asignará directamente a la variable f
    with open('..\Data\camion.csv', 'rt') as file:
        camion = parse_csv(file, types=[str, int, float])
        print(camion)

    # En este caso le pasamos una lista (con encabezados) que será leído sin problemas por csv.reader por ser un iterable
    lines = ['nombre,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
    camion = parse_csv(lines, types=[str, int, float])
    print(camion)

    #Acá abrimos un gz como file, lo pasamos a la funcion parse_csv y asignamos la lista de salida a camion.
    with gzip.open('..\Data\camion.csv.gz', 'rt') as file:
        camion = parse_csv(file, types=[str,int,float])

   
