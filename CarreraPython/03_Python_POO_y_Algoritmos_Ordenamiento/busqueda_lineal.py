import random

def busqueda_lineal(lista, objetivo):
    match = False 

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match


if __name__ == '__main__':
    longitud_lista = int(input('de que tamaño será tu lista de números? '))
    lista = [random.randint(0,100) for i in range(longitud_lista)]
    
    #print(lista)

    objetivo = int(input('que número quieres encontrar? '))

    
    encontrado = busqueda_lineal(lista, objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')






