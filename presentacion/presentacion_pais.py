from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio import procesar_listado_paises

def mostrar_listado_paises():
    try:
        tabla_paises = PrettyTable()
        tabla_paises = procesar_listado_paises(tabla_paises)
        print(tabla_paises)

    except Exception as error:
        print(f'{mensaje_error}{error}')