from prettytable import PrettyTable

from datetime import datetime
import re

from datos.repositorios.repositorio_usuario import listado_usuarios_habilitados, guardar_usuario,obtener_usuario_rut
from datos.modelos.usuario import Usuario
from auxiliares import mensaje_error

def procesar_listado_usuarios(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'RUT', 'Nombre Completo', 'Correo', 'Nacionalidad', 'Fecha Nacimiento', 'Género', 'Habilitado']
        lista_usuarios = listado_usuarios_habilitados()
        if lista_usuarios:
            for usuario in lista_usuarios:
                nombre_completo = f'{usuario.nombre} {usuario.apellido}'

                genero_usuario = ''
                match usuario.genero:
                    case 1:
                        genero_usuario = 'Masculino'
                    case 2:
                        genero_usuario = 'Femenino'
                    case 3:
                        genero_usuario = 'Otro'
                
                estado = 'Habilitado' if usuario.habilitado else 'Deshabilitado'

                tabla.add_row([
                    usuario.id_usuario,
                    usuario.rut,
                    nombre_completo,
                    usuario.correo,
                    usuario.pais.nacionalidad,
                    usuario.fecha_nacimiento,
                    genero_usuario,
                    estado
                ])
            return tabla


def crear_objeto_usuario(str_rut, str_nombre, str_apellido, str_correo, str_id_pais, fecha_nacimiento, str_genero, str_contrasenia):
    try:
        usuario = Usuario()
        usuario.rut= str_rut
        usuario.nombre = str_nombre.title()
        usuario.apellido = str_apellido.title()
        usuario.correo = str_correo.lower()
        usuario.pais = int(str_id_pais)
        usuario.fecha_nacimiento = fecha_nacimiento
        usuario.genero = int(str_genero)
        usuario.password = str_contrasenia
        usuario.fecha_incorporacion = datetime.now()
        usuario.habilitado = True
        guardar_usuario(usuario)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_objeto_usuario(str_rut, str_nombre, str_apellido, str_correo, str_pais, fecha_nacimiento, str_genero, usuario: Usuario):
    try:
        if usuario.rut != str_rut and str_rut != '':
            usuario.rut = str_rut
        if usuario.nombre != str_nombre and str_nombre != '':
            usuario.nombre = str_nombre.title()
        if usuario.apellido != str_apellido and str_apellido != '':
            usuario.apellido = str_apellido.title()
        if usuario.correo != str_correo and str_correo != '':
            usuario.correo = str_correo
        if str(usuario.pais) != str_pais and str_pais != '':
            usuario.pais = int(str_pais)
        if usuario.fecha_nacimiento != fecha_nacimiento and fecha_nacimiento != '':
            usuario.fecha_nacimiento = fecha_nacimiento
        if str_genero != '' and usuario.genero != int(str_genero):
            usuario.genero = int(str_genero)
            
        guardar_usuario(usuario)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def deshabilitar_objeto_usuario(usuario: Usuario):
    try:
        usuario.habilitado = False
            
        guardar_usuario(usuario)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        
def usuario_por_rut(rut):
    try:
        usuario = obtener_usuario_rut(rut)
        if usuario:
            return usuario
    except Exception as error:
        print(f'{mensaje_error}{error}')