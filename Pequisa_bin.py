# Pesquisa Binaria
def busca_bin(array, valor):
    menor_ind = 0
    maior_ind = len(array)-1
    
    while menor_ind<=maior_ind:
        meio_ind = int((maior_ind+menor_ind)/2)
        chute = array[meio_ind]
        if chute == valor:
            return meio_ind
        elif chute > valor:
            maior_ind = meio_ind - 1
        else:
            menor_ind = meio_ind + 1
    return -1

# Pesquisa Binaria Recursiva
def busca_bin_rec(array,valor):
    menor_ind = 0
    maior_ind = len(array)-1
    meio_ind = int((maior_ind+menor_ind)/2)
    chute = array[meio_ind]

    if chute == valor:
        print("achou")
        return meio_ind
    
    else:
        if chute>valor:
            print("chute>valor")
            array.pop(maior_ind)
            return busca_bin_rec(array, valor)
        
        if chute<valor:
            print("chute<valor")
            array.pop(menor_ind)
            return busca_bin_rec(array, valor)


print(busca_bin_rec([1,2,3,4,5],4))
