def retorna_par(lista):
    return [num for num in lista if num % 2 == 0]

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = retorna_par(numeros)
print(pares) 