import os
import sys
from datetime import datetime
import shutil


def procesar_nombre(fname):
    nuevo_nombre=fname[:-13]+fname[-4:]
    anio=int(fname[-12:-8])
    mes=int(fname[-8:-6])
    dia=int(fname[-6:-4])
    fecha_actualizada = datetime(year = anio, month = mes, day = dia )
    return nuevo_nombre,fecha_actualizada
    
def procesar(fname):
    if len(sys.argv)!=3:
        raise SystemExit(f'Uso correcto: {sys.argv[0]} directorio_original directorio_destino')
    directorio_original=fname[1]
    directorio_destino=fname[2]
    if not os.path.exists(directorio_destino):
        os.mkdir(directorio_destino)
    lista_directorios=[]

    
    for raiz, directorios, archivos in os.walk(directorio_original):
        for directorio in directorios:
            lista_directorios.append(os.path.join(raiz, directorio))
            lista_directorios.append(raiz)
        for archivo in archivos:
            if archivo.endswith('.png'):
                name_modificado,fecha=procesar_nombre(archivo)
                ts_modif=fecha.timestamp() 
                ruta_archivo_original=os.path.join(raiz,archivo)
                ts_acceso=os.stat(ruta_archivo_original).st_atime 
                ruta_archivo_modificado=os.path.join(raiz,name_modificado)
                os.rename(ruta_archivo_original,ruta_archivo_modificado)
                os.utime(ruta_archivo_modificado, (ts_acceso,ts_modif))
                shutil.move(ruta_archivo_modificado,directorio_destino)
            if not os.listdir(raiz):
                os.rmdir(raiz)         
    lista_directorios=set(lista_directorios)            
    for carpeta in lista_directorios:
        try:
            if not os.listdir(carpeta):
                os.rmdir(carpeta)
        except FileNotFoundError:
            pass
               
if __name__ == '__main__':
    procesar(sys.argv)
