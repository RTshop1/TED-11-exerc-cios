#  22 Lista de filmes
filmes = [
    {'título': 'O Poderoso Chefão', 'ano': 1972, 'gênero': 'drama'},
    {'título': 'Pulp Fiction', 'ano': 1994, 'gênero': 'drama'},
    {'título': 'Indiana Jones e os Caçadores da Arca Perdida', 'ano': 1981, 'gênero': 'aventura'},
    {'título': 'De Volta Para o Futuro', 'ano': 1985, 'gênero': 'aventura'}
]

# Ordenação da lista de filmes
filmes_ordenados = sorted(filmes, key=lambda x: (x['gênero'], x['ano']))

# Exibindo o resultado
print("Filmes ordenados:", filmes_ordenados)