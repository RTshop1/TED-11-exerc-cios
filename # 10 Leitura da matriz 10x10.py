# 10 Leitura da matriz 10x10
matriz = []
print("Digite os 100 números para preencher a matriz 10x10:")
for i in range(10):
    linha = [float(input(f"Digite o número para a posição matriz[{i}][{j}]: ")) for j in range(10)]
    matriz.append(linha)

# Inicialização do maior valor e sua posição
maior_valor = matriz[0][0]
linha_maior, coluna_maior = 0, 0

# Encontrar o maior valor e sua localização
for i in range(10):
    for j in range(10):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            linha_maior, coluna_maior = i, j

# Resultado
print(f"O maior valor é {maior_valor} encontrado na posição: linha {linha_maior}, coluna {coluna_maior}.")