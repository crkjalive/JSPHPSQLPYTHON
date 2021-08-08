# iterar
for i in range(30):
	if i == 5 or i == 11 or i == 17 or i == 19:
		continue
	elif i == 20:
		break
	else:
		print(i,"Hola Mundo")


for x in range(20):
	if x % 3 != 0:
		continue
	else:
		print(x**2)

i = 0
while i < 10:
	print("iteracion con while", i)
	i+=1
