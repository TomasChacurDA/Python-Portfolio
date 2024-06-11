
import informe_funciones

def costo_camion(nombre_archivo):
    camion = informe_funciones.leer_camion(nombre_archivo)
    total = sum(item['cajones'] * item['precio'] for item in camion)
    return total

# Ruta relativa a los archivos
dir_camion = '../Data/camion.csv'
dir_missing = '../Data/missing.csv'
dir_fecha_camion = '../Data/fecha_camion.csv'


print(costo_camion('../Data/camion.csv'))