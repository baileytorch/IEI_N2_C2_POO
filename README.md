# IEI_N2_C2_POO

El objetivo de esta actividad es practicar programación orientada a objetos (POO), modularización, separación de responsabilidades y acceso a una base de datos MySQL mediante un ORM.

## Conceptos que trabajaremos

### Programación orientada a objetos (POO)

La POO organiza el programa alrededor de objetos: unidades que reúnen datos y operaciones relacionadas.

| Concepto | Definición | Ejemplo en el proyecto |
| --- | --- | --- |
| Clase | Molde que define los datos y comportamientos de un tipo de objeto. | `Pais` define los campos de un país. |
| Objeto | Instancia concreta creada a partir de una clase. | Un país obtenido desde la base de datos. |
| Atributo | Dato asociado a una clase u objeto. | `id_pais`, `pais`, `nacionalidad`, `iso2`, `iso3` y `habilitado`. |
| Método | Función asociada a una clase u objeto. | `save()` guarda un modelo de Peewee. |
| Encapsulamiento | Agrupa y protege los detalles internos de una unidad, exponiendo operaciones claras. | Los módulos de datos concentran las consultas y el guardado. |
| Abstracción | Permite usar una operación sin tener que conocer todos sus detalles internos. | El resto de la aplicación puede solicitar un listado sin construir SQL manualmente. |
| Herencia | Permite crear una clase a partir de otra y reutilizar su comportamiento. | `Pais` hereda de `BaseModel`, que comparte la configuración de la base de datos. |
| Polimorfismo | Permite usar una misma operación con objetos de distintos tipos, cada uno con su implementación. | Es un principio de POO que se puede aplicar al extender el sistema con distintos modelos. |

Estos conceptos se estudian y aplican progresivamente; no todas las clases del proyecto necesitan implementar todos los principios.

### Modularización

Modularizar consiste en dividir el programa en módulos pequeños, cada uno con una responsabilidad definida. En Python, los archivos `.py` son módulos y las carpetas con `__init__.py` funcionan como paquetes.

Una buena modularización busca:

- **Alta cohesión:** las funciones de un módulo trabajan en una misma responsabilidad.
- **Bajo acoplamiento:** un módulo depende lo menos posible de los detalles internos de otros.
- **Interfaces claras:** los módulos se comunican mediante funciones y clases con propósitos reconocibles.

Esto facilita entender, probar, mantener y ampliar el sistema sin tener que modificar toda la aplicación a la vez.

### ORM

Un ORM (*Object-Relational Mapper* o mapeador objeto-relacional) conecta el modelo de objetos del programa con las tablas relacionales de una base de datos. En este proyecto usamos **Peewee**.

| En Python | En la base de datos |
| --- | --- |
| Clase de modelo, por ejemplo `Pais` | Tabla, por ejemplo `paises` |
| Atributo/campo del modelo, por ejemplo `iso2` | Columna de la tabla |
| Objeto `Pais` | Fila o registro |
| Consulta del ORM | Consulta SQL construida por Peewee |

El ORM reduce la necesidad de escribir SQL para cada operación y convierte los resultados en objetos que podemos usar desde Python. No reemplaza la base de datos ni elimina la necesidad de entender tablas, claves y relaciones.

## Estructura del proyecto

```text
.
├── app.py                         # Punto de entrada
├── auxiliares/                    # Configuración y textos compartidos de la aplicación
├── presentacion/                  # Menús, interacción con el usuario y salida por pantalla
├── negocio/                       # Procesamiento y coordinación de reglas de negocio
└── datos/
    ├── conexion.py                # Configuración de la conexión MySQL
    ├── modelos/                   # Modelos de Peewee
    ├── repositorios/              # Consultas y operaciones de persistencia
    └── sql/                       # Creación y carga de datos de la base de datos
```

La separación por capas permite ubicar cada responsabilidad:

1. **Presentación:** recibe opciones y datos de la persona usuaria y muestra resultados.
2. **Negocio:** procesa la información y coordina las operaciones de la aplicación.
3. **Datos:** contiene los modelos, repositorios y la conexión con MySQL.

Por ejemplo, al listar países, la presentación solicita el listado, la capa de negocio prepara la tabla y el repositorio consulta los registros mediante el modelo `Pais`.

## Requisitos

- Python **3.12 o superior**.
- MySQL Server en ejecución.
- Acceso a un cliente MySQL, por ejemplo MySQL Workbench o el cliente de consola.

## Instalación

Instala las librerías que utiliza directamente la aplicación:

| Librería | Uso | Comando |
| --- | --- | --- |
| Peewee | ORM y conexión de la aplicación con MySQL. | `python -m pip install peewee` |
| PyMySQL | Driver de Python para conectarse a MySQL mediante Peewee. | `python -m pip install PyMySQL` |
| python-decouple | Lee la configuración de conexión desde `.env`. | `python -m pip install python-decouple` |
| PrettyTable | Presenta el listado de datos en formato de tabla. | `python -m pip install prettytable` |

Para instalarlas en un solo paso, también puedes ejecutar:

```powershell
python -m pip install peewee PyMySQL python-decouple prettytable
```

### Archivo `requirements.txt`

El archivo `requirements.txt` registra versiones de paquetes para que el proyecto pueda instalarse de forma consistente en otro entorno. Una vez instaladas las dependencias necesarias, actualízalo cuando agregues o quites paquetes:

```powershell
python -m pip freeze > requirements.txt
```

En otro equipo o en un entorno virtual nuevo, instala los paquetes registrados con:

```powershell
python -m pip install -r requirements.txt
```

No es necesario ejecutar los comandos individuales y luego instalar el archivo `requirements.txt` en el mismo entorno; basta con uno de los dos métodos.

## Preparación de MySQL

1. En MySQL Workbench o en el cliente de MySQL, ejecuta la instrucción  para crear la base de datos.
2. Selecciona tu DB como esquema activo y ejecuta las sentencias para crear las tablas.
3. Crea un usuario y otorgale únicamente los permisos necesarios sobre tu DB (por ejemplo, `SELECT`, `INSERT`, `UPDATE` y `DELETE`). No uses la cuenta `root` desde la aplicación ni concedas privilegios globales para este ejercicio.

* Crear usuario local 'Usuario' con contraseña 'micontraseña' (Usuario y contraseña debe definirlas Ud.)
```
CREATE USER 'Usuario'@'localhost' IDENTIFIED BY 'micontraseña';
```


* Conceder privilegios para mi base de datos específica al usuario local 'Usuario'  (por ejemplo, 'mibasedatos')
```
GRANT ALL PRIVILEGES ON mibasedatos.* TO 'Usuario'@'localhost';
```


* Aplicar los cambios de privilegios
```
FLUSH PRIVILEGES;
```

## Configuración de conexión

La conexión se configura mediante `python-decouple`. Crea un archivo llamado `.env` en la carpeta raíz del proyecto con los datos de tu instalación:

```dotenv
db=iei_n2_c2
host=localhost
port=3306
user=usuario_aplicacion
password=<tu_clave_mysql>
```

Reemplaza `usuario_aplicacion` y el valor de `password` por las credenciales creadas. El archivo `.env` está excluido del control de versiones: no publiques ni compartas tus contraseñas. Cada integrante debe configurar sus propias credenciales localmente.

## Ejecución

La aplicación inicia el menú principal. La opción para listar países consulta la base de datos; por lo tanto, MySQL debe estar disponible y la tabla `paises` debe existir.

## Convenciones de trabajo

- Mantén cada función o clase en el módulo que corresponde a su responsabilidad.
- Evita colocar consultas SQL o acceso a la base de datos en la capa de presentación.
- Reutiliza los repositorios y modelos existentes al agregar operaciones.
- Usa nombres claros para módulos, clases, funciones y variables.
- No guardes contraseñas, credenciales ni otros datos sensibles en el código fuente.
