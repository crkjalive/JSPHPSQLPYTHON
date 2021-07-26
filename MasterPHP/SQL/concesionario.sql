#drop database concesionario;
create database if not exists concesionario;
use concesionario;

CREATE TABLE coches(
    id int auto_increment,
    modelo varchar(100) not null,
    marca varchar(50) not null,
    precio int(20) not null,
    stock int(255) not null,

    CONSTRAINT pk_coches PRIMARY KEY(id)
) ENGINE=InnoDB;

desc coches;
drop table coches;

CREATE TABLE grupos(
    id int auto_increment,
    nombre varchar(100) not null,
    ciudad varchar(100),

    CONSTRAINT pk_grupos PRIMARY KEY(id)
) ENGINE=InnoDB;

desc grupos;
drop table grupos;

CREATE TABLE personal(
    id int auto_increment PRIMARY KEY,
    grupo_id int not null,
    jefe int,
    nombre varchar(100) not null,
    apellido varchar(150),
    cargo varchar(50),
    fecha date,
    sueldo float(20,2),
    comision float(10,2),

    CONSTRAINT pk_personal PRIMARY KEY (id),
    CONSTRAINT fk_personal_grupo FOREIGN KEY(grupo_id) REFERENCES grupos(id),
    CONSTRAINT fk_personal_jefe FOREIGN KEY(jefe) REFERENCES personal(id)
) ENGINE=InnoDB;

desc personal;
drop table personal;

CREATE TABLE clientes(
    id int auto_increment,
    personal_id int,
    nombre varchar(100) not null,
    ciudad varchar(150),
    gastado float(50,2),
    fecha date,

    CONSTRAINT pk_clientes PRIMARY KEY(id),
    CONSTRAINT fk_cliente_personal FOREIGN KEY(personal_id) REFERENCES personal(id)
) ENGINE=InnoDB;

desc clientes;
# drop clientes;

CREATE TABLE ventas(
    id int auto_increment,
    cliente_id int,
    coche_id int,
    cantidad int(100),
    fecha date,

    CONSTRAINT pk_ventas PRIMARY KEY(id),
    CONSTRAINT fk_ventas_cliente FOREIGN KEY(cliente_id) REFERENCES clientes(id),
    CONSTRAINT fk_ventas_coche FOREIGN KEY (coche_id) REFERENCES coches(id)
) ENGINE=InnoDB;

desc ventas;
drop table ventas;

# inserts coches
DESC coches;

INSERT INTO coches VALUES(null, 'clio', 'renault', 12000, 13);
INSERT INTO coches VALUES(null, '365i', 'mercedes benz', 20000, 5);
INSERT INTO coches VALUES(null, 'twingo','renault',8000, 8);
INSERT INTO coches VALUES(null, 'aveo','chevrolet',13000, 10);
INSERT INTO coches VALUES(null, 'land cruiser','toyota',25000, 9);
INSERT INTO coches VALUES(null, 'm8','bmw', 35000, 2);
INSERT INTO coches VALUES(null, 'veneno','lamborghini', 50000, 2);
INSERT INTO coches VALUES(null, 'noire','bugatti', 60000, 3);

UPDATE coches SET precio=35000 WHERE id=6 ;
UPDATE coches SET modelo='m8' WHERE id=5 ;
UPDATE coches SET marca='mercedes benz' WHERE id=2 ;
UPDATE coches SET stock=5 WHERE id=7 ;

SELECT * FROM coches;

# inserts grupos

DESC grupos;

INSERT INTO grupos VALUES(null, 'vendedrores a','bogotá');
INSERT INTO grupos VALUES(null, 'vendedrores b','cali');
INSERT INTO grupos VALUES(null, 'vendedrores c','medellín');
INSERT INTO grupos VALUES(null, 'vendedrores d','barranquilla');

UPDATE grupos SET nombre='vendedores a' WHERE id=1;
UPDATE grupos SET ciudad='barranquilla' WHERE id=4;

DELETE FROM grupos WHERE id=9;

SELECT * FROM grupos;

#inserts personal

DESC personal;

INSERT INTO personal VALUES(null, 1, null, 'Linus', 'Tolbars', 'ingeniero', curdate(), 1100, 1);
INSERT INTO personal VALUES(null, 2, null, 'Jared', 'Latorre', 'jefe', curdate(), 1800, 5);
INSERT INTO personal VALUES(null, 3, null, 'Bill', 'Gates', 'vendedor', curdate(), 1500, 2);
INSERT INTO personal VALUES(null, 4, null, 'Steve', 'Jobs', 'vendedor', curdate(), 2000, 2);
INSERT INTO personal VALUES(null, 2, 2, 'Kenneth', 'Latorre', 'piloto', curdate(), 3800, 5);
INSERT INTO personal VALUES(null, 3, 1, 'Christian', 'Latorre', 'biker', curdate(), 2500, 6);

DELETE FROM personal WHERE id=6;

select * from personal;
#drop table personal;

use concesionario;

#inserts clientes
desc clientes;
select * from clientes;
select * from coches;

INSERT INTO clientes VALUES(null, 1, 'construcciones diaz inc', 'Bogota', 24000, curdate());
INSERT INTO clientes VALUES(null, 1, 'imprenta ltda', 'Bogota', 40000, curdate());
INSERT INTO clientes VALUES(null, 1, 'fruteria del barrio', 'Bogota', 5000, curdate());
INSERT INTO clientes VALUES(null, 1, 'colchones sa', 'Bogota', 8000, curdate());
INSERT INTO clientes VALUES(null, 1, 'julian mejia', 'Bogota', 6000, curdate());

update clientes set gastado = 45000 WHERE id=3;

#inserts ventas
desc ventas;

INSERT INTO ventas VALUES(null, 1, 1, 2, curdate());
INSERT INTO ventas VALUES(null, 2, 2, 3, curdate());
INSERT INTO ventas VALUES(null, 3, 7, 1, curdate());
INSERT INTO ventas VALUES(null, 4, 8, 1, curdate());
INSERT INTO ventas VALUES(null, 5, 5, 1, curdate());

select * from coches;
select * from personal;
select * from grupos;
select * from clientes;
select * from ventas;

# consultas
select cantidad, nombre AS cliente from ventas, clientes WHERE ventas.cliente_id = clientes.id; # compras, cliente
select marca, modelo, cantidad, nombre AS cliente from ventas, clientes, coches WHERE ventas.cliente_id = clientes.id AND ventas.coche_id = coches.id; # marca modelo cantidas cliente
 
select * from personal;
UPDATE personal SET sueldo = 90000 WHERE id = 4; 
UPDATE personal SET comision = 0.6 WHERE sueldo >= 50000;

SELECT * FROM coches;
UPDATE coches SET precio = precio * 1.05; # cambio no seguro

SELECT * FROM personal;
UPDATE personal SET cargo = 'Jefe' WHERE cargo != 'Vendedores';
UPDATE personal SET cargo = 'Vendedor' WHERE cargo != 'Jefe';

Select * from personal where fecha < '2021-06-01'; 
select * from personal;
update personal set fecha = '2022-05-01' where id = 6;

SELECT nombre, DATEDIFF(CURDATE(), fecha) AS 'DIAS' FROM personal; #diferencia en dias

SELECT CONCAT(nombre, ' ', apellido) AS 'Nombre Completo', fecha AS Registro, dayname(fecha) AS DIA FROM personal;

SELECT * from personal;
SELECT nombre, sueldo, cargo from personal where cargo = 'Vendedores';

select * from coches;
select marca, modelo from coches where marca LIKE '%a%' AND modelo LIKE 'n%';
SELECT marca, modelo FROM coches WHERE marca NOT LIKE '%a%';

SELECT * FROM coches WHERE marca LIKE '%a%' OR modelo LIKE '%f%';

select * from personal;
select * from personal where grupo_id=2 order by sueldo desc;
desc personal;

SELECT apellido, fecha, id FROM personal ORDER BY fecha DESC limit 4;

select * from personal;
SELECT cargo, count(id) FROM personal group by cargo;

SELECT sum(sueldo) AS 'masa salarial', sum(sueldo) / 12 AS 'pagos mensuales'  FROM personal;

SELECT ceil((sueldo)) AS 'ceil', g.nombre, g.ciudad
FROM personal p 
INNER JOIN grupos g ON g.id = p.grupo_id  
GROUP BY grupo_id;

select * from coches;

select concat(marca, ' ', modelo) AS 'Coche',  sum(v.cantidad) AS 'Compro', nombre AS 'Cliente' from ventas v
inner join coches co ON co.id = v.coche_id
inner join clientes cl ON cl.id = v.cliente_id
GROUP BY v.coche_id, v.cliente_id; 

select * from clientes;

select nombre, cantidad from ventas
inner join clientes ON clientes.id = ventas.cliente_id AND ventas.cantidad > 2; 

insert into clientes values (null, 2, 'Wizard deejay', 'New Zeland', 9000, curdate());
select * from coches;
select * from ventas;
insert into ventas values (null, 6, 4, 2, curdate());

create view CL AS
select nombre,marca,modelo,precio,cantidad,(precio*cantidad) AS Total, gastado AS 'Cancelado', (precio*cantidad) - gastado AS 'Adeuda' from ventas
inner join clientes ON cliente_id = clientes.id
inner join coches ON coches.id = ventas.coche_id
where cliente_id = 6;

select * from CL;
desc CL;

SELECT cliente_id, COUNT(id) FROM ventas
GROUP BY cliente_id ORDER BY 2 DESC LIMIT 2;

SELECT c.nombre, COUNT(v.id) FROM ventas v
INNER JOIN clientes c ON c.id = v.cliente_id
GROUP BY cliente_id ORDER BY 2 DESC LIMIT 2;

select * from clientes;
select * from personal;

SELECT clientes.nombre AS 'Cliente', personal.nombre AS 'Vendedor' FROM clientes, personal WHERE personal_id IN 
(SELECT id FROM personal WHERE nombre = 'Linus' AND apellido = 'Tolbars')
group by clientes.nombre;

SELECT * FROM ventas WHERE cliente_id IN
(SELECT id FROM clientes WHERE nombre='colchones sa');
desc ventas;

CREATE VIEW CLIENTE as
SELECT v.id AS 'No pedido', cantidad, c.nombre, co.marca, co.modelo, v.fecha
FROM ventas v
INNER JOIN clientes c ON c.id = v.cliente_id
INNER JOIN coches co ON co.id = v.coche_id
WHERE v.cliente_id IN
(SELECT id FROM clientes WHERE nombre = 'colchones sa');

SELECT * FROM CLIENTE;

DESC CLIENTE;

select * from coches;
select * from ventas;
select * from cliente;

#select clientes.nombre from clientes where 
#IN (select modelo from coches where marca = "mercedes benz");
desc clientes;

SELECT * FROM clientes WHERE id IN
(SELECT cliente_id FROM ventas);

# 3 subconsultas
SELECT * FROM clientes WHERE id 
IN (SELECT cliente_id FROM ventas WHERE coche_id 
IN (SELECT id FROM coches WHERE marca LIKE '%mercedes benz%'));

# Desconstruccion
SELECT id FROM coches WHERE marca LIKE '%mercedes benz%'; #id 2
SELECT cliente_id FROM ventas WHERE coche_id
  IN (SELECT id FROM coches WHERE marca LIKE '%mercedes benz%'); # cliente_id 2

# 2	1	imprenta ltda	Bogota	40000.00	2021-06-09
# comprobacion de que si pidio n mercedes benz
select * from coches;
select * from ventas;
select * from clientes;



