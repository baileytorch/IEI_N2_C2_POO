from datos.modelos.pais import Pais
from auxiliares import mensaje_error

def listado_paises():
    try:
        paises = Pais.select()
        if paises:
            return paises
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_pais_nombre(nombre_pais):
    try:
        pais = Pais.get(Pais.pais == nombre_pais)
        if pais:
            return pais
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_pais(pais:Pais):
    try:
        respuesta = pais.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {pais.pais}')
    except Exception as error:
        print(f'{mensaje_error}{error}')