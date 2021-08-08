# -*- Coding: UTF-8 -*-

KEYS = {
	',':'?',
	'¡':'¿',
	'¿':'¡',
	'?':'!',
	'!':'.',
	'.':',',
	'a':'s',
	'b':'t',
	'c':'u',
	'd':'v',
	'e':'w',
	'f':'x',
	'g':'y',
	'h':'z',
	'i':'0',
	'j':'1',
	'k':'2',
	'l':'3',
	'm':'4',
	'n':'5',
	'ñ':'6',
	'o':'a',
	'p':'b',
	'q':'c',
	'r':'d',
	's':'e',
	't':'f',
	'u':'g',
	'v':'h',
	'w':'i',
	'x':'j',
	'y':'k',
	'z':'l',
	'0':'m',
	'1':'n',
	'2':'ñ',
	'3':'o',
	'4':'ú',
	'5':'ó',
	'6':'á',
	'7':'é',
	'8':'í',
	'9':'r',
	'á':'7',
	'é':'8',
	'í':'9',
	'ó':'p',
	'ú':'q',
	}


def cypher(message):
	words = message.split(' ')
	cypher_message = []

	for word in words:

		cypher_word = ''

		for letter in word:
			cypher_word += KEYS[letter]

		cypher_message.append(cypher_word)

	return ' '.join(cypher_message)


def decypher(message):
	words = message.split(' ')

	decypher_message = []

	for word in words:
		decypher_word = ''

		for letter in word:

			for key, value in KEYS.items():

				if value == letter:
					decypher_word += key

		decypher_message.append(decypher_word)

	return ' '.join(decypher_message)


def run():

	while True:

		command = str(input('''
--- * --- * --- * --- 
  MENSAJES CIFRADOS
--- * --- * --- * --- 

Bienvenido a criptografía.
  Que deseas hacer?

[c] cifrar mensaje
[d] decifrar mensaje
[s] salir

>> '''))

		if command == 'c':
			message = str(input('Mensaje a cifrar: ')).lower()
			cypher_message = cypher(message)
			print(f"mensaje cifrado: \n{cypher_message}")

		elif command == 'd':
			message = str(input('Escribe tu mensaje cifrado: ')).lower()
			decypher_message = decypher(message)
			print(f"desifrar mensaje: \n{decypher_message}")
		
		elif command == 's':
			print("Adios")
			break

		else:
			print('comando no encontrado')


if __name__ == '__main__':
	run()