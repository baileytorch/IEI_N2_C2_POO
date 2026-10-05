from presentacion import cargar_menu


# cargar_menu()
from datos.repositorios.repo_pais import listado_paises
from prettytable import PrettyTable

tabla_paises = PrettyTable()
paises = listado_paises()