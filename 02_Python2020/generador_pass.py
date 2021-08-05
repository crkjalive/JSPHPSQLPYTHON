import random

def keygen():
	mayusculas = ('A','B','C','D','E','F','G')
	minusculas = ('a','b','c','d','e','f','g')
	simbolos = ('!','#','$','&','/',')','~')
	numeros = ('1','2','3','4','5','6','7','8','9','0')

	caracteres = mayusculas+minusculas+simbolos+numeros

	segura = []

	for i in range(15):
		caracter_random = random.choice(caracteres)
		segura.append(caracter_random)

	keygen = "".join(segura)
	
	return keygen 



def main():
	password_safe = keygen()
	print(f"Tu nueva contraseña es: {password_safe} ") 



if __name__ == '__main__':
	main()
