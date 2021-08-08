def palindrome(string):
	return string == string[::-1]

try:
	print(palindrome(1))
except TypeError:
	print("Solo se pueden palabras NO números")

# de esta forma podemos capturar el error y  
# mostrar un mensaje por pantalla sobre el error