# Curso de Master en PHP por Victor Robles
1. Programacion desde cero
2. PHP moderno
3. Bases de datos
4. Maquetacion Web 
5. POO y MVC 
6. Librerias
8. Laravel
9. Synfony 4
10. Wordpress
11. Desarrollo Web

# Seccion HTML (opcional)
1. Que es HTML 
2. Estructura 
3. Etiquetas para textos
4. Listas
5. Imagenes
6. Tablas
7. Formularios
8. Ejercicio
9. Pasamos a PHP

# Desarrollo Web desde cero 
## 1. Que es HTML
Es un repaso de HTMl solo tomo apuntes de lo que no tenga claro 

1. etiquetas
2. atributos

# Estructura HTML
<!doctype html>
<html lang="es">
  <head>
    <title>Hola Mundo</title>
  </head>
  <body>
    <h1>Hola Mundo</h1>
  </body>
</html>

# Etiquetas de Textos
1. p  parráfo
2. br/ salto de linea
3. hr/ linea Horizontal separatoría
4. strong negrita
5. em
6. span texto sin formato
7. i cursiva
8. blockquote citas remarcadas
9. h3 h1 hasta h6 titulos y subtitulso

# Listados
1. ol lista ordenada
2. ul lista desordenada
3. li item de la lista 
4. a hipervinculos

# Imagenes
1. img inserta imagenes
2. alt texto descriptivo
3. ***title*** popup descriptivo de la imagen
4. src ruta de la imagen
5. width 
6. heigth

# Tablas 
las tablas se deben crear en css, segun el modelo de caja
1. table tabla
2. th encabezados
3. tr fila
4. td columnas 

### atributo de las tablas 
1. border="1" añade borde a la tabla
2. colspan="2" toma el ancho de 2 columnas

# Formularios
son para enviar informacion introducida por el usuario
1. form crea el formulario

### Atributos de la etiqueta form 
1. action Donde se envian los datos  
2. method Como se envian los datos metodo POST ó GET

## Etiquetas para el form 
1. label
  - for a que input pertenece
2. input
  - name nombre del elemento input 
  - placeholder texto interno del input 
  - type tipo de dato que va a recibir 
  - type=text texto
  - type=radio unica seleccion
  - value valor del elemento
3. textarea input de texto multilinea
4. select name="genero" contenedor de opciones
  - option value="hombre" Hombre
  - option value="mujer" Mujer
5. button 
6. input type=submit value=EnviarDatos

# ejercicio 

***formulario***

~~~
for

p
  label for=nombre Nombre
  input type=text name=nombre

p 
  label for=biografia Biografia
  textarea name=biografia

p 
  label for=edad Edad
  select name=edad
  option value=mayor Mayor de edad 
  option value=adulto Adulto
  option value=65 Mayor de 65 años

input type=submit value=enviar email
~~~
<!--
# enlaces 
1. a href=index.html
2. a href=https://www.google.com target=_blank
-->













