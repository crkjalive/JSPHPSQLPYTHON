# Practica sobre SQL en bases de datos
# 1. crear una base da datos de un concesionario
- coches
  - id
  - modelo
  - marca
  - precio
  - stock
- vendedores
  - id
  - grupo_id
  - nombre
  - apellido
  - cargo
  - fecha_ingreso
  - sueldo
  - comision
  - jefe
- clientes
  - id
  - vendedor_id
  - nombre_cliente
  - ciudad
  - gastado
- ventas
  - id
  - cliente_id
  - coche_id
  - cantidad
  - fecha_compra
- grupo
  - id
  - nombre_grupo
  - ciudad

# 2. creacion de DML a Database 

### creacion database
~~~
CREATE DATABASE IF NOT EXISTS concesionario;
USE concesionario;
~~~

### tabla de coches
~~~
CREATE TABLE coches(
    id int auto_increment,
    modelo varchar(100) not null,
    marca varchar(50) not null,
    precio int(20) not null,
    stock int(255) not null,

    CONSTRAINT pk_coches PRIMARY KEY(id)
) ENGINE=InnoDB;

desc coches;
#drop table coches;
~~~

### tabla de grupos
~~~
CREATE TABLE grupos(
    id int auto_increment not null,
    nombre varchar(100) not null,
    ciudad varchar(100),

    CONSTRAINT pk_grupos PRIMARY KEY(id)
) ENGINE=InnoDB;

desc grupos;
#drop table grupos;
~~~

### tablas del personal
~~~
CREATE TABLE personal(
    id int auto_increment not null,
    grupo_id int not null,
    jefe int,
    nombre varchar(100) not null,
    apellido varchar(150),
    cargo varchar(50),
    fecha date,
    sueldo float(20,2),
    comision float(10,2),

    CONSTRAINT pk_personal PRIMARY KEY(id),
    CONSTRAINT fk_personal_grupo FOREIGN KEY(grupo_id) REFERENCES grupos(id),
    CONSTRAINT fk_personal_jefe FOREIGN KEY(jefe) REFERENCES personal(id)
) ENGINE=InnoDB;

desc personal;
# drop table personal;
~~~

### tablas de clientes
~~~
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
~~~

### tabla de ventas
~~~
CREATE TABLE ventas(
    id int auto_increment,
    cliente_id int not null,
    coche_id int not null,
    cantidad int(100),
    fecha date,

    CONSTRAINT pk_ventas PRIMARY KEY(id),
    CONSTRAINT fk_ventas_cliente FOREIGN KEY(cliente_id) REFERENCES clientes(id),
    CONSTRAINT fk_ventas_coche FOREIGN KEY (coche_id) REFERENCES coches(id)
) ENGINE=InnoDB;

desc ventas;
# drop table ventas;
~~~

# 3. llenado de tablas
### tabla de coches 
- id modelo marca precio stock
~~~
DESC coches;

INSERT INTO coches VALUES(null, 'clio', 'renault', 12000, 13);
INSERT INTO coches VALUES(null, '365i', 'mercedezs benz', 13000, 15);
INSERT INTO coches VALUES(null, 'twingo','renault',8000, 5);
INSERT INTO coches VALUES(null, 'aveo','chevrolet',11000, 10);
INSERT INTO coches VALUES(null, 'land cruiser','toyota',20000, 9);
INSERT INTO coches VALUES(null, 'm8','bmw', 205000, 2);
INSERT INTO coches VALUES(null, 'veneno','lamborghini', 205000, 2);
INSERT INTO coches VALUES(null, 'noire','bugatti', 500000, 3);

UPDATE coches SET precio=65000 WHERE id=7 ;
UPDATE coches SET modelo='m8' WHERE id=5 ;
UPDATE coches SET marca='lamborghini' WHERE id=7 ;
UPDATE coches SET stock=5 WHERE id=7 ;

SELECT * FROM coches;
~~~

### tablas de grupos
- id nombre ciudad
~~~
DESC grupos;

INSERT INTO grupos VALUES(null, 'vendedrores a','bogotá');
INSERT INTO grupos VALUES(null, 'vendedrores b','cali');
INSERT INTO grupos VALUES(null, 'vendedrores c','medellín');
INSERT INTO grupos VALUES(null, 'vendedrores d','barranquilla');

UPDATE grupos SET nombre='vendedores a' WHERE id=1;
UPDATE grupos SET ciudad='barranquilla' WHERE id=4;

DELETE FROM grupos WHERE id=9;

SELECT * FROM grupos;
~~~

### tabla de personal
- id grupo_id jefe nombre apellido cargo fecha sueldo comision
~~~
DESC personal;

INSERT INTO personal VALUES(null, 1, null, 'Linus', 'Tolbars', 'ingeniero', CURDATE(), 1100, 1);
INSERT INTO personal VALUES(null, 2, null, 'Jared', 'Latorre', 'jefe', CURDATE(), 1800, 5);
INSERT INTO personal VALUES(null, 3, null, 'Bill', 'Gates', 'vendedor', CURDATE(), 1500, 2);
INSERT INTO personal VALUES(null, 4, null, 'Steve', 'Jobs', 'vendedor', CURDATE(), 2000, 2);
INSERT INTO personal VALUES(null, 2, 2, 'Kenneth', 'Latorre', 'piloto', CURDATE(), 3800, 5);
INSERT INTO personal VALUES(null, 3, 1, 'Christian', 'Latorre', 'biker', CURDATE(), 2500, 6);

DELETE FROM personal WHERE id=6;

select * from personal;
#drop table personal;
~~~

### tabla clientes
- id personal_id nombre ciudad gastado fecha
~~~
INSERT INTO clientes VALUES(null, 1, 'construcciones diaz inc', 'Bogota', 24000, CURDATE());
INSERT INTO clientes VALUES(null, 1, 'imprenta ltda', 'Bogota', 40000, CURDATE());
INSERT INTO clientes VALUES(null, 1, 'fruteria del barrio', 'Bogota', 5000, CURDATE());
INSERT INTO clientes VALUES(null, 1, 'colchones sa', 'Bogota', 8000, CURDATE());
INSERT INTO clientes VALUES(null, 1, 'julian mejia', 'Bogota', 6000, CURDATE());
~~~

### tabla ventas
- id cliente_id coche_id cantidad fecha
~~~
INSERT INTO ventas VALUES(null, 1, 1, 2, CURDATE());
INSERT INTO ventas VALUES(null, 2, 2, 3, CURDATE());
INSERT INTO ventas VALUES(null, 3, 7, 1, CURDATE());
INSERT INTO ventas VALUES(null, 4, 8, 1, CURDATE());
INSERT INTO ventas VALUES(null, 5, 5, 1, CURDATE());
~~~

# 4. consultas
> SELECT cantidad, nombre AS cliente FROM ventas, clientes WHERE ventas.cliente_id = clientes.id;

|cantidad | cliente|
|---:|---|
|2	| construcciones diaz inc|
|2	| imprenta ltda|
|1	| fruteria del barrio|
|1	| colchones sa|
|1	| julian mejia|

> SELECT marca, modelo, cantidad, nombre AS cliente FROM ventas, clientes, coches WHERE ventas.cliente_id = clientes.id AND ventas.coche_id = coches.id;

|marca | modelo | cantidad | cliente|
|---:|---|---:|---|
|renault | clio | 2 | construcciones diaz inc|
|mercedes | benz 365i | 2 | imprenta ltda |
|lamborghini | veneno | 1 | fruteria del barrio|
|bugatti | noire | 1 | colchones sa |
|toyota | land cruiser | 1 | julian mejia|

## Ejercicios
2. modificar la comision de los vendedores y ponerla al 2% si se gana más de 50000

> UPDATE personal SET comision = 0.5 WHERE id = 6 and sueldo >= 50000;

3. incrementar el precio de los coches en 5%

> UPDATE coches SET precio = precio * 1.05;

4. sacar los vendedores con fecha posterior al 1 de junio del 2021

> SELECT * FROM personal WHERE fecha < '2021-06-01'; 

5. listar el nombre de personal con el numero de dias que lleva en el concesionario

> SELECT nombre, DATEDIFF(CURDATE(), fecha) AS 'DIAS' FROM personal;

6. visualizar el nombre y apellidos en una misma columna, y su fecha de registro, y que dia era de la semana cuando se registraron

> SELECT CONCAT(nombre, ' ', apellido) AS 'Nombre Completo', fecha AS Registro, dayname(fecha) AS DIA FROM personal;

|Nombre Completo | Registro | DIA|
|---|---|---|
|Linus Tolbars	| 2020-06-01 |Monday|
|Jared Latorre	| 2020-05-01 |Friday|
|Bill Gates  | 2020-06-01 |Monday|
|Steve Jobs	| 2021-06-09 |Wednesday|
|Kenneth Latorre	| 2021-06-09 |Wednesday|
|Christian Latorre	| 2022-05-01 |Sunday|

7. mostrar el nombre y el salario del personal con cargo de vendedor

> SELECT nombre, sueldo, cargo from personal where 
cargo = 'Vendedores';

8. visualizar todos los coches donde la marca contenga la letra a, modelo por letra n

> SELECT marca, modelo FROM coches WHERE marca LIKE '%a%' AND modelo LIKE 'n%';

|marca | modelo|
|---|---|
|bugatti | noire|

> SELECT marca, modelo FROM coches WHERE marca NOT LIKE '%a%';

|marca | modelo|
|---|---|
|mercedes | benz 365i|
|chevrolet | aveo|
|bmw | m8|

> SELECT * FROM coches WHERE marca LIKE '%a%' OR modelo LIKE '%f%';

|id | modelo| marca | precio | stock|
|---|---|---|---|---|
|1 | clio | renault | 12600 |13|
|3 | twingo | renault | 8400  |8|
|5 | land cruiser | toyota | 26250 | 9|
|7 | veneno | lamborghini | 52500 | 2|
|8 | noire | bugatti | 63000 | 3|

9. mostrar todos los vendedores del grupo 2, ordenados por salario

> SELECT * FROM personal WHERE grupo_id=2 ORDER BY sueldo DES;

|id | grupo_id | jefe | nombre | apellido | cargo | fecha | sueldo | comision|
|---|---|---|---|---|---|---|---|---|
|2 | 2 | | Jared | Latorre | Vendedor | 2020-05-01 |  20000.00 | 5.00|
|5 | 2 | 2 | Kenneth | Latorre | Vendedor | 2021-06-09 | 20000.00 | 5.00|

10. visualizar el apellidos del personal, fecha, grupo ordenados por fecha desc, y mostrar los 4 ultimos

> SELECT apellido, fecha, id FROM personal ORDER BY fecha DESC limit 4;

|apellido|fecha|id|
|---|---|---|
|Latorre | 2022-05-01 | 6 |
|Jobs |  2021-06-09 | 4 |
|Latorre | 2021-06-09 | 5 |
|Tolbars | 2020-06-01 | 1 |

11. visualizar los cargos y el numero de vendedores por cargo

> SELECT cargo, count(id) AS cantidad FROM personal group by cargo;

|cargo | cantidad|
|---|---|
|Jefe | 1|
|Vendedor | 5|

12. conseguir la masa salarial del concesioario (anual)

> SELECT sum(sueldo) AS 'masa salarial' from personal;

> SELECT sum(sueldo) AS 'masa salarial', sum(sueldo) / 12 AS 'pagos mensuales'  FROM personal;

13. sacar la media de sueldos entre el personal por grupo, y mostrar el grupo

> SELECT avg(sueldo), g.nombre, g.ciudad
FROM personal p
INNER JOIN grupos g ON g.id = p.grupo_id
GROUP BY grupo_id;


|avg(sueldo)| grupo | ciudad|
|---|---|---|
|50000.000000 | vendedrores a | bogotá|
|20000.000000 | vendedrores b | cali|
|50000.000000 | vendedrores c | medellín|
|90000.000000 | vendedrores d | barranquilla|

> SELECT ceil((sueldo)), g.nombre, g.ciudad
FROM personal p
INNER JOIN grupos g ON g.id = p.grupo_id
GROUP BY grupo_id;

|avg(sueldo)| grupo | ciudad|
|---|---|---|
|50000 | vendedrores a | bogotá|
|20000 | vendedrores b | cali|
|50000 | vendedrores c | medellín|
|90000 | vendedrores d | barranquilla|

14. visualizar las unidades vendidas de cada coche a cada cliente, mostrando el nombre del producto, numero de cliente y la suma de unidades

> select concat(marca, ' ', modelo) AS 'Coche',  sum(v.cantidad) AS 'Compro', nombre AS 'Cliente' from ventas v
inner join coches co ON co.id = v.coche_id
inner join clientes cl ON cl.id = v.cliente_id
GROUP BY v.coche_id, v.cliente_id;

|Coche | Compro | Cliente|
|---|---|---|
|renault clio | 2 | construcciones diaz inc|
|mercedes benz 365i | 2 | imprenta ltda|
|lamborghini veneno | 1 | fruteria del barrio|
|bugatti noire | 1 | colchones sa|
|toyota land cruiser | 1 | julian mejia|

15. mostrar los cliente que mas pedidos han hecho pedidos, y mostrar cuantos hicieron

> SELECT c.nombre, COUNT(v.id) FROM ventas v
INNER JOIN clientes c ON c.id = v.cliente_id
GROUP BY cliente_id ORDER BY 2 DESC LIMIT 2;

___

### mi consulta
100. buscar un cliente, coche, precio, gastado, debe

> select nombre,marca,modelo,precio,cantidad,(precio*cantidad) AS Total, gastado AS 'Cancelado', (precio*cantidad) - gastado AS 'Adeuda' from ventas
inner join clientes ON cliente_id = clientes.id
inner join coches ON coches.id = ventas.coche_id
where cliente_id = 6;

|nombre|marca|modelo|precio|cantidad|Total|Cancelado|Adeuda|
|---|---|---|---|---|---|---|---|
|Wizard deejay|chevrolet|aveo|13650|2|27300|9000.00|18300.00|

101. con vista para consultar mas rapido

~~~
CREATE VIEW CL AS
SELECT nombre,marca,modelo,precio,cantidad,(precio*cantidad) AS Total, gastado AS 'Cancelado', (precio*cantidad) - gastado AS 'Adeuda' FROM ventas
INNER JOIN clientes ON cliente_id = clientes.id
INNER JOIN coches ON coches.id = ventas.coche_id
WHERE cliente_id = 6;

DESC CL;

SELECT * FROM CL;
~~~

|nombre|marca|modelo|precio|cantidad|Total|Cancelado|Adeuda|
|---|---|---|---|---|---|---|---|
|Wizard deejay|chevrolet|aveo|13650|2|27300|9000.00|18300.00|

___

16. obtener listado de clientes atendidos por el vendedor

> SELECT clientes.nombre AS 'Cliente', personal.nombre AS 'Vendedor' FROM clientes, personal WHERE personal_id IN 
(SELECT id FROM personal WHERE nombre = 'Linus' AND apellido = 'Tolbars')
group by clientes.nombre;

| Cliente | Vendedor|
|-:|:-|
| construcciones diaz inc | Linus|
| imprenta ltda | Linus|
| fruteria del barrio | Linus|
| colchones sa  | Linus|
| julian mejia  | Linus|

17. obtener listado de ventas, realizados por 'wizard deejay'

> SELECT * FROM ventas WHERE cliente_id IN
(SELECT id FROM clientes WHERE nombre='colchones sa');

| id | cliente_id | coche_id | cantidad | fecha |
|---|---|---|---|---|
| 4 | 4 | 8 | 1 | 2021-06-09|

### lo cual no nos dice nada
vamos a mostrar los campos con los nombres reales

~~~
CREATE VIEW CLIENTE as
SELECT v.id AS 'No pedido', cantidad, c.nombre, co.marca, co.modelo, v.fecha
FROM ventas v
INNER JOIN clientes c ON c.id = v.cliente_id
INNER JOIN coches co ON co.id = v.coche_id
WHERE v.cliente_id IN
(SELECT id FROM clientes WHERE nombre = 'colchones sa');

SELECT * FROM CLIENTE;

DESC CLIENTE;
~~~

|No pedido|cantidad|nombre|marca|modelo|fecha|
|---|---|---|---|---|---|
|4 |1|colchones sa|bugatti|noire|2021-06-09|

18. listado de clientes con pedido de un coche especifico (mercedes benz)

- 3 subconsultas

~~~
SELECT * FROM clientes WHERE id IN 
(SELECT cliente_id FROM ventas WHERE coche_id IN 
  (SELECT id FROM coches WHERE marca LIKE '%mercedes benz%')
  );

~~~


# Ubuntu
### Consulta en Mysql phpmyadmin
~~~
CREATE VIEW cliente_debe AS 
SELECT ventas.cantidad, coches.precio, coches.precio * ventas.cantidad AS 'Precio Total', 
coches.modelo, coches.marca, clientes.id, clientes.nombre, clientes.gastado, (coches.precio * ventas.cantidad)- clientes.gastado AS 'Debe' 
FROM `ventas` 
INNER JOIN clientes ON cliente_id = clientes.id
INNER JOIN coches ON coche_id = coches.id;
~~~

| cantidad | precio | Precio Total | modelo | marca | id | nombre | gastado | Debe | 
|---|---|---|---|---|---|---|---|---|
| 2 | 12000 | 24000 | clio | renault | 1 | construcciones diaz inc | 24000.00 | 0.00|
| 3 | 20000 | 60000 | 365i | mercedes benz | 2 | imprenta ltda | 40000.00 | 20000.00|
| 1 | 50000 | 50000 | veneno | lamborghini | 3 | fruteria del barrio | 5000.00 | 45000.00|
| 1 | 60000 | 60000 | noire |  bugatti | 4 | colchones sa | 8000.00 | 52000.00|
| 1 | 25000 | 25000 | land | ruiser  toyota | 5 | julian mejia | 6000.00 | 19000.00|


19. Obtener los vendedores con dos o más clientes
~~~
SELECT * FROM personal WHERE id IN 
  (SELECT personal_id FROM clientes GROUP BY personal_id HAVING COUNT(id)>=2);
~~~

20. seleccionar el grupo en el que trabaja el vendedor con mayor salario y mostrar el nombre del grupo

1. primera parte
~~~
SELECT * FROM grupos WHERE id IN
(SELECT grupo_id FROM personal);
~~~

|id|nombre|ciudad|
|-|-|-|
| 1 | vendedrores a | bogotá |
| 2 | vendedrores b | cali |
| 3 | vendedrores c | medellín |
| 4 | vendedrores d | barranquilla |

2. segunda parte

~~~
SELECT * FROM grupos WHERE id IN
(SELECT grupo_id FROM personal WHERE sueldo = (
  SELECT MAX(sueldo) FROM personal));
~~~

|id|nombre|ciudad|
|-|-|-|
| 2 | vendedrores b | cali |

3. tercera parte comprobamos

~~~
SELECT * FROM personal ORDER BY sueldo DESC limit 1;
~~~

|id | grupo_id | jefe | nombre | apellido | cargo | fecha | sueldo | comision | 
|-|-|-|-|-|-|-|-|-|
| 5 | 2 | 2 |  Kenneth |  Latorre |  piloto | 2021-06-21 | 3800.00 | 5.00 |
| 6 | 3 | 1 |  Christian |  Latorre |  biker |  2021-06-21 | 2500.00 | 6.00 |
| 4 | 4 | NULL | Steve |  Jobs | vendedor | 2021-06-21 | 2000.00 | 2.00 |
| 2 | 2 | NULL | Jared |  Latorre |  jefe | 2021-06-21 | 1800.00 | 5.00 |
| 3 | 3 | NULL | Bill | Gates |  vendedor | 2021-06-21 | 1500.00 | 2.00 |
| 1 | 1 | NULL | Linus |  Tolbars |  ingeniero |  2021-06-21 | 1100.00 | 1.00 | 

21. obtener los nombres y ciudades de los clientes con encargos con mas de 3 unidades 

~~~
SELECT nombre, ciudad FROM clientes WHERE id IN 
(SELECT cliente_id FROM ventas WHERE cantidad >= 3);
~~~

|nombre|ciudad|
|-|-|
|imprenta ltda|bogotá|

22. mostrar listado de clientes (numero de cliente y el nombre) mostrar tambien el numero de vendedor y su nombre

~~~
SELECT c.id, c.nombre AS 'cliente', v.id, concat(v.nombre, ' ', v.apellido) AS 'vendedor'
FROM clientes c, personal v
WHERE c.personal_id = v.id;
~~~

|id|cliente|id|vendedor|
|-|-|-|-|
|1|construcciones diaz inc|1|Linus Tolbars|
|2|imprenta ltda|1|Linus Tolbars|
|3|fruteria del barrio|2|Jared Latorre|
|4|colchones sa|1|Linus Tolbars|
|5|julian mejia|2|Jared Latorre|

23. Listar todos los encargos realizados con la marca del coche y el nombre del cliente

~~~
SELECT e.id, co.marca, c.nombre
FROM ventas e
INNER JOIN coches co ON co.id = e.coche_id
INNER JOIN clientes c ON c.id = e.cliente_id
~~~

|id|marca|nombre|
|-|-|-|
|1|renault|construcciones diaz inc|
|2|mercedes benz|imprenta ltda|
|3|lamborghini|fruteria del barrio|
|4|bugatti|colchones sa|
|5|toyota|julian mejia|

24. listar los encargos con el nombre del coche del cliente y la ciudad del cliente, pero cuando sea de bogotá

~~~
SELECT p.id, co.nombre, c.nombre, c.ciudad
FROM encargos
INNER JOIN coches co ON co.id = e.coche_id
INNER JOIN clintes c ON c.id = e.cliente_id
WHERE c.ciudad = 'bogota';
~~~

|id|marca|nombre|ciudad|
|-|-|-|-|
|1|renault|construcciones diaz inc|Bogota|
|2|mercedes benz|imprenta ltda|Bogota|
|3|lamborghini|fruteria del barrio|Bogota|
|4|bugatti|colchones sa|Bogota|
|5|toyota|julian mejia|Bogota|

25. Obtener una lista de los nombres de los clientes con el importe de susu encargo acumulado
1. order by 2 (orden por la segunda columna)

~~~
SELECT cl.nombre, SUM(precio*cantidad) AS 'importe'
FROM clientes cl 
INNER JOIN ventas ve ON cl.id = ve.cliente_id
INNER JOIN coches co ON ve.coche_id = co.id
GROUP BY cl.nombre
ORDER BY 2 ASC;
~~~

|nombre|importe|
|-|-|
|construcciones diaz inc |24000|
|julian mejia|25000|
|fruteria del barrio |50000|
|imprenta ltda |60000|
|colchones sa|60000|

26. sacar vendedores que tienen jefe y sacar el nombre el jefe 
1. clave ajena reflexiva
~~~
SELECT CONCAT(v1.nombre,' ',V1.apellido) AS 'Vendedor', CONCAT(v2.nombre,' ',v2.apellido) AS 'Jefe' 
FROM vendedores v1
INNER JOIN vendedores v2 ON v1.jefe = v2.id;
~~~

|Vendedor|Jefe|
|-|-|
|Kenneth Latorre|Jared Latorre|
|Christian Latorre|Linus Tolbars|

27. Visualizar los nombres de los clientes y la cantidad de encargos realizados, incluyendo los que no hayan realizado encargos
1. CON LEFT JOIN trae todo lo de la tabla clientes dandole prioridad, asi los datos no tenga nada

~~~
INSERT INTO clientes VALUES (null, 1, 'tienda party', 'medellin',0, CURDATE());
~~~
~~~
SELECT c.nombre, COUNT(e.id) 
FROM clientes c
LEFT JOIN ventas e ON c.id = e.cliente_id
GROUP BY 1;
~~~

|nombre | COUNT(e.id)|
|-|-|   
|casita roja|0|
|colchones sa|1|
|construcciones diaz inc|1|
|fruteria del barrio|1|
|hell boy|0|
|imprenta ltda|1|
|julian mejia|1|
|jungue animate|0|
|Oasis|0|
|tienda party|0|

28. listar los vendedores y tengan o no clientes, y mostrar numero de clientes

~~~
SELECT p.nombre, p.apellido, COUNT(c.id) AS 'cantidad de clientes'
FROM personal p
LEFT JOIN clientes c ON c.personal_id = p.id
GROUP BY p.id;
~~~

|nombre|apellido|cantidad de clientes|
|-|-|-|
|Linus|Tolbars|5|
|Jared|Latorre|2|
|Bill|Gates|1|
|Steve|Jobs|1|
|Kenneth|Latorre|0|
|Christian|Latorre|1|

29. crear una vista llamada vandedoreaA que incluira todos los vendedores del grupo que se llame "VEndedores A"

~~~
CREATE VIEW VendedoresA AS
SELECT * FROM vendedores WHERE grupo_id IN
(SELECT id FROM grupos WHERE nombre="VendedoresA");
~~~

30. mostrar los datos del personal con mas antiguedad en el concesionario

~~~
SELECT * FROM personal ORDER BY fecha ASC LIMIT 1;
~~~

31. obtener los coches con mas unidades vendidas

~~~
SELECT * FROM coches WHERE id IN
(SELECT coche_id FROM ventas where cantidad IN
  (SELECT MAX(cantidad) from ventas));
~~~

|id|modelo|marca|precio|stock|
|-|-|-|-|-|
|2|365i|mercedes benz|20000|5|

