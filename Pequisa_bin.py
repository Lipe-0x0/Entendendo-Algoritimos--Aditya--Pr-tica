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

# Para verificação da eficácia, recomendo utilizar time.time
# Ex:
import time

tempo1 = time.time()
print(busca_bin([1,2,3,4,5,6,10,12,13,14,15,20,21,23,24,25],27))
tempo2 = time.time()

print("Algoritimo de busca binária possui tempo de execução = %.20f"%(tempo2-tempo1))