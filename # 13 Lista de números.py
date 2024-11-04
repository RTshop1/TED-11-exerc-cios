# 13 Lista de números
numeros = [1, 2, 3, 4, 5, 6]

# Cálculo da soma dos números pares
soma_pares = sum(num for num in numeros if num % 2 == 0)

# Exibindo o resultado
print("A soma dos números pares é:", soma_pares)