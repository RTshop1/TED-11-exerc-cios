# 07 Leitura dos vetores V1 e V2
V1 = [float(input(f"Digite o número {i + 1} para V1: ")) for i in range(10)]
V2 = [float(input(f"Digite o número {i + 1} para V2: ")) for i in range(10)]

# Contagem de elementos iguais nas mesmas posições
contagem = sum(1 for i in range(10) if V1[i] == V2[i])

# Resultado
print(f"A quantidade de elementos iguais nas mesmas posições é: {contagem}")