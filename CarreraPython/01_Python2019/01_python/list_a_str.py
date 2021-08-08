# string
mi_string = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789.,?!"
print(mi_string)
print(type(mi_string))

# invertir string
invertir = mi_string[::-1]
print(invertir)
print(type(invertir))

# str a list
lista = list(mi_string)
print(lista)
print(type(lista))

# list a str con **
aStringDeNuevo = '**'.join(lista)
print(aStringDeNuevo)
print(type(aStringDeNuevo))

# str a list sin **
split = aStringDeNuevo.split('**')
print(split)
print(type(split))