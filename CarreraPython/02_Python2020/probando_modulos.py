import random
import math

probando = "Mensaje formateado"
mensaje = "hola"
numero = 100

print("probando {} {}".format(probando,mensaje))
print(mensaje, probando, numero, "estamos probando")

numero//=2
print(numero)

print(random.random())
print(random.uniform(1,10))
print(random.randrange(10))
print(random.randrange(0,101))
print(random.randrange(0,101,2))
print(random.randrange(0,101,5))
print(random.choice("Hola mundo"))
print(random.choice([1,2,3,4,5]))
print(random.sample([1,2,3,4,5],2))
lista = [1,2,3,4,5]
random.shuffle(lista)
print(lista)

numeros = [0.9999999, 1, 2, 3]
sumatorio = math.fsum(numeros)
print(sumatorio)

print(math.trunc(125.45))
print(math.pow(2, 3))
print(math.sqrt(5))
print(math.pi)
print(math.e)

from datetime import datetime

dt = datetime.now()

print(dt)
print(dt.year)
print(dt.month)
print(dt.day)

print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)

print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
print("{}/{}/{}".format(dt.day, dt.month, dt.year))
dt = datetime(2000,1,1)
print(dt)






