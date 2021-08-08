# operaciones con listas

# tipo de dato
mi_lista = [2,3,4]
print(type(mi_lista)) # list

# agregar a lista
mi_lista.append(1)
print(mi_lista)

# concatena listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista2 + lista1
print(lista3)

# imprimir 10 veces a
listado = ['a']
lista_a = listado * 10
print(lista_a)

# slices en listas
arr = [10,2,3,5,6,9,87]
print(arr)
print(arr[:4])
print(arr[4:])
print(arr[::-1]) # invierte la lista
print(arr[1::-1]) # invierte

# listas son mutables
arr_nombres = ['laura','valentina','catalina']
arr_nombres[1] = 'dakota'
print(arr_nombres)

# alterando las listas 
# agrega al final
arr_nombres.append('sansa') 
print(arr_nombres)

# elimina el ultimo, y regresa el valor
eliminado = arr_nombres.pop() 
print(arr_nombres)
print(eliminado)

# ordenar listas
arr_nombres.sort()
print(arr_nombres)

# borrar por indice
del arr_nombres[1]
print(arr_nombres)

# crear lista a partir de una variable 
nombre_list = 'kenneth jared'

lista_del_nombre = list(nombre_list) # crea array
print(lista_del_nombre) 
print(len(lista_del_nombre)) # 13

lista_del_nombre[7] = "Hola"
print(lista_del_nombre) 

aString = ''.join(lista_del_nombre) # crea string
print(aString)
print(len(aString))
