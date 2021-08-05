"""
"abacabad" c
{
	'a':(0,4),
	'b':(1,2),
	'c':(3,1),
	'd':(7,1),
}
"abacabaabacaba" _
"abcdefghijklmnñopqrstuvwxyzasffghklqwerty" d
"bcccccccccyb" y 
"""

def first_not_repeat_char(char_secuence):
	seen_letters = {}

	for idx, letter in enumerate(char_secuence):
		if letter not in seen_letters:
			seen_letters[letter] = (idx, 1)
		else:
			seen_letters[letter] = (seen_letters[letter][0],seen_letters[letter][1] + 1)

	final_letters = []

	for key, value in seen_letters.items():
		if value[1] == 1:
			final_letters.append( (key, value[0]) )

	# funcion que retorna
	#def sort_order(value):
	#	return value[1]

	# funcion de 1 linea lambda
	not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

	if not_repeated_letters:
		return not_repeated_letters[0][0]
	else:
		return '_' # si no encontro nada


if __name__ == '__main__':
	char_secuence = str(input('Escribe secuencia de caractereres: '))

	result = first_not_repeat_char(char_secuence)

	if result == '_':
		print('Todos los caracteres se repiten.')
	else:
		print(f'el primer caracter no repetido es: {result}')



# 