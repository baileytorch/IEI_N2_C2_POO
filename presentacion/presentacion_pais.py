from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio import procesar_listado_paises
from datos import obtener_pais_nombre

def mostrar_listado_paises():
    try:
        tabla_paises = PrettyTable()
        tabla_paises = procesar_listado_paises(tabla_paises)
        print(tabla_paises)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def modificar_pais():
    nombre_pais = input('Ingrese nombre del país: ')
    pais = obtener_pais_nombre(nombre_pais)
    if pais:
        print('País Encontrado:')
        print(f'Nombre: {pais.pais}\nNacionalidad: {pais.nacionalidad}')
