# forma de acceder a un string

my_string = 'pyThon es un super lenguaje'
my_list = ['Hola', 'Mundo','Dev'];

print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[3])
print(my_string[4])
print(my_string[5])

# funciones de strings
print(len(my_string)) # 6
print(my_string.upper()) # Mayusculas
print(my_string.isupper()) # False
print(my_string.lower()) # minusculas
print(my_string.islower()) # False
print(my_string.find('T')) # 2 position
print(my_string.endswith('n')) # True
print(my_string.startswith('j')) # False
# print(my_string.isdigit())
print(','.join(my_string)) # list a str
print(','.join(my_list)) # list a str
x = my_string.split(' ') # str a list
print(x)

# rebanadas o slice
print(my_string[3]) # h indice 3
print(my_string[1:]) # desde 1 hasta el final
print(my_string[1:3]) # yt no incluye el indice 3
print(my_string[1:5]) # posicion 1 a la 5
print(my_string[1:6:2]) # se salta de 2 en 2
print(my_string[::-1]) # imprime desde el ultimo
