import random

def ordenamiento_burbuja(lista):

    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):

            if lista[j] > lista [j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)
    
    return lista


if __name__ == '__main__':

    longitud_lista = int(input('de que tamaño será tu lista de números? '))
    
    lista = [random.randint(0,100) for i in range(longitud_lista)]
    print(lista)
 
    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)
    
