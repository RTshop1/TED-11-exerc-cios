# 02 Inicialização vetor as notas dos alunos
notas = []

# Leitura das notas dos alunos
for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

# Cálculo da média
media = sum(notas) / len(notas)

# Contagem de alunos com nota acima da média
contagem = sum(1 for nota in notas if nota > media)

# Resultados
print(f"Média da turma: {media:.2f}")
print(f"Número de alunos acima da média: {contagem}")