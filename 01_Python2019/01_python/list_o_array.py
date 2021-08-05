# listas
# temperatura promedio

def average_temps(temps):
	sum_of_temps = 0

	for temp in temps:
		sum_of_temps += float(temp) # python2

	return sum_of_temps / len(temps)


if __name__ == '__main__':
	temps = [21,24,24,22,25,23,24]

	average = average_temps(temps)

	# print(f'La temperatura promedio es: {average}')
	print(average) # python2

# en python2 convertir a float para que de exacto