def busca_menor(array):
    menor_ind = 0
    menor_valor = array[0]

    for i in range(len(array)):
        if array[i] < menor_valor:
            menor_valor = array[i]
            menor_ind = i
        return menor_ind
    
def ordenacao_crescente(array):
    novo_array = []
    for i in range(len(array)):
        menor_ind = busca_menor(array)
        novo_array.append(array.pop(menor_ind))
    return novo_array

# Comparação com função "sorted"

import time

tempo1 = time.time()
ordenacao_crescente([2,5,10,78,45,23])
tempo2 = time.time()

tempo3 = time.time()
sorted([2,5,10,78,45,23])
tempo4 = time.time()

print("Diferença da velocidade entre sorted e o algoritimo de ordenação são respectivamente:")
print("Sorted: %.20f" % (tempo4-tempo3))
print("Ordenação: %.20f" % (tempo2-tempo1))