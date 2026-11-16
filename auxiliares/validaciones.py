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
    
    if len(errores) > 0:
        contrasena = ''

    return contrasena, errores

def validar_correo(correo):
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(patron_correo, correo):
        mensaje = 'Formato de correo válido\n'
    else:
        mensaje = 'Correo Inválido, ingrese nuevamente...\n'
        correo = ''
    return correo, mensaje

def validar_fecha_nacimiento(fecha_nacimiento):
    patron_fecha_nacimiento = r'^\b(0[1-9]|[12]\d|3[01])[/](0[1-9]|1[0-2])[/](19\d\d|20\d\d)\b$'
    if re.match(patron_fecha_nacimiento, fecha_nacimiento):
        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
            mensaje = 'Formato de fecha correcto'
        except ValueError:
            mensaje = 'Fecha Inválida, ingrese nuevamente...\n'
            fecha_nacimiento = ''
    else:
        mensaje = 'Fecha Inválida, ingrese nuevamente...\n'
        fecha_nacimiento = ''
    
    return fecha_nacimiento, mensaje

def validar_genero(genero):
    if genero in ['1','2','3']:
        mensaje = 'Género válido\n'
    else:
        mensaje = 'Género Inválido, ingrese nuevamente...\n'
        genero = ''
    return genero, mensaje

def validar_rut(rut):
    patron_rut = r'^\d{1,3}(\.?\d{3})*-[0-9kK]$'
    if re.match(patron_rut, rut):
        rut_limpio = rut.replace('.', '').replace('-', '')
        digito_verificador = rut_limpio[-1]
        numero_rut = rut_limpio[:-1]
        rut_invertido = numero_rut[::-1]
        
        multiplicador = 2
        suma = 0
        
        for caracter in rut_invertido:
            suma += int(caracter) * multiplicador
            multiplicador += 1
            if multiplicador > 7:
                multiplicador = 2
                
        resto = suma % 11
        digito_calculado = 11 - resto
        
        if digito_calculado == 11:
            digito_calculado = '0'
        elif digito_calculado == 10:
            digito_calculado = 'K'
        else:
            digito_calculado = str(digito_calculado)
        
        if digito_calculado == digito_verificador:
            mensaje = 'RUT válido\n'
        else:
            mensaje = 'RUT Inválido, ingrese nuevamente...\n'
            rut = ''
    else:
        mensaje = 'Formato de RUT Inválido, ingrese nuevamente...\n'
        rut = ''
    return rut, mensaje
        