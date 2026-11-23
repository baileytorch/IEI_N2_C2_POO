import bcrypt
from prettytable import PrettyTable
import maskpass

from auxiliares import mensaje_error,nombre_app,version_app
import negocio as neg
from auxiliares import (
    validar_rut,
    validar_largo_string,
    validar_correo,
    validar_fecha_nacimiento,
    validar_genero,
    validar_contrasena)


def solicitar_rut(str_input, opcional=False):
    rut = ''
    while rut == '':
        rut = input(str_input).strip()
        if opcional and rut == '':
            return ''
        rut, mensaje = validar_rut(rut)
        print(mensaje)
        if rut != '':
            return rut


def solicitar_dato_obligatorio(str_input):
    while True:
        valor = input(str_input).strip()
        valor, mensaje = validar_largo_string(valor, 25)
        print(mensaje)
        if valor != '':
            return valor


def solicitar_dato_opcional(str_input, opcional=False):
    while True:
        valor = input(str_input).strip()
        if opcional and valor == '':
            return ''
        valor, mensaje = validar_largo_string(valor, 25)
        print(mensaje)
        if valor:
            return valor


def solicitar_correo(str_input, opcional=False):
    while True:
        correo = input(str_input).strip()
        if opcional and correo == '':
            return ''
        correo, mensaje = validar_correo(correo)
        print(mensaje)
        if correo:
            return correo


def _solicitar_nombre_pais(prompt_pais, opcional):
    while True:
        nombre_pais = input(prompt_pais).strip()
        if nombre_pais or opcional:
            return nombre_pais
        print('Ingrese un país.')


def _obtener_ids_paises(nombre_pais):
    resultado = neg.listado_paises_nombre(PrettyTable(), nombre_pais)
    if not resultado:
        print('País no encontrado, ingrese nuevamente...')
        return []

    tabla_paises, id_paises = resultado
    print(tabla_paises)
    return id_paises


def _solicitar_id_pais(prompt_id, id_paises, opcional):
    while True:
        entrada = input(prompt_id).strip()
        if opcional and not entrada:
            return ''

        if not entrada.isdecimal():
            print('Ingrese un ID numérico.')
            continue

        if int(entrada) in id_paises:
            return entrada

        print('El ID no corresponde a los países mostrados.')


def solicitar_pais(prompt_pais, prompt_id, opcional=False):
    while True:
        nombre_pais = _solicitar_nombre_pais(prompt_pais, opcional)
        if not nombre_pais:
            return ''

        id_paises = _obtener_ids_paises(nombre_pais)
        if id_paises:
            return _solicitar_id_pais(prompt_id, id_paises, opcional)


def solicitar_fecha_nacimiento(str_input, opcional=False):
    while True:
        fecha_nacimiento = input(str_input).strip()
        if opcional and fecha_nacimiento == '':
            return ''
        fecha_nacimiento, mensaje = validar_fecha_nacimiento(fecha_nacimiento)
        print(mensaje)
        if fecha_nacimiento:
            return fecha_nacimiento


def solicitar_genero(str_input, opcional=False):
    while True:
        print('Opciones Género: ')
        print('[1] Masculino\n[2] Femenino\n[3] Otro')
        genero = input(str_input).strip()
        if opcional and genero == '':
            return ''
        genero, mensaje = validar_genero(genero)
        print(mensaje)
        if genero:
            return genero


def solicitar_contrasenia(str_input,crear=False):
    contrasenia = ''
    while contrasenia == '':
        if crear:
            print('Contraseña Segura: ')
            print(
                '- Debe contener al menos una mayúscula\n- Debe contener al menos una minúscula')
            print('- Debe contener entre 8-15 caracteres\n- Debe contener al menos un dígito')
            print('- Debe contener al menos un símbolo: !@#$%&/')
        contrasenia = maskpass.askpass(prompt=str_input, mask='*')
        contrasenia, mensaje = validar_contrasena(contrasenia)
        if len(mensaje) > 0:
            print('Contraseña Inválida, resuelva los siguientes errores:')
            for error in mensaje:
                print("-", error)
        if contrasenia != '':
            return contrasenia


def mostrar_listado_usuarios():
    try:
        tabla_usuarios = PrettyTable()
        tabla_usuarios = neg.procesar_listado_usuarios(tabla_usuarios)
        print(tabla_usuarios)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_usuario():
    titulo = '\nIngrese los datos del Usuario'
    print(titulo)
    print('=' * len(titulo))

    rut = solicitar_rut('RUT (11.111.111-1): ')
    nombre = solicitar_dato_obligatorio('Nombre: ')
    apellido = solicitar_dato_obligatorio('Apellido: ')
    correo = solicitar_correo('Correo: ')
    id_pais = solicitar_pais('País: ', 'Id País: ')
    fecha_nacimiento = solicitar_fecha_nacimiento(
        'Fecha de Nacimiento [dd/mm/aaaa]: ')
    genero = solicitar_genero('Seleccione género [1-3]: ')
    contrasenia = solicitar_contrasenia('Contraseña: ',True)
    encriptado = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())

    neg.crear_objeto_usuario(
        rut, nombre, apellido, correo, id_pais, fecha_nacimiento, genero, encriptado)


def modificar_usuario():
    titulo = '\nIngrese los datos del Usuario a modificar'
    print(titulo)
    print('=' * len(titulo))

    rut = solicitar_rut('RUT (11.111.111-1): ')
    usuario = neg.usuario_por_rut(rut)
    if not usuario:
        print('Usuario no encontrado.')
        return

    rut = solicitar_rut(
        'RUT (11.111.111-1) (ENTER para conservar): ', opcional=True)
    nombre = solicitar_dato_opcional(
        'Nombre (ENTER para conservar): ', opcional=True)
    apellido = solicitar_dato_opcional(
        'Apellido (ENTER para conservar): ', opcional=True)
    correo = solicitar_correo(
        'Correo (ENTER para conservar): ', opcional=True)
    id_pais = solicitar_pais(
        'País (ENTER para conservar): ',
        'Id País (ENTER para conservar): ',
        opcional=True)
    fecha_nacimiento = solicitar_fecha_nacimiento(
        'Fecha de Nacimiento [dd/mm/aaaa] (ENTER para conservar): ',
        opcional=True)
    genero = solicitar_genero(
        'Seleccione género [1-3] (ENTER para conservar): ',
        opcional=True)

    neg.modificar_objeto_usuario(
        rut, nombre, apellido, correo, id_pais, fecha_nacimiento, genero, usuario
    )

def eliminar_usuario():
    titulo = '\nIngrese los datos del Usuario a eliminar'
    print(titulo)
    print('=' * len(titulo))

    rut = solicitar_rut('RUT (11.111.111-1): ')
    usuario = neg.usuario_por_rut(rut)
    if not usuario:
        print('Usuario no encontrado.')
        return
    else:
        print(f'¿Está seguro de ELIMINAR al usuario {usuario.rut} {usuario.apellido}, {usuario.nombre}?')
        opcion = input('Ingrese S/N:')
        if opcion.lower() == 's':
            usuario.habilitado = False

            neg.modificar_objeto_usuario(
                '', '', '', '', '', '', '', usuario
            )
        else:
            return
    