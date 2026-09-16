CREATE TABLE usuarios(
    id_usuario INTEGER AUTO_INCREMENT,
    rut VARCHAR(11) NULL,
    nombre VARCHAR(25) NOT NULL,
    apellido VARCHAR(25) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    pais INTEGER NULL,
    fecha_nacimiento DATE NULL,
    genero INTEGER NOT NULL,
    fecha_incorporacion DATE NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_usuarios PRIMARY KEY (id_usuario),
    CONSTRAINT fk_usuarios_paises FOREIGN KEY (pais) REFERENCES paises(id_pais)
) COMMENT = 'Tabla de usuarios. Género 1 = MASCULINO, 2 = FEMENINO';

CREATE TABLE direcciones_usuarios(
    id_direccion_usuario INTEGER AUTO_INCREMENT,
    direccion INTEGER NOT NULL,
    usuario INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_direccionesusuarios PRIMARY KEY (id_direccion_usuario),
    CONSTRAINT fk_direccionesusuarios_direcciones FOREIGN KEY (direccion) REFERENCES direcciones(id_direccion),
    CONSTRAINT fk_direccionesusuarios_usuarios FOREIGN KEY (usuario) REFERENCES usuarios(id_usuario)
) COMMENT = 'Tabla auxiliar de direcciones de usuarios';

CREATE TABLE tipos_usuario(
    id_tipo_usuario INTEGER AUTO_INCREMENT,
    tipo_usuario VARCHAR(20) NOT NULL,
    descripcion VARCHAR(100) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_tipos_usuario PRIMARY KEY (id_tipo_usuario)
) COMMENT = 'Tabla de tipos de usuario para trabajadores de la biblioteca. 1 = Bibliotecario, 2 = Administrador';

CREATE TABLE bibliotecarios(
    id_bibliotecario INTEGER AUTO_INCREMENT,
    usuario INTEGER NOT NULL,
    tipo_usuario INTEGER NOT NULL,
    contrasena CHAR(60) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_bibliotecarios PRIMARY KEY (id_bibliotecario),
    CONSTRAINT fk_bibliotecarios_usuarios FOREIGN KEY (usuario) REFERENCES usuarios(id_usuario),
    CONSTRAINT fk_bibliotecarios_tiposusuario FOREIGN KEY (tipo_usuario) REFERENCES tipos_usuario(id_tipo_usuario)
) COMMENT = 'Tabla de usuarios de tipo bibliotecario, gestionan libros, lectores y préstamos de la bilioteca';

CREATE TABLE categorias(
    id_categoria INTEGER AUTO_INCREMENT,
    categoria VARCHAR(20) NOT NULL,
    descripcion VARCHAR(100) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_categorias PRIMARY KEY (id_categoria)
) COMMENT = 'Tabla de categorías de lectores';

CREATE TABLE lectores(
    id_lector INTEGER AUTO_INCREMENT,
    usuario INTEGER NOT NULL,
    categoria INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_lectores PRIMARY KEY (id_lector),
    CONSTRAINT fk_lectores_usuarios FOREIGN KEY (usuario) REFERENCES usuarios(id_usuario),
    CONSTRAINT fk_lectores_categorias FOREIGN KEY (categoria) REFERENCES categorias(id_categoria)
) COMMENT = 'Tabla de usuarios de tipo lector, pueden solicitar libros de la bilioteca';

CREATE TABLE inventarios(
    id_inventario INTEGER AUTO_INCREMENT,
    libro INTEGER NOT NULL,
    estado INTEGER NOT NULL,
    ubicacion INTEGER NOT NULL,
    
    CONSTRAINT pk_inventarios PRIMARY KEY (id_inventario),
    CONSTRAINT fk_inventarios_libros FOREIGN KEY (libro) REFERENCES libros(id_libro),
    CONSTRAINT fk_inventarios_estados FOREIGN KEY (estado) REFERENCES estados(id_estado),
    CONSTRAINT fk_inventarios_ubicaciones FOREIGN KEY (ubicacion) REFERENCES ubicaciones(id_ubicacion)
) COMMENT = 'Registro de libros y ubicaciones';

CREATE TABLE prestamos(
    id_prestamo INTEGER AUTO_INCREMENT,
    libro INTEGER NOT NULL,
    lector INTEGER NOT NULL,
    fecha_prestamo DATETIME NOT NULL DEFAULT NOW(),
    fecha_devolucion DATETIME NOT NULL,
    fecha_retorno DATETIME NULL,
    
    CONSTRAINT pk_prestamos PRIMARY KEY (id_prestamo),
    CONSTRAINT fk_prestamos_libros FOREIGN KEY (libro) REFERENCES inventarios(id_inventario),
    CONSTRAINT fk_prestamos_lectores FOREIGN KEY (lector) REFERENCES lectores(id_lector)
) COMMENT = 'Registro de préstamos y devoluciones de libros.';