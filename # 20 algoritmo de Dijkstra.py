# 20 algoritmo de Dijkstra

import heapq

def dijkstra(grafo, inicio, fim):
    fila = [(0, inicio)]  # (custo, vértice)
    distancias = {v: float('inf') for v in grafo}
    distancias[inicio] = 0
    caminhos = {v: None for v in grafo}

    while fila:
        custo_atual, vertice_atual = heapq.heappop(fila)

        if vertice_atual == fim:
            caminho = []
            while vertice_atual is not None:
                caminho.append(vertice_atual)
                vertice_atual = caminhos[vertice_atual]
            return caminho[::-1]  # Retorna o caminho invertido

        for vizinho, custo in grafo[vertice_atual].items():
            novo_custo = custo_atual + custo
            if novo_custo < distancias[vizinho]:
                distancias[vizinho] = novo_custo
                caminhos[vizinho] = vertice_atual
                heapq.heappush(fila, (novo_custo, vizinho))

    return None  # Se não houver caminho

# Exemplo de uso
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 3},
    'C': {'D': 2},
    'D': {}
}
caminho = dijkstra(grafo, 'A', 'D')
print("Caminho mais curto:", caminho)