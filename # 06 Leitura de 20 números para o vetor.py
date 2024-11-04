# Leitura de 20 números para o vetor
vetor = [float(input(f"Digite o número {i + 1}: ")) for i in range(20)]

# Leitura do número a ser verificado
numero_verificar = float(input("Digite um número para verificar: "))

# Verificação e criação do novo vetor
if numero_verificar in vetor:
    novo_vetor = [num for num in vetor if num != numero_verificar]
    print("Novo vetor sem o número:", novo_vetor)
else:
    print(f"O número {numero_verificar} não existe no vetor.")