# 08 Leitura do vetor com 30 números
vetor = [float(input(f"Digite o número {i + 1}: ")) for i in range(30)]

# Leitura do número a ser verificado
numero_verificar = float(input("Digite um número para verificar quantas vezes aparece no vetor: "))

# Contagem de quantas vezes o número aparece no vetor
contagem = vetor.count(numero_verificar)

# Resultado
print(f"O número {numero_verificar} aparece {contagem} vez(es) no vetor.")