ALTER TABLE usuarios MODIFY correo VARCHAR(191) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE usuarios ADD UNIQUE INDEX unique_correo (correo);
AlTER TABLE parametros MODIFY descripcion TEXT;