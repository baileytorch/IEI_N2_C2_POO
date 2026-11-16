import bcrypt
from prettytable import PrettyTable
import maskpass

from datetime import datetime
import re

from auxiliares import mensaje_error
from negocio.negocio_usuario import procesar_listado_usuarios,crear_objeto_usuario,modificar_objeto_usuario
from datos.repositorios.repositorio_pais import obtener_pais_nombre
from datos.repositorios.repositorio_usuario import obtener_usuario_rut
from auxiliares.validaciones import validar_contrasena,validar_correo,validar_fecha_nacimiento,validar_genero,validar_rut

def mostrar_listado_usuarios():
    try:
        tabla_usuarios = PrettyTable()
        tabla_usuarios = procesar_listado_usuarios(tabla_usuarios)
        print(tabla_usuarios)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        
def crear_usuario():
    rut = nombre = apellido = correo = nombre_pais = fecha_nacimiento = genero = contrasenia = ''
    titulo = '\nIngrese los datos del Usuario'
    print(titulo)
    print('=' * len(titulo))

    while rut == '':
        rut = input('RUT (11.111.111-1): ')
        rut, mensaje = validar_rut(rut)
        print(mensaje)

    while nombre == '':
        nombre = input('Nombre: ')

    while apellido == '':
        apellido = input('Apellido: ')

    while correo == '':
        correo = input('Correo: ')
        correo, mensaje = validar_correo(correo)
        print(mensaje)

    while nombre_pais == '':
        nombre_pais = input('País: ')
        paises = obtener_pais_nombre(nombre_pais)
        if not paises:
            print('País NO encontrado, ingrese nuevamente...')
            nombre_pais = ''
        else:
            tabla_paises = PrettyTable()
            tabla_paises.field_names = ['Id','Pais','Nacionalidad']
            for pais in paises:
                tabla_paises.add_row([pais.id_pais,pais.pais,pais.nacionalidad])
            print(tabla_paises)
            id_pais = input('Id País: ')

    while fecha_nacimiento == '':
        fecha_nacimiento = input('Fecha de Nacimiento [dd/mm/aaaa]: ')
        fecha_nacimiento, mensaje = validar_fecha_nacimiento(fecha_nacimiento)
        print(mensaje)
    
    while genero == '':
        print('Opciones Género: ')
        print('[1] Masculino\n[2] Femenino\n[3] Otro')
        genero = input('Seleccione género [1-3]: ')
        genero, mensaje = validar_genero(genero)
        print(mensaje)
    
    while contrasenia == '':
        print('Contraseña Segura: ')
        print('- Debe contener al menos una mayúscula\n- Debe contener al menos una minúscula')
        print('- Debe contener entre 8-15 caracteres\n- Debe contener al menos un dígito')
        print('Debe contener al menos un símbolo: !@#$%&/')
        contrasenia = maskpass.askpass(prompt='Contraseña:', mask='*')
        contrasenia, resultado = validar_contrasena(contrasenia)
        if len(resultado) > 0:
            print('Contraseña Inválido, resuelva los siguientes errores:')
            for error in resultado:
                print("-", error)
            contrasenia = ''
        else:
            encriptado = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())

    crear_objeto_usuario(rut,nombre,apellido,correo,id_pais,fecha_nacimiento,genero,encriptado)
    
def modificar_usuario():
    rut = nombre = apellido = correo = nombre_pais = fecha_nacimiento = genero = ''
    titulo = '\nIngrese los datos del Usuario a modificar'
    print(titulo)
    print('=' * len(titulo))

    while rut == '':
        rut = input('RUT (11.111.111-1): ')
        rut, mensaje = validar_rut(rut)
        print(mensaje)
        if rut != '':
            usuario = obtener_usuario_rut(rut)

            if usuario:
                nombre = input('Nombre (o ENTER para conservar): ')
                apellido = input('Apellido (o ENTER para conservar): ')

                correo = input('Correo (o ENTER para conservar): ')
                if correo != '':
                    correo, mensaje = validar_correo(correo)
                    print(mensaje)

                nombre_pais = input('País (o ENTER para conservar): ')
                if nombre_pais != '':
                    paises = obtener_pais_nombre(nombre_pais)
                    if not paises:
                        print('País NO encontrado, ingrese nuevamente...')
                        nombre_pais = ''
                    else:
                        tabla_paises = PrettyTable()
                        tabla_paises.field_names = ['Id','Pais','Nacionalidad']
                        for pais in paises:
                            tabla_paises.add_row([pais.id_pais,pais.pais,pais.nacionalidad])
                            print(tabla_paises)
                        id_pais = input('Id País (o ENTER para conservar): ')

                fecha_nacimiento = input('Fecha de Nacimiento [dd/mm/aaaa] (o ENTER para conservar): ')
                if fecha_nacimiento != '':
                    fecha_nacimiento, mensaje = validar_fecha_nacimiento(fecha_nacimiento)
                    print(mensaje)
                
                print('Opciones Género: ')
                print('[1] Masculino\n[2] Femenino\n[3] Otro')
                genero = input('Seleccione género [1-3] (o ENTER para conservar): ')
                if genero != '':
                    genero, mensaje = validar_genero(genero)
                    print(mensaje)

                modificar_objeto_usuario(rut,nombre,apellido,correo,id_pais,fecha_nacimiento,genero,usuario)