import random
import time

def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
            lista[posicion_actual] = valor_actual

    return lista


if __name__ == '__main__':

    longitud_lista = int(input('de que tamaño será tu lista de números? '))
    
    lista = [random.randint(0,100) for i in range(longitud_lista)]
    print(lista)

    comienzo = time.time()
    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)
    final = time.time()
    print(final- comienzo)
