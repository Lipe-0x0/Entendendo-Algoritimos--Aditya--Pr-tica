def fat(n):
    if n == 1: # Caso base (para finalizar a função)
        return 1
    else: # Caso recursivo
        return n*fat(n-1)
    
# Recursividade não costuma ser bom pois trabalha com pilhas e consequentemente consome muita mémoria

print(fat(13))