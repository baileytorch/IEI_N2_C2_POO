from prettytable import PrettyTable

from datetime import datetime
import re

from datos.repositorios.repositorio_usuario import listado_usuarios_habilitados, guardar_usuario
from datos.repositorios.repositorio_pais import obtener_pais_id
from datos.modelos.usuario import Usuario
from auxiliares import mensaje_error


def procesar_listado_usuarios(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ['Id', 'RUT', 'Nombre Completo', 'Correo', 'Nacionalidad', 'Fecha Nacimiento', 'Género']
        lista_usuarios = listado_usuarios_habilitados()
        if lista_usuarios:
            for usuario in lista_usuarios:
                nombre_completo = f'{usuario.nombre} {usuario.apellido}'

                pais = obtener_pais_id(usuario.pais)

                genero_usuario = ''
                match usuario.genero:
                    case 1:
                        genero_usuario = 'Masculino'
                    case 2:
                        genero_usuario = 'Femenino'
                    case 3:
                        genero_usuario = 'Otro'

                tabla.add_row([
                    usuario.id_usuario,
                    usuario.rut,
                    nombre_completo,
                    usuario.correo,
                    pais.nacionalidad,
                    usuario.fecha_nacimiento,
                    genero_usuario
                ])
            return tabla


def crear_objeto_usuario(str_rut, str_nombre, str_apellido, str_correo, id_pais, fecha_nacimiento, str_genero, str_contrasenia):
    try:
        usuario = Usuario
        usuario.rut= str_rut
        usuario.nombre = str_nombre
        usuario.apellido = str_apellido
        usuario.correo = str_correo
        usuario.pais = id_pais
        usuario.fecha_nacimiento = fecha_nacimiento
        usuario.genero = int(str_genero)
        usuario.password = str_contrasenia
        usuario.fecha_incorporacion = datetime.now()
        usuario.habilitado = True
        guardar_usuario(usuario)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_objeto_usuario(str_rut, str_nombre, str_apellido, str_correo, str_pais, fecha_nacimiento, int_genero, str_contrasenia, usuario: Usuario):
    try:
        if usuario.rut != str_rut and str_rut != '':
            usuario.rut = str_rut
        if usuario.nombre != str_nombre and str_nombre != '':
            usuario.nombre = str_nombre
        if usuario.apellido != str_apellido and str_apellido != '':
            usuario.apellido = str_apellido
        if usuario.correo != str_correo and str_correo != '':
            usuario.correo = str_correo
        if usuario.pais != str_pais and str_pais != '':
            usuario.pais = str_pais
        if usuario.fecha_nacimiento != fecha_nacimiento and fecha_nacimiento != '':
            usuario.fecha_nacimiento = fecha_nacimiento
        if usuario.genero != int_genero and int_genero != '':
            usuario.genero = int_genero
        if usuario.password != str_contrasenia and str_contrasenia != '':
            usuario.password = str_contrasenia
            
        guardar_usuario(usuario)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def deshabilitar_objeto_usuario(usuario: Usuario):
    try:
        usuario.habilitado = False
            
        guardar_usuario(usuario)
    except Exception as error:
        print(f'{mensaje_error}{error}')