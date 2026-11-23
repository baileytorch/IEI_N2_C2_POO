import bcrypt

from auxiliares import nombre_app,version_app
from presentacion.presentacion_usuario import solicitar_correo,solicitar_contrasenia
from presentacion import cargar_menu
from negocio import usuario_por_correo

def login_usuario():
    print(f'\n{nombre_app} - {version_app}')
    print(f'{"=" * (len(nombre_app) + len(version_app) + 3)}\n')
    
    correo = solicitar_correo('Correo: ')
    usuario = usuario_por_correo(correo)
    if usuario:
        contrasenia = solicitar_contrasenia('Contraseña: ')
        if bcrypt.checkpw(contrasenia.encode('utf-8'), usuario.password.encode('utf-8')):
            cargar_menu()
        else:
            print('Contraseña errónea...')
    else:
        print('Usuario NO encontrado.\nIngrese nuevamente...')

def iniciar_aplicacion():
    while True:
        login_usuario()

iniciar_aplicacion()