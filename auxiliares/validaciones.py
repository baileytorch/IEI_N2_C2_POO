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
            return rut
        else:
            print('RUT Inválido, ingrese nuevamente...')
            return ''
    else:
        print('Formato de RUT Inválido, ingrese nuevamente...')
        return ''
        