
#CLASE DEFINIDA POR MI

class Canguro:
    def __init__(self, nombre, contenido_marsupio=None):
        self.nombre = nombre
        if contenido_marsupio is None:
            self.contenido_marsupio = []
        else:
            self.contenido_marsupio = contenido_marsupio
    
    def meter_en_marsupio(self, objeto):
        self.contenido_marsupio.append(objeto)
    
    def __str__(self):
        return (f'Canguro {self.nombre}, marsupio: {self.contenido_marsupio}')

# tEST
madre_canguro = Canguro('Madre Canguro')
cangurito = Canguro('Cangurito')
madre_canguro.meter_en_marsupio('Avellanas')
madre_canguro.meter_en_marsupio('Zanahorias')
madre_canguro.meter_en_marsupio(cangurito)
print(madre_canguro)
#Salida: Canguro Madre Canguro, marsupio: ['Avellanas', 'Zanahorias', <__main__.Canguro object at 0x0000011B1C49B920>]


#CORRECCION DE LA CLASE DEL EJEMPLO.

class Canguro_Correccion:
    """Un Canguro es un marsupial."""

    def __init__(self, nombre, contenido=None):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista opcional.
        """
        self.nombre = nombre
        if contenido is None:
            self.contenido_marsupio = []
        else:
            self.contenido_marsupio = contenido

    def __str__(self):
        """Devuelve una representación como cadena de este Canguro."""
        t = [self.nombre + ' tiene en su marsupio:']
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objeto a ser agregado
        """
        self.contenido_marsupio.append(item)


#Dentro del constructor " __init__  # se estaba inicializando el contenido como lista vacía.
#Por eso se establece como predeterminado a None y despues se chequea si es None dentro del constructor init

madre_canguro = Canguro_Correccion('Madre')
cangurito = Canguro_Correccion('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)
print(cangurito)