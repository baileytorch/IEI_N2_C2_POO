-- Crear usuario local 'Torch' con contraseña 'mypassword'
CREATE USER 'Torch'@'localhost' IDENTIFIED BY 'mypassword';

-- Crear usuario remoto 'Torch' con contraseña 'mypassword'
CREATE USER 'Torch'@'%' IDENTIFIED BY 'mypassword';

--Conceder privilegios al usuario 'Torch' para todas las bases de datos y tablas
GRANT ALL PRIVILEGES ON *.* TO 'Torch'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'Torch'@'%' WITH GRANT OPTION;

-- Conceder privilegios para una base de datos específica (por ejemplo, 'mydatabase')
GRANT ALL PRIVILEGES ON mydatabase.* TO 'Torch'@'localhost';
GRANT ALL PRIVILEGES ON mydatabase.* TO 'Torch'@'%';

-- Aplicar los cambios de privilegios
FLUSH PRIVILEGES;
EXIT;