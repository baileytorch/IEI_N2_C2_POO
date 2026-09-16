CREATE TABLE subgeneros(
    id_subgenero INTEGER AUTO_INCREMENT,
    genero INTEGER NOT NULL,
    subgenero VARCHAR(25) NOT NULL,
    descripcion VARCHAR(255) NULL,

    CONSTRAINT pk_subgeneros PRIMARY KEY (id_subgenero),
    CONSTRAINT fk_subgeneros_generos FOREIGN KEY (genero) REFERENCES generos(id_genero)
) COMMENT = 'Tabla de sub-generos literarios.';