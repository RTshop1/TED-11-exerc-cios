# 12 Criando um dicionário para armazenar os números favoritos
numeros_favoritos = {}

# Perguntando os números favoritos para cinco colegas
for _ in range(5):
    nome = input("Digite o nome do colega: ")
    numero_favorito = input(f"Qual é o número favorito de {nome}? ")
    numeros_favoritos[nome] = numero_favorito  # Armazena o número favorito no dicionário

# Exibindo os números favoritos
print("\nNúmeros favoritos dos colegas:")
for nome, numero in numeros_favoritos.items():
    print(f"{nome}: {numero}")