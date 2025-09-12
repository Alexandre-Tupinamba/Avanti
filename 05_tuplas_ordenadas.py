def tuplas_ordenadas_nome_idade(tuplas):
    return sorted(tuplas, key=lambda x: (x[0], x[1]))


# Exemplo de uso
tuplas = [("Ana", 25), ("João", 22), ("Ana", 20), ("Carlos", 30)]
tuplas_ordenadas = tuplas_ordenadas_nome_idade(tuplas)
print(tuplas_ordenadas)  