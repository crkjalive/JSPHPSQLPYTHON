objetos = ["Google",True,38,False,"2.3",23.4]
objetos2 = ["Twitter",True,37,False,"6.9",29.4]

print(len(objetos))
print(type(objetos[0]))
print(type(objetos[1]))
print(type(objetos[2]))
print(type(objetos[5]))

objetos.append("NodeJs")
objetos.insert(0,"Git")
print(objetos)
print(id(objetos))
objetos.pop(3)
print(objetos)
print(objetos.count("2.3"))
lista_reves = objetos[::-1]
print(lista_reves)

for elemento in objetos:
  print(elemento)	

super_lista = objetos + objetos2
print(super_lista)