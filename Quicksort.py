# Algoritimo Quicksort
def quicksort(array):
    if len(array)<2: # Caso base
        return array
    
    else: # Caso recursivo
        pivo = array[0]
        menores = [i for i in array if i < pivo]
        maiores = [i for i in array if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
    

print(quicksort([1,35,20,12,9,78]))