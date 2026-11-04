import re
import bcrypt

from datetime import datetime

from negocio.negocio_usuario import crear_objeto_usuario
from datos.repositorios.repositorio_pais import obtener_pais_nombre
from auxiliares.validaciones import validar_contrasena,validar_correo,validar_fecha_nacimiento,validar_genero

def crear_usuario():
    rut = nombre = apellido = correo = nombre_pais = fecha_nacimiento = genero = contrasenia = ''
    titulo = '\nIngrese los datos del Usuario'
    print(titulo)
    print('=' * len(titulo))

    while rut == '':
        rut = input('RUT (11.111.111-1): ')

    while nombre == '':
        nombre = input('Nombre: ')

    while apellido == '':
        apellido = input('Apellido: ')

    while correo == '':
        correo = input('Correo: ')
        correo = validar_correo(correo)

    while nombre_pais == '':
        nombre_pais = input('País: ')
        pais = obtener_pais_nombre(nombre_pais)
        if not pais:
            print('País NO encontrado, ingrese nuevamente...')
            nombre_pais = ''

    while fecha_nacimiento == '':
        fecha_nacimiento = input('Fecha de Nacimiento [dd/mm/aaaa]: ')
        fecha_nacimiento = validar_fecha_nacimiento(fecha_nacimiento)
    
    while genero == '':
        print('Opciones Género: ')
        print('[1] Masculino\n[2] Femenino\n[3] Otro')
        genero = input('Seleccione género [1-3]: ')
        genero = validar_genero(genero)
    
    while contrasenia == '':
        print('Contraseña Segura: ')
        print('- Debe contener al menos una mayúscula\n- Debe contener al menos una minúscula')
        print('- Debe contener entre 8-15 caracteres\n- Debe contener al menos un dígito')
        print('Debe contener al menos un símbolo: !@#$%&/')
        contrasenia = input('Contraseña:')
        resultado = validar_contrasena(contrasenia)
        if len(resultado) > 0:
            print('Contraseña Inválido, resuelva los siguientes errores:')
            for error in resultado:
                print("-", error)
            contrasenia = ''
        else:
            encriptado = bcrypt.hashpw(contrasenia, bcrypt.gensalt())

    crear_objeto_usuario(rut,nombre,apellido,correo,pais.id_pais,fecha_nacimiento,genero,encriptado)