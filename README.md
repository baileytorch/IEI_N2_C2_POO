# IEI_N2_C2_POO
___
Desarrollo Modular Proyecto POO

El desarrollo modular de software es una técnica que divide un programa grande en partes más pequeñas e independientes llamadas módulos. Cada bloque cumple una función específica y se conecta con los demás mediante interfaces claras, lo que facilita crear sistemas ordenados, fáciles de probar y simples de actualizar.

## Principios Clave
    - Módulos independientes: Bloques de código con una tarea única que funcionan por sí mismos.
    - Alta cohesión: Cada parte hace una sola cosa y la hace muy bien.
    - Bajo acoplamiento: Los módulos dependen poco el uno del otro, permitiendo cambios sin romper el sistema.

## Ventajas Principales
    - Mantenimiento fácil: Los errores se buscan y arreglan rápido en una sola sección.
    - Trabajo en equipo: Varios grupos pueden crear distintas partes al mismo tiempo.
    - Reutilización: Las piezas sirven de nuevo en otros proyectos.
    - Crecimiento simple: Se añaden funciones nuevas sin rediseñar todo el programa.
___

* Instalación ORM + Driver de base de datos. Mediante terminal de VSCode o CMD ejecutaremos el siguiente comando:
```
pip install peewee pymysql
```
- Peewee es el ORM que utilizaremos para procesar los datos.
- Pymysql es el driver que permitirá la conexión con la base de datos.

Para usar las herramientas de automatización de peewee necesitamos crear un usuario con permisos y seguridad en nuestra base de datos.
* Crear usuario local 'Usuario' con contraseña 'mypassword'
```
CREATE USER 'Usuario'@'localhost' IDENTIFIED BY 'mypassword';
```

* Crear usuario remoto 'Usuario' con contraseña 'mypassword'
```
CREATE USER 'Usuario'@'%' IDENTIFIED BY 'mypassword';
```

* Conceder privilegios al usuario 'Usuario' local para todas las bases de datos y tablas
```
GRANT ALL PRIVILEGES ON *.* TO 'Usuario'@'localhost' WITH GRANT OPTION;
```

* Conceder privilegios al usuario 'Usuario' global para todas las bases de datos y tablas
```
GRANT ALL PRIVILEGES ON *.* TO 'Usuario'@'%' WITH GRANT OPTION;
```

* Conceder privilegios para una base de datos específica aal usuario 'Usuario' local  (por ejemplo, 'mydatabase')
```
GRANT ALL PRIVILEGES ON mydatabase.* TO 'Usuario'@'localhost';
```

* Conceder privilegios para una base de datos específica aal usuario 'Usuario' global  (por ejemplo, 'mydatabase')
```
GRANT ALL PRIVILEGES ON mydatabase.* TO 'Usuario'@'%';
```

* Aplicar los cambios de privilegios
```
FLUSH PRIVILEGES;
```

Creacion de modelo de forma automatica:
```
python -m pwiz -e mysql -H localhost -p 3306 -u your_username -P your_database_name > models.py
```
___
*ORM* Object Relational Mapping. Estas librerías se encargan de ofrecer clases y métodos para que podamos manipular la base de datos usando programación orientada a objetos.