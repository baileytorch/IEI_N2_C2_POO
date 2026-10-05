from datos.modelos.pais import Pais

def listado_paises():
    paises = Pais.select()
    if paises:
        return