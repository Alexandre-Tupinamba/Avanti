def segundo_maior_lista(lista):
    if len(lista) < 2:
        return None
    
    primeiro_maior = float('-inf')
    segundo_maior = float('-inf')
    for num in lista:
        if num > primeiro_maior:
            segundo_maior = primeiro_maior
            primeiro_maior = num
        elif num > segundo_maior and num != primeiro_maior:
            segundo_maior = num
    return segundo_maior

# Exemplo de uso
numeros = [10, 20, 4, 45, 99]
resultado = segundo_maior_lista(numeros)
print("O segundo maior número é:", resultado)