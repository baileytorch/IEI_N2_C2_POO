from prettytable import PrettyTable
from datos.repositorios.repositorio_pais import listado_paises
from datos import Pais,guardar_pais
from auxiliares import mensaje_error

def procesar_listado_paises(tabla:PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'País', 'Nacionalidad', 'ISO 2', 'ISO 3']
        lista_paises = listado_paises()
        if lista_paises:
            for pais in lista_paises:
                tabla.add_row([pais.id_pais, pais.pais, pais.nacionalidad, pais.iso2, pais.iso3])
            return tabla

def crear_objeto_pais(nombre:str, nacionalidad:str, iso2:str, iso3:str):
    try:
        pais = Pais(nombre, nacionalidad, iso2, iso3)
        guardar_pais(pais)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def modificar_objeto_pais(nombre:str, nacionalidad:str, iso2:str, iso3:str, habilitado:bool, pais: Pais):
    try:
        if pais.pais != nombre and nombre != '':
            pais.pais = nombre
        if pais.nacionalidad != nacionalidad and nacionalidad != '':
            pais.nacionalidad = nacionalidad
        if pais.iso2 != iso2 and iso2 != '':
            pais.iso2 = iso2
        if pais.iso3 != iso3 and iso3 != '':
            pais.iso3 = iso3
        if pais.habilitado != habilitado:
            pais.habilitado = habilitado
        guardar_pais(pais)
    except Exception as error:
        print(f'{mensaje_error}{error}')