import re
from datetime import datetime

def validar_contrasena(contrasena):
    errores = []

    if len(contrasena) < 8 or len(contrasena) > 15:
        errores.append("La contraseña debe tener entre 8 y 15 caracteres.")

    if not any(c.isupper() for c in contrasena):
        errores.append("La contraseña debe contener al menos una letra mayúscula.")

    if not any(c.islower() for c in contrasena):
        errores.append("La contraseña debe contener al menos una letra minúscula.")

    if not any(c.isdigit() for c in contrasena):
        errores.append("La contraseña debe contener al menos un número.")

    if not any(c in "!@#$%&/" for c in contrasena):
        errores.append("La contraseña debe contener al menos uno de los siguientes caracteres especiales: !, @, #, $, %, &. /.")

    return errores

def validar_correo(correo):
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(patron_correo, correo):
        return correo
    else:
        print('Correo Inválido, ingrese nuevamente...')
        return ''

def validar_fecha_nacimiento(fecha_nacimiento):
    patron_fecha_nacimiento = r'^\b(0[1-9]|[12]\d|3[01])[/](0[1-9]|1[0-2])[/](19\d\d|20\d\d)\b$'
    if re.match(patron_fecha_nacimiento, fecha_nacimiento):
        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
            return fecha_nacimiento
        except ValueError:
            print('Fecha Inválida, ingrese nuevamente...')
            return ''
    else:
        print('Fecha Inválida, ingrese nuevamente...')
        return ''

def validar_genero(genero):
    if genero in ['1','2','3']:
        return genero
    else:
        print('Género Inválido, ingrese nuevamente...')
        return ''
        