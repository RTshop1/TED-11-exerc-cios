# 04 Leitura do vetor A com 10 números
A = [float(input(f"Digite o número {i + 1}: ")) for i in range(10)]

# Leitura do número x
x = float(input("Digite um número para multiplicar: "))

# Cálculo e impressão do vetor M
M = [a * x for a in A]
print("Vetor M:", M)