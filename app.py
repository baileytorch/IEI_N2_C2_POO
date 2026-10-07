from presentacion import cargar_menu


# cargar_menu()
from datos.repositorios.repo_pais import listado_paises,guardar_pais
from prettytable import PrettyTable
from datos.modelos.pais import Pais

tabla_paises = PrettyTable()

nuevo_pais = Pais()
nuevo_pais.pais = 'Baileylandia'
nuevo_pais.nacionalidad = 'Baileylandés'
nuevo_pais.iso2 = 'BL'
nuevo_pais.iso3 = 'BLL'
guardar_pais(nuevo_pais)

paises = listado_paises()
for pais in paises:
    print(f'{pais.id_pais} - {pais.pais} - {pais.nacionalidad} - {pais.iso2} - {pais.iso3} - {pais.habilitado}')
