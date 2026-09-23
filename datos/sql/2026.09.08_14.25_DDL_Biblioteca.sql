CREATE DATABASE iei_n2_c2;

CREATE TABLE parametros(
    id_parametro INTEGER AUTO_INCREMENT,
    codigo VARCHAR(20) NOT NULL,
    parametro VARCHAR(50) NOT NULL,
    descripcion VARCHAR(100) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_parametros PRIMARY KEY (id_parametro)
) COMMENT = 'Parámetros de sistema. Géneros y categorías de lectores, idiomas de publicación, géneros y subgéneros literarios, tipos de usuario';

CREATE TABLE estados(
    id_estado INTEGER AUTO_INCREMENT,
    estado VARCHAR(20) NOT NULL,
    descripcion VARCHAR(100) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_estados PRIMARY KEY (id_estado)
) COMMENT = 'Tabla de listado de estados físico de libros';

CREATE TABLE ubicaciones(
    id_ubicacion INTEGER AUTO_INCREMENT,
    ubicacion VARCHAR(20) NOT NULL,
    detalles VARCHAR(100) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_ubicaciones PRIMARY KEY (id_ubicacion)
) COMMENT = 'Tabla ubicación física para libros';

CREATE TABLE paises(
    id_pais INTEGER AUTO_INCREMENT,
    pais VARCHAR(50) NOT NULL,
    nacionalidad VARCHAR(50) NULL,
    iso2 CHAR(2) NOT NULL,
    iso3 CHAR(3) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_paises PRIMARY KEY (id_pais)
) COMMENT = 'Tabla de paises y nacionalidades para asociar a autor, editorial y personas';

CREATE TABLE comunas(
    id_comuna INTEGER AUTO_INCREMENT,
    codigo_comuna CHAR(5) NOT NULL,
    comuna VARCHAR(50) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_comunas PRIMARY KEY (id_comuna)
) COMMENT = 'Tabla de comunas de Chile de acuerdo a SUBDERE para asociar a direccion';

CREATE TABLE tipos_direccion(
    id_tipo_direccion INTEGER AUTO_INCREMENT,
    tipo_direccion VARCHAR(20) NOT NULL,
    descripcion VARCHAR(100) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_tipos_direccion PRIMARY KEY (id_tipo_direccion)
) COMMENT = 'Tabla de tipos de dirección';

CREATE TABLE direcciones(
    id_direccion INTEGER AUTO_INCREMENT,
    parametro INTEGER NOT NULL,
    comuna INTEGER NULL,
    calle VARCHAR(50) NOT NULL,
    numero VARCHAR(5) NULL,
    departamento VARCHAR(5) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_direcciones PRIMARY KEY (id_direccion),
    CONSTRAINT fk_direcciones_parametros FOREIGN KEY (parametro) REFERENCES parametros(id_parametro),
    CONSTRAINT fk_direcciones_comunas FOREIGN KEY (comuna) REFERENCES comunas(id_comuna)
) COMMENT = 'Tabla de direcciones para asociar a editoriales y personas';

CREATE TABLE bibliotecas(
    id_biblioteca INTEGER AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    web VARCHAR(255) NULL,
    telefono VARCHAR(15) NULL,
    correo VARCHAR(255) NULL,
    direccion INTEGER NULL,

    CONSTRAINT pk_bibliotecas PRIMARY KEY (id_biblioteca),
    CONSTRAINT fk_bibliotecas_direcciones FOREIGN KEY (direccion) REFERENCES direcciones(id_direccion)
) COMMENT = 'Tabla de bibliotecas';

CREATE TABLE editoriales(
    id_editorial INTEGER AUTO_INCREMENT,
    pais INTEGER NOT NULL,
    direccion INTEGER NULL,
    editorial VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NULL,
    correo VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_editoriales PRIMARY KEY (id_editorial),
    CONSTRAINT fk_editoriales_paises FOREIGN KEY (pais) REFERENCES paises(id_pais),
    CONSTRAINT fk_editoriales_direcciones FOREIGN KEY (direccion) REFERENCES direcciones(id_direccion)
) COMMENT = 'Tabla de casas editoriales de libros, asociadas a libros mediante publicacio';

CREATE TABLE autores(
    id_autor INTEGER AUTO_INCREMENT,
    pais INTEGER NULL,
    nombre VARCHAR(100) NULL,
    pseudonimo VARCHAR(25) NULL,
    fecha_nacimiento DATE NULL,
    fecha_defuncion DATE NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_autores PRIMARY KEY (id_autor),
    CONSTRAINT fk_autores_paises FOREIGN KEY (pais) REFERENCES paises(id_pais)
) COMMENT = 'Tabla de autores de libros';

CREATE TABLE publicaciones(
    id_publicacion INTEGER AUTO_INCREMENT,
    editorial INTEGER NULL,
    idioma INTEGER NULL,
    publicacion VARCHAR(25) NULL,
    fecha_publicacion DATE NULL,
    isbn CHAR(17) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_publicaciones PRIMARY KEY (id_publicacion),
    CONSTRAINT fk_publicaciones_editoriales FOREIGN KEY (editorial) REFERENCES editoriales(id_editorial),
    CONSTRAINT fk_publicaciones_parametros FOREIGN KEY (idioma) REFERENCES parametros(id_parametro)
) COMMENT = 'Tabla de publicaciones de libros por editorial';

CREATE TABLE libros(
    id_libro INTEGER AUTO_INCREMENT,
    autor INTEGER NOT NULL,
    subgenero INTEGER NOT NULL,
    publicacion INTEGER NOT NULL,
    biblioteca INTEGER NOT NULL,
    titulo VARCHAR(100) NULL,
    paginas INTEGER NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_libros PRIMARY KEY (id_libro),
    CONSTRAINT fk_libros_autores FOREIGN KEY (autor) REFERENCES autores(id_autor),
    CONSTRAINT fk_libros_parametros FOREIGN KEY (subgenero) REFERENCES parametros(id_parametro),
    CONSTRAINT fk_libros_publicaciones FOREIGN KEY (publicacion) REFERENCES publicaciones(id_publicacion),
    CONSTRAINT fk_libros_bibliotecas FOREIGN KEY (biblioteca) REFERENCES bibliotecas(id_biblioteca)
) COMMENT = 'Tabla de libros';

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
) COMMENT = 'Tabla de usuarios de sistema. Administradores de bibliotecas y lectores';

CREATE TABLE direcciones_usuarios(
    id_direccion_usuario INTEGER AUTO_INCREMENT,
    direccion INTEGER NOT NULL,
    usuario INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_direccionesusuarios PRIMARY KEY (id_direccion_usuario),
    CONSTRAINT fk_direccionesusuarios_direcciones FOREIGN KEY (direccion) REFERENCES direcciones(id_direccion),
    CONSTRAINT fk_direccionesusuarios_usuarios FOREIGN KEY (usuario) REFERENCES usuarios(id_usuario)
) COMMENT = 'Tabla auxiliar de direcciones de usuarios';

CREATE TABLE bibliotecarios(
    id_bibliotecario INTEGER AUTO_INCREMENT,
    usuario INTEGER NOT NULL,
    tipo_usuario INTEGER NOT NULL,
    contrasena CHAR(60) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_bibliotecarios PRIMARY KEY (id_bibliotecario),
    CONSTRAINT fk_bibliotecarios_usuarios FOREIGN KEY (usuario) REFERENCES usuarios(id_usuario),
    CONSTRAINT fk_bibliotecarios_parametros FOREIGN KEY (tipo_usuario) REFERENCES parametros(id_parametro)
) COMMENT = 'Tabla de usuarios de tipo bibliotecario, gestionan libros, lectores y préstamos de la bilioteca';

CREATE TABLE lectores(
    id_lector INTEGER AUTO_INCREMENT,
    usuario INTEGER NOT NULL,
    categoria INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_lectores PRIMARY KEY (id_lector),
    CONSTRAINT fk_lectores_usuarios FOREIGN KEY (usuario) REFERENCES usuarios(id_usuario),
    CONSTRAINT fk_lectores_parametros FOREIGN KEY (categoria) REFERENCES parametros(id_parametro)
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

ALTER TABLE usuarios ADD UNIQUE(rut);
ALTER TABLE usuarios ADD UNIQUE(correo);
ALTER TABLE usuarios ADD CONSTRAINT correo_unico UNIQUE (correo);