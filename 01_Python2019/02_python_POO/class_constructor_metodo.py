class Lamp():
	# estado de la lampara
	_LAMPS = ['''

			||| O N |||

	''',
	'''

			|| O F F ||

	''']


	# constructor
	def __ini__(self): 
		self._is_turned_on = False


	# prendido (metodos publicos)
	def turn_on(self):
		self._is_turned_on = True
		self._display_image()


	# apagado (metodos publicos)
	def turn_off(self):
		self._is_turned_on = False
		self._display_image()


	# estado (metodo privado)
	def _display_image(self):
		if self._is_turned_on:
			print(self._LAMPS[0])
		else:
			print(self._LAMPS[1])

def run():
	
	# instancia del objeto
	lamp = Lamp()

	while True:
		command = str(input('''
			Que quieres hacer: 

			[p] prender
			[a] apagar

			=> '''))

		if command == 'p':
			lamp.turn_on()

		elif command == 'a':
			lamp.turn_off()
		else:
			print('''
				
			||| chao |||

				''')
			break

if __name__ == '__main__':
	run()