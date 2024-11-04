# 05 Inicialização dos vetores A e B
A = [1, 2, 3, 4, 5]  # Exemplo de valores para A
B = [10, 20, 30, 40, 50]  # Exemplo de valores para B

# Cálculo do vetor N como a soma dos elementos de A e B
N = [a + b for a, b in zip(A, B)]

# Impressão do vetor N
print("Vetor N:", N)