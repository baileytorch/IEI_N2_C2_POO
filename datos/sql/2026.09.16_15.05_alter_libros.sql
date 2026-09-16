ALTER TABLE libros DROP FOREIGN KEY fk_libros_generos;
ALTER TABLE libros DROP COLUMN genero;
ALTER TABLE libros subgenero INTEGER NOT NULL;
ALTER TABLE libros ADD CONSTRAINT fk_libros_subgeneros FOREIGN KEY (subgenero) REFERENCES subgeneros(id_subgenero);