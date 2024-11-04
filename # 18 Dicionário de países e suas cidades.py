# 18 Dicionário de países e suas cidades
cidades_por_pais = {
    'Brasil': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'],
    'EUA': ['Nova Iorque', 'Los Angeles', 'Chicago']
}

# Dicionário para armazenar a cidade mais populosa de cada país
cidades_populosas = {}

# Cálculo da cidade mais populosa para cada país
for pais, cidades in cidades_por_pais.items():
    # Assume que a primeira cidade é a mais populosa
    cidade_populosa = cidades[0]
    cidades_populosas[pais] = cidade_populosa

# Exibindo o resultado
print("Cidade mais populosa de cada país:", cidades_populosas)