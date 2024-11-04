# Inicialização do vetor para armazenar os nomes dos clubes
clubes = []

# Leitura dos nomes dos clubes, evitando duplicatas
while len(clubes) < 5:
    clube = input("Digite o nome do clube: ")
    if clube not in clubes:
        clubes.append(clube)
    else:
        print("Nome já inserido. Tente novamente.")

# Leitura do nome do clube a ser buscado
nome_buscado = input("Digite o nome de um clube para buscar: ")

# Verificação se o nome buscado está entre os clubes
if nome_buscado in clubes:
    print("ACHEI")
else:
    print("NÃO ACHEI")
