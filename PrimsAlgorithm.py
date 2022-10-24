

INF = float('inf')

G = [[0, 2, 7, 5, 4, 1],
    [2, 0, 4, INF, 5, INF],
    [7, 4, 0, 3, INF, INF],
    [5, INF, 3, 0, INF, 3],
    [4, 5, INF, INF, 0, 6],
    [1, INF, INF, 3, 6, 0]]


def children(curr):
    return [[curr, j, G[0][j]] for j in range(n) if G[curr][j] < INF and G[curr][j] > 0]



n = len(G)

unconnected = set([i for i in range(n)])
edges_ans = []

curr = 0
unconnected.remove(0)
candidates = children(curr)

while(len(unconnected) > 0):

    candidates.sort(key=lambda x: x[2])

    for arr in candidates:
        curr_node = arr[0]
        potential_conn = arr[1]
        if potential_conn in unconnected:
            
            edges_ans.append([curr_node, potential_conn])
            unconnected.remove(potential_conn)
            candidates += candidates + children(potential_conn)
            break


print(edges_ans)


















