from datos.modelos.usuario import Usuario
from auxiliares import mensaje_error

def listado_usuarios_habilitados():
    try:
        usuarios = Usuario.select().where(Usuario.habilitado == True)
        if usuarios:
            return usuarios
    except Exception as error:
        print(f'{mensaje_error}{error}')

def listado_usuarios_deshabilitados():
    try:
        usuarios = Usuario.select().where(Usuario.habilitado == False)
        if usuarios:
            return usuarios
    except Exception as error:
        print(f'{mensaje_error}{error}')

def listado_usuarios():
    try:
        usuarios = Usuario.select()
        if usuarios:
            return usuarios
    except Exception as error:
        print(f'{mensaje_error}{error}')

def obtener_usuario_rut(rut_usuario):
    try:
        usuario = Usuario.get(Usuario.rut == rut_usuario)
        if usuario:
            return usuario
    except Exception as error:
        print(f'{mensaje_error}{error}')

def guardar_usuario(usuario:Usuario):
    try:
        respuesta = usuario.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito, ID: {usuario.id_usuario}')
    except Exception as error:
        print(f'{mensaje_error}{error}')