from auxiliares import nombre_app, version_app, menu_principal, diccionario_menu_principal
import sys
from presentacion.presentacion_pais import mostrar_listado_paises

def cargar_menu():
    print(f'\n{nombre_app} - {version_app}')
    print(f'{'=' * len(nombre_app)}==={'=' * len(version_app)}\n')

    while True:
        print(menu_principal)
        print(f'{'=' * len(menu_principal)}\n')
        for clave, valor in diccionario_menu_principal.items():
            print(f'[{clave}] - {valor}')

        opcion_menu_principal = input(f'Seleccione su opción [0-{len(diccionario_menu_principal)-1}]: ')
        print()
        
        match opcion_menu_principal:
            case '1':
                mostrar_listado_paises()
            case '2':
                print('Seleccionada Opción 2')
            case '3':
                print('Seleccionada Opción 3')
            case '4':
                print('Seleccionada Opción 4')
            case '0':
                print('Saliendo...')
                sys.exit()
            case _:
                print('Opción ingresada NO corresponde,\nintente nuevamente...\n')