from auxiliares import (
    nombre_app,
    version_app,
    mensaje_error_opcion,
    menu_principal, diccionario_menu_principal,
    menu_configuracion, diccionario_menu_configuracion,
    menu_configurar_parametros, diccionario_menu_configurar_parametros,
    menu_paises, diccionario_menu_paises
)
from presentacion.presentacion_pais import mostrar_listado_paises, crear_pais, modificar_pais, eliminar_pais


def mostrar_menu(titulo, opciones):
    print(titulo)
    print(f'{"=" * len(titulo)}\n')

    for clave, valor in opciones.items():
        print(f'[{clave}] - {valor}')


def cargar_menu_configurar_parametros():
    while True:
        mostrar_menu(menu_configurar_parametros, diccionario_menu_configurar_parametros)
        opcion = input('Seleccione su opción: ')
        print()

        match opcion:
            case '1':
                print('Seleccionada Opción 1')
            case '2':
                print('Seleccionada Opción 2')
            case '3':
                print('Seleccionada Opción 3')
            case '0':
                print('Volviendo al Menú Configuración Sistema...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu_paises():
    while True:
        mostrar_menu(menu_paises, diccionario_menu_paises)
        opcion = input('Seleccione su opción: ')
        print()

        match opcion:
            case '1':
                mostrar_listado_paises()
            case '2':
                crear_pais()
            case '3':
                modificar_pais()
            case '4':
                eliminar_pais()
            case '0':
                print('Volviendo al Menú Configurar Parámetros...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu_configuracion():
    while True:
        mostrar_menu(menu_configuracion, diccionario_menu_configuracion)
        opcion = input('Seleccione su opción: ')
        print()

        match opcion:
            case '1':
                print('Seleccionada Opción 1')
            case '2':
                print('Seleccionada Opción 2')
            case '3':
                cargar_menu_configurar_parametros()
            case '4':
                print('Seleccionada Opción 4')
            case '0':
                print('Volviendo al Menú Principal...\n')
                break
            case _:
                print(mensaje_error_opcion)


def cargar_menu():
    print(f'\n{nombre_app} - {version_app}')
    print(f'{"=" * (len(nombre_app) + len(version_app) + 3)}\n')

    while True:
        mostrar_menu(menu_principal, diccionario_menu_principal)
        opcion = input('Seleccione su opción: ')
        print()

        match opcion:
            case '1':
                mostrar_listado_paises()
            case '2':
                modificar_pais()
            case '3':
                print('Seleccionada Opción 3')
            case '4':
                print('Seleccionada Opción 4')
            case '5':
                cargar_menu_configuracion()
            case '0':
                print('Saliendo...')
                break
            case _:
                print(mensaje_error_opcion)
