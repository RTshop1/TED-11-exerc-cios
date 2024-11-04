# 03 Ler vetor Q de 20 posições
import random

# Preenchendo o vetor Q com 20 números positivos aleatórios
Q = [random.randint(1, 100) for _ in range(20)]

# Exibindo o vetor gerado
print("Vetor Q:", Q)

# Encontrando o maior e menor elemento e suas posições
maior = max(Q)
menor = min(Q)
pos_maior = Q.index(maior)
pos_menor = Q.index(menor)

# Resultados
print(f"O maior elemento de Q é {maior} na posição {pos_maior}.")
print(f"O menor elemento de Q é {menor} na posição {pos_menor}.")