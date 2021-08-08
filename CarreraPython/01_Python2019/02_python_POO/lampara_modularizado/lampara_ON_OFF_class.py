# -*- coding: utf-8 -*-

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
