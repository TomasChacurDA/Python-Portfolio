
from datetime import timedelta, datetime

def vida_en_segundos(fecha_nac):

    fecha_nac_time = datetime.strptime(fecha_nac, '%d/%m/%Y')
    ahora = datetime.now()
    tiempo_vivido = ahora - fecha_nac_time
    segundos_vividos = tiempo_vivido.total_seconds()

    return segundos_vividos

fecha_nac = '14/11/1995'
print(vida_en_segundos(fecha_nac))
type(vida_en_segundos(fecha_nac)) 



