
INF = float('inf')

def get_children(u, G, nv):
    return [i for i in range(nv) if G[u][i] != INF and G[u][i] != 0]


def set_dist(s, G, nv):
    return [G[s][i] for i in range(nv)]


def dijkstra(s, G, nv):
    previous = [s for i in range(nv)]

    distance = set_dist(s, G, nv)

    Q = [i for i in range(nv) if i != s]

    while(len(Q)!= 0):
        u = Q.pop()

        for v in get_children(u, G, nv):
            tmp_d = distance[u] + G[u][v]
            if tmp_d < distance[v]:
                distance[v] = tmp_d
                previous[v] = u

    return distance, previous

G = [[0, 2, 7, 5, 4, 1],
    [2, 0, 4, INF, 5, INF],
    [7, 4, 0, 3, INF, INF],
    [5, INF, 3, 0, INF, 3],
    [4, 5, INF, INF, 0, 6],
    [1, INF, INF, 3, 6, 0]]

nv = len(G)


dvr = []

for j in range(nv):
    s = j
    distance, previous = dijkstra(s, G, nv)

    dvr.append(distance)

print(dvr)



