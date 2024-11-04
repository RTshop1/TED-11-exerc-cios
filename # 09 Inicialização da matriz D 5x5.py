# 09 Inicialização da matriz D 5x5
D = []

# Leitura da matriz 5x5
print("Digite 25 números diferentes para preencher a matriz 5x5:")
for i in range(5):
    linha = []  # Cria uma nova linha
    for j in range(5):
        num = int(input(f"Digite o número para a posição D[{i}][{j}]: "))
        linha.append(num)  # Adiciona o número à linha
    D.append(linha)  # Adiciona a linha à matriz

# Leitura do número X
X = int(input("Digite um número para verificar se existe na matriz: "))

# Verificação se o número X existe na matriz
encontrado = False  # Inicializa a variável encontrado como False
for i in range(5):
    for j in range(5):
        if D[i][j] == X:  # Verifica se o número na posição D[i][j] é igual a X
            encontrado = True  # Se encontrado, muda para True
            break  # Para de verificar
    if encontrado:  # Se já encontrou, não precisa verificar mais linhas
        break

# Resultado
if encontrado:
    print(f"O número {X} existe na matriz.")
else:
    print(f"O número {X} NÃO existe na matriz.")