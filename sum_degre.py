import  numpy as np

from gerador_de_grafro_bipartido import create_bipartite_graph

create_bipartite_graph(3,3 )

nos = {}

def sum_degree(graph):
    nosIndex = 0;
    for node in graph:
        nos[nosIndex] = 0
        for edge in node:
            nos[nosIndex] += edge
        nosIndex = nosIndex + 1


sum_degree(create_bipartite_graph(2, 3))

print(nos)

# Saída
# {0: 3, 1: 3, 2: 2, 3: 2, 4: 2}
# cada chave representa um nó, portanto a chave 0 representa o nó 0 e valor inserido representa a quantidade de graus daquele nó
