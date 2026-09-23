INSERT INTO autores(pais,nombre,pseudonimo,fecha_nacimiento,fecha_defuncion) VALUES
((SELECT id_pais FROM paises WHERE pais = 'Chile'),'Ricardo Eliécer Neftalí Reyes Basoalto','Pablo Neruda',STR_TO_DATE('12/07/1904','%d/%m/%Y'),STR_TO_DATE('23/09/1973', '%d/%m/%Y'));

INSERT INTO autores
(pais, nombre, pseudonimo, fecha_nacimiento, fecha_defuncion)
VALUES
(
    (SELECT id_pais FROM paises WHERE pais = 'Chile'),
    'Lucila Godoy Alcayaga',
    'Gabriela Mistral',
    '1889-04-07',
    '1957-01-10'
),
(
    (SELECT id_pais FROM paises WHERE pais = 'Chile'),
    'Vicente García-Huidobro Fernández',
    'Vicente Huidobro',
    '1893-01-10',
    '1948-01-02'
),
(
    (SELECT id_pais FROM paises WHERE pais = 'Chile'),
    'Manuel Rojas Sepúlveda',
    NULL,
    '1896-01-08',
    '1973-03-11'
),
(
    (SELECT id_pais FROM paises WHERE pais = 'Chile'),
    'José Santos González Vera',
    'González Vera',
    '1897-04-24',
    '1970-02-27'
),
(
    (SELECT id_pais FROM paises WHERE pais = 'Chile'),
    'Alberto Blest Gana',
    NULL,
    '1830-05-04',
    '1920-11-09'
),
(
    (SELECT id_pais FROM paises WHERE pais = 'Chile'),
    'Baldomero Lillo Figueroa',
    'Baldomero Lillo',
    '1867-01-06',
    '1923-09-10'
),
(
    (SELECT id_pais FROM paises WHERE pais = 'Chile'),
    'María Luisa Bombal Anthes',
    'María Luisa Bombal',
    '1910-06-08',
    '1980-05-06'
),
(
    (SELECT id_pais FROM paises WHERE pais = 'Chile'),
    'Nicanor Segundo Parra Sandoval',
    'Nicanor Parra',
    '1914-09-05',
    '2018-01-23'
),
(
    (SELECT id_pais FROM paises WHERE pais = 'Chile'),
    'José Donoso Yáñez',
    'José Donoso',
    '1924-10-05',
    '1996-12-07'
),
(
    (SELECT id_pais FROM paises WHERE pais = 'Chile'),
    'Isabel Allende Llona',
    'Isabel Allende',
    '1942-08-02',
    NULL
);