# 16 Lista de dicionários representando os produtos
estoque = [
    {'nome': 'maçã', 'preço': 2.0, 'quantidade': 5},
    {'nome': 'banana', 'preço': 1.5, 'quantidade': 10}
]

# Cálculo do valor total do estoque
valor_total = 0.0  # Inicializa o valor total

for produto in estoque:
    valor_total += produto['preço'] * produto['quantidade']  # Soma preço * quantidade

# Exibindo o resultado
print("Valor total do estoque:", valor_total)