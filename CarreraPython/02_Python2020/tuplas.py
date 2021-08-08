tupla = (1,2,3,4,5)
tupla2 = (5,6,7,8,9,0)

super_tupla = tupla+tupla2
print(super_tupla)
print(type(super_tupla))

for tup in tupla:
	print(f"{id(tup*9+3)} {tup}")