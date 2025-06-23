# Recursividade Fatorial
def fat(n):
    if n == 1: # Caso base (para finalizar a função)
        return 1
    else: # Caso recursivo
        return n*fat(n-1)
    
# Recursividade não costuma ser bom pois trabalha com pilhas e consequentemente consome muita mémoria


# Recursividade Soma
def soma(arra):
    if len(arra)==1:
        return arra[0] # Caso base
    else: # Caso recursivo
        ultimo_elem = arra.pop(len(arra)-1) # Pega o ultimo elemento
        return ultimo_elem + soma(arra) # Soma o ultimo elemento com o array modificado


# Recursividade Contagem
def contagem(array): 
    cont = 1 # contador
    if len(array)==1: # Caso base
        return cont
    else: # Caso recursivo
        array.pop() # Modifica o array retirando um elemento
        return cont + contagem(array) 
    
