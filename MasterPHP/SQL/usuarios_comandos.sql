# comandos de la tabla usuarios

#drop database blog_master; #eliminar database
create database blog_master; # crear database
use blog_master; #seleccionar database

CREATE TABLE usuarios (
    id int auto_increment not null,
    name varchar(100) not null,
    lastName varchar(100) not null,
    email varchar(255) not null,
    password varchar(255) not null,
    date_at date null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE categorias (
    id int auto_increment,
    categoria varchar(100) not null,
    CONSTRAINT pk_categorias PRIMARY KEY(id) 
)ENGINE=InnoDb;

CREATE TABLE posts (
    id int auto_increment not null,
    usuario_id int,
    categoria_id int,
    title varchar(255) not null,
    description MEDIUMTEXT null,
    date_at date not null,

    CONSTRAINT pk_posts PRIMARY KEY(id),
    
    # relacion posts + usuario(id)
    CONSTRAINT fk_posts_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    
    # relacion posts + categorias(id)
    CONSTRAINT fk_posts_categoria FOREIGN KEY (categoria_id) REFERENCES categorias(id)
)ENGINE=InnoDb;


alter table usuarios modify column fecha date null;

drop table usuarios;

INSERT INTO usuarios VALUES (null, 'Jared7', 'Latorre', 'jared7@gmail.com','marcha', curdate());

SELECT * FROM usuarios WHERE email = 'jared@gmail.com';

SELECT nombre, apellido, fecha FROM usuarios WHERE YEAR(fecha) < 2019 OR NOT ISNULL(fecha);

SELECT * FROM usuarios; # where id=1;

SELECT id, nombre FROM usuarios ORDER BY nombre desc;

SELECT * FROM usuarios WHERE (YEAR(fecha) % 2 != 0);

SELECT UPPER(nombre), apellido FROM usuarios WHERE (length(nombre) > 5) AND YEAR(fecha) < 2022;

SELECT email, (7%2) FROM usuarios;

SELECT id, nombre, email, (id+27) AS suma FROM usuarios ORDER BY suma desc;

SELECT id, nombre FROM usuarios ORDER BY nombre asc;

SELECT id, nombre, email FROM usuarios ORDER BY id DESC;

SELECT id, nombre FROM usuarios ORDER BY nombre asc limit 4,3;

# select propiedades de la tabla
SELECT VERSION() FROM usuarios;
SELECT USER() FROM usuarios;
SELECT DISTINCT USER() FROM usuarios;

INSERT INTO usuarios values (null, 'admin', 'lopez','admin@admin.com', '654987', curdate());

UPDATE usuarios SET email='rosa@rosa.com' WHERE id='3';
UPDATE usuarios SET fecha=curtime(), apellido='cero' WHERE id=1;

DELETE FROM usuarios WHERE id=8;
DELETE FROM usuarios WHERE email = 'jared0@gmail.com';

SELECT * FROM usuarios;

SELECT email FROM usuarios WHERE email LIKE '%gmail.com';

## Practica sin ver
SELECT * FROM usuarios;

INSERT INTO usuarios VALUES (null,'admon','admon','admon@dumy.com','123456',current_date());

UPDATE usuarios SET fecha='2022-01-08' WHERE id="2";

UPDATE usuarios SET apellido='fourth' WHERE id=4;

UPDATE usuarios SET apellido='third' WHERE id=3;

UPDATE usuarios SET apellido='first' WHERE email='jared1@gmail.com';

UPDATE usuarios SET apellido='fiveth', password='quinto', fecha='2023-08-14' WHERE id='5';

DELETE FROM usuarios WHERE id='6';

SHOW DATABASES;

USE blog_master;

SHOW TABLES;

DESC usuarios;
DESC posts;
DESC categorias;

ALTER TABLE posts MODIFY column id int;

INSERT INTO categorias VALUES (null,'MARVEL');
INSERT INTO categorias VALUES (null,'DC COMICS');
INSERT INTO categorias VALUES (null,'ANIMATE');

SELECT * FROM categorias;
SELECT * FROM usuarios;
SELECT * FROM posts;

TRUNCATE usuarios;

DROP TABLE usuarios;

INSERT INTO posts VALUES (null, 5, 3, 'chanchi feliz','Hola mundo desde SQL subconsulta', curdate());
INSERT INTO posts VALUES (null, 3, 3, 'magneto','poder de manejar el hierro a voluntad',curdate());
INSERT INTO posts VALUES (null, 3, 3, 'profesor x','charlis francis xavier',curdate());
INSERT INTO posts VALUES (null, 3, 3, 'mystique','jenifer lawrens',curdate());

UPDATE posts SET descripcion='heroe mundial sin poderes pero con plata' WHERE id='6';

UPDATE categorias SET nombre='X-MEN' WHERE id=3;

SELECT COUNT(titulo) FROM posts GROUP BY categoria_id;

SELECT COUNT(titulo) AS 'cantidad de posts', categoria_id AS categoria FROM posts GROUP BY categoria_id;

SELECT COUNT(titulo) AS 'Numero de posts', categoria_id FROM posts GROUP BY categoria_id HAVING COUNT(titulo) >= 5;

SELECT AVG(id) 'promedio de posts' FROM posts;

SELECT MAX(id) AS 'maximo id', titulo FROM posts;

SELECT SUM(id) AS 'suma de id' FROM posts;

USE blog_master;
INSERT INTO usuarios VALUES (null, 'lalala', 'lalala', 'lalala@lalala.com','lalala', curdate());
SELECT * FROM usuarios;
UPDATE usuarios SET nombre='super', apellido='super', email='super@super.com', password='super', fecha=curdate() WHERE id=3;

# subconsultas
SELECT * FROM usuarios 
WHERE id IN (select usuario_id from posts);

SELECT * FROM usuarios 
WHERE id NOT IN (select usuario_id from posts);

SELECT * FROM posts;
SELECT nombre, apellido FROM usuarios WHERE id IN (SELECT usuario_id FROM posts WHERE titulo LIKE '%man');

SELECT * FROM categorias;

SELECT titulo FROM posts WHERE categoria_id
IN (SELECT id FROM categorias WHERE nombre='marvel');

SELECT * FROM categorias;
UPDATE posts SET categoria_id='2' WHERE id=4; 

SELECT * FROM categorias WHERE id IN (SELECT categoria_id FROM posts GROUP BY categoria_id HAVING COUNT(categoria_id) >=5);

SELECT * FROM usuarios WHERE id IN 
(SELECT usuario_id FROM posts WHERE dayofweek(fecha)=3);

SELECT nombre FROM usuarios WHERE id IN 
(SELECT usuario_id FROM posts GROUP BY usuario_id ORDER BY COUNT(id) DESC) LIMIT 1;

SELECT id, nombre, email FROM usuarios;
SELECT id, nombre, email FROM usuarios WHERE id IN (SELECT usuario_id FROM posts);

SELECT usuario_id, COUNT(id) FROM posts GROUP BY usuario_id ORDER BY COUNT(id);

SELECT nombre FROM usuarios WHERE id =
(SELECT usuario_id, COUNT(id) FROM posts GROUP BY usuario_id ORDER BY COUNT(id) DESC LIMIT 1 );

SELECT * FROM categorias WHERE id IN 
(SELECT categoria_id FROM posts);

INSERT INTO categorias 
VALUES (NULL, 'nintendo');

UPDATE categorias SET nombre='family' WHERE id=5;

SELECT * FROM categorias 
WHERE id NOT IN 
(SELECT categoria_id FROM posts);

# multiconsultas y join

desc usuarios; # id nombre apellido email password fecha
desc posts; # id usuario_id categoria_id titulo descripcion fecha
desc categorias; # id nombre

# todos los datos
select * from posts, usuarios, categorias;

# consulta a multitablas
SELECT u.id , u.nombre as 'User', p.titulo as 'Hero', p.descripcion as 'Secret person',  c.nombre as 'Company', p.fecha as 'Date'
FROM posts p, usuarios u, categorias c
WHERE p.usuario_id = u.id AND p.categoria_id = c.id ORDER BY u.id;

SELECT usuarios.id , usuarios.nombre as 'usuario', posts.titulo as 'Super', posts.descripcion as 'identidad secreta',  categorias.nombre as 'Inc', posts.fecha
FROM posts, usuarios, categorias
WHERE posts.usuario_id = usuarios.id AND posts.categoria_id = categorias.id ORDER BY usuarios.id;

# ejercicios
use blog_master;

SELECT c.nombre, COUNT(p.id) 
FROM categorias c, posts p 
WHERE p.categoria_id = c.id GROUP BY p.categoria_id;

SELECT u.email, count(p.id) AS 'total de posts' FROM usuarios u, posts p WHERE u.id = p.usuario_id GROUP BY u.email;
SELECT u.email, count(titulo) FROM usuarios u, posts p WHERE p.usuario_id = u.id group by p.usuario_id;

desc usuarios;
desc posts;
desc categorias;
select * from usuarios;
select * from posts;
select * from categorias;

select * from usuarios;
update usuarios set email='wizard@wizard.com' WHERE id=1;

# inner join
SELECT u.id, u.nombre AS 'User', p.categoria_id, c.nombre AS 'categoria'
FROM posts p
INNER JOIN usuarios u ON p.usuario_id = u.id
INNER JOIN categorias c ON p.categoria_id = c.id group by p.usuario_id;

SELECT p.id, p.titulo, u.nombre AS 'User', c.nombre AS 'categoria'
FROM posts p
INNER JOIN usuarios u ON p.usuario_id = u.id
INNER JOIN categorias c ON p.categoria_id = c.id;

SELECT u.id AS user_id, p.titulo, p.descripcion, u.nombre AS 'User'
FROM posts p
INNER JOIN usuarios u ON p.usuario_id = u.id;

# Left join diferencias
SELECT categorias.nombre, COUNT(posts.id)
FROM categorias
LEFT JOIN posts ON posts.categoria_id = categorias.id
GROUP BY posts.categoria_id;

# rigth join
SELECT categorias.nombre, COUNT(posts.id)
FROM categorias
RIGHT JOIN posts ON posts.categoria_id = categorias.id
GROUP BY posts.categoria_id;

SELECT * FROM posts;

use blog_master;

CREATE VIEW posts_por_categorias AS
SELECT c.nombre, COUNT(p.id)
FROM posts p
RIGHT JOIN categorias c ON p.categoria_id = c.id
GROUP BY p.categoria_id;

SHOW tables;

SELECT * FROM posts_por_categorias;

SELECT * FROM posts_por_categorias WHERE nombre='marvel';

# hasta aqui fue el curso, vamos por la practica




















