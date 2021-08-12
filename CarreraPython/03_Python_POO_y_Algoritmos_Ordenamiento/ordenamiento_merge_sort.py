import random

def ordenamiento_por_mezcla(lista):

    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(f"izquierda {izquierda}-{derecha} derecha")
        print("*"*35)
    
        # llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # iteradores de sublistas
        i = 0
        j = 0
        # iterador de lista principal
        k = 0
        
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i+=1
            else:
                lista[k] = derecha[j]
                j+=1
            k+=1


        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1 
        
        #print(f"{izquierda}-{derecha}")
        print(f"Izquierda {izquierda}-{derecha} Derecha")
        print(f"lista armada {lista}")
        print('*'*35)

    return lista



if __name__ == '__main__':

    longitud_lista = int(input('de que tamaño será tu lista de números? '))
    
    lista = [random.randint(0,100) for i in range(longitud_lista)]
    print(f"lista a ordenar {lista}")
 
    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(f"lista finalmente ordenada {lista_ordenada}")
