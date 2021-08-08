# mirar que tipo de dato es con type()
print(type(2))
print(type('hola'))
print(type(True))
print(type(2.2))

# variables y expresiones 
pi = 3.14159
radio = 3
area = pi * radio**2
print(area)

# funciones, parametros, inicializacion python
def suma(num1,num2):
	operacion = num1 + num2
	return operacion

def main():
	print(suma(7,9))

if __name__ == '__main__':
	main()

# condicional if
edad = 20
if (edad > 18):
	print(f"con {edad} puedes ingresar")
else:
	print(f"con {edad} NO puedes ingresar")













