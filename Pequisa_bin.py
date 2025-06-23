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
def busca_bin_rec(array,valor, maior_ind, menor_ind = 0):
    meio_ind = int((maior_ind+menor_ind)/2)
    chute = array[meio_ind]

    if chute == valor: # Caso base
        return meio_ind
    
    else: # Caso recursivo
        if chute>valor:
            maior_ind_novo = meio_ind-1
            return busca_bin_rec(array, valor, maior_ind_novo, menor_ind)
        
        if chute<valor:
            menor_ind_novo = meio_ind+1
            return busca_bin_rec(array, valor, maior_ind, menor_ind_novo)


arra = [5,10,11,20,34,40,50]
print(busca_bin_rec(arra,5, maior_ind=len(arra)-1))
