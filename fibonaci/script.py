def fibonacci_recursivo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequencia = fibonacci_recursivo(n - 1)
        numero = sequencia[-1] + sequencia[-2]
        sequencia.append(numero)
    return sequencia

n = 100
resultado = fibonacci_recursivo(n)
print(resultado)


# Com erro
#  -> fibonacci_recursivo(n - 2) <- ocorre um "erro" pois toda vez que o loop reincia ele remove 2 de n. 
#     exemplo atualmente n é igual a 10, no fim do primeiro loop n vai ser igual a 8 e depois 6 ... 4... divindo o loop pela metade
#     como se fosse n / 2 
# --------

# Sem erro
#   -> fibonacci_recursivo(n - 2) <- Corrigindo o erro para -> fibonacci_recursivo(n - 1) <- 
#      O loop volta a funcionar normalmente que no caso funciona da seguinte forma.
#      O loop é iniciado com n = 10 no fim do primeiro loop "por baixo dos panos" n passa a ser 9 e depois 8 7 6 5...
#      e o loop percorre todos os numeros definidos 