# crear tupla
mi_tupla = 1,2,3,4,5
mi_tupla1 = (1,2,3,4,5)
mi_tupla2 = (7,)
mi_tupla3 = (1)
print(type(mi_tupla)) # tuple
print(type(mi_tupla1)) # tuple
print(type(mi_tupla2)) # tuple
print(type(mi_tupla3)) # int

# modificacion
mi_tupla4 = mi_tupla1, mi_tupla2
print(mi_tupla4)