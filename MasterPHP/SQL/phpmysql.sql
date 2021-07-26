create database phpmysql;
use phpmysql;
# root kennethjared

CREATE TABLE notas(
    id int auto_increment,
    titulo varchar(100) not null,
    descripcion varchar(100) not null,
    color varchar(50) not null,
    
    CONSTRAINT pk_notas PRIMARY KEY(id)
) ENGINE=InnoDB;

desc notas;

insert into notas values (null, "CSS3", "estilos en cascada","azul");
update notas set descripcion = "Lenguaje de programacion PHP" WHERE id = 1; 
delete from notas where id = 4;
select * from notas;