# 19 lista de tuplas

import math

# Lista de pontos tridimensionais
pontos = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# Cálculo da distância total percorrida
distancia_total = sum(math.sqrt((pontos[i + 1][0] - pontos[i][0]) ** 2 + 
                                 (pontos[i + 1][1] - pontos[i][1]) ** 2 + 
                                 (pontos[i + 1][2] - pontos[i][2]) ** 2)
                      for i in range(len(pontos) - 1))

# Exibindo o resultado
print("Distância total percorrida:", distancia_total)