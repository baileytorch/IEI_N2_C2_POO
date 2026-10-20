from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio import procesar_listado_paises
from datos import obtener_pais_nombre
from negocio import crear_objeto_pais, modificar_objeto_pais

def mostrar_listado_paises():
    try:
        tabla_paises = PrettyTable()
        tabla_paises = procesar_listado_paises(tabla_paises)
        print(tabla_paises)
    except Exception as error:
        print(f'{mensaje_error}{error}')

def crear_pais():
    nombre, nacionalidad, iso2, iso3 = ''
    while nombre == '':
        nombre = input('Ingrese nombre del país: ')
    while nacionalidad == '':
        nacionalidad = input('Ingrese nacionalidad: ')
    while iso2 == '':
        iso2 = input('Ingrese código ISO 2: ')
    while iso3 == '':
        iso3 = input('Ingrese código ISO 3: ')
    crear_objeto_pais(nombre, nacionalidad, iso2, iso3)

def modificar_pais():
    nombre_pais = input('Ingrese nombre del país: ')
    pais = obtener_pais_nombre(nombre_pais)
    if pais:
        print('País Encontrado:')
        print(f'Nombre: {pais.pais}\nNacionalidad: {pais.nacionalidad}')
        nombre, nacionalidad, iso2, iso3 = ''
        while nombre == '':
            nombre = input('Ingrese nuevo nombre del país [o ENTER para conservar]: ')
        while nacionalidad == '':
            nacionalidad = input('Ingrese nueva nacionalidad [o ENTER para conservar]: ')
        while iso2 == '':
            iso2 = input('Ingrese nuevo código ISO 2 [o ENTER para conservar]: ')
        while iso3 == '':
            iso3 = input('Ingrese nuevo código ISO 3 [o ENTER para conservar]: ')
        modificar_objeto_pais(nombre, nacionalidad, iso2, iso3, pais.habilitado, pais)

def eliminar_pais():
    nombre_pais = input('Ingrese nombre del país: ')
    pais = obtener_pais_nombre(nombre_pais)
    if pais:
        print('Se eliminará el país:')
        print(f'Nombre: {pais.pais}\nNacionalidad: {pais.nacionalidad}')
        nombre, nacionalidad, iso2, iso3 = ''
        modificar_objeto_pais(nombre, nacionalidad, iso2, iso3, False, pais)