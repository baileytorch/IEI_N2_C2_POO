from prettytable import PrettyTable
from datos.repositorios.repositorio_pais import listado_paises

def procesar_listado_paises(tabla:PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'País', 'Nacionalidad', 'ISO 2', 'ISO 3']
        lista_paises = listado_paises()
        if lista_paises:
            for pais in lista_paises:
                tabla.add_row([pais.id_pais, pais.pais, pais.nacionalidad, pais.iso2, pais.iso3])
            return tabla