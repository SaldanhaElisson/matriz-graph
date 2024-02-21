import  numpy as np

def create_bipartite_graph(m:int, n:int):
    if(not(m >= 2 | m <= 20)):
        return
    if(not(n >= 2 | n <= 20)):
        return

    graph = np.zeros((n+m, n+m), dtype=int)

    for i in range(0, m):
        for j in range(m, m+n):
            graph[i, j] = 1


    for i in range(m, m+n):
        for j in range(0, m):
            graph[i, j] = 1

    return graph


# print(create_bipartite_graph(10, 19))


# Entrada (2, 3)
# Saída
#     A B C D F G
#  A[[0 0 0 1 1 1]
#  B[0 0 0 1 1 1]
#  C[0 0 0 1 1 1]
#  D[1 1 1 0 0 0]
#  F[1 1 1 0 0 0]
#  G[1 1 1 0 0 0]]
# Para ser grafo bipartido, cada elemento de M = 2, deve se conectar com os elementos de N = 3,
# entretanto os elementos de M não podem se conectaram, nem os elementos de N
#
#


