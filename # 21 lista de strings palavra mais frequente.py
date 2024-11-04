# 21 lista de strings palavra frequente na lista

from collections import Counter

# Lista de strings
palavras = ['azul', 'vermelho', 'verde', 'azul', 'vermelho', 'amarelo', 'azul']

# Contando a frequência das palavras
contagem = Counter(palavras)

# Encontrando a palavra mais frequente
palavra_mais_frequente = contagem.most_common(1)[0][0]

# Exibindo o resultado
print("Palavra mais frequente:", palavra_mais_frequente)