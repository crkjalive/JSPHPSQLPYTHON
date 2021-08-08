# -*- coding: utf-8 -*-

from lampara_ON_OFF_class import Lamp

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