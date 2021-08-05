# -*- coding: utf-8 -*- 

def protected(func):

	def wrapper(password):
		
		if password == 'siguealconejoblanco':
			return func()
		else:
			print('No es el santo y seña')

	return wrapper


@protected
def protected_func():
	print('Bienvenido, puede ingresar')


if __name__ == '__main__':
	
	password = str(input('Ingreso de contraseña: '))

	protected_func(password)