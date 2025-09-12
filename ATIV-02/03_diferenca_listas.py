def diferenca_listas(lista1, lista2):
    return [list(item for item in lista1 if item not in lista2),
            list(item for item in lista2 if item not in lista1)]

# Exemplo de uso
listaA = [1, 2, 3, 4, 5]
listaB = [4, 5, 6, 7, 8]
diferenca = diferenca_listas(listaA, listaB)
print(diferenca)  