import copy


INF = float('inf')

G = [[0, 2, 7, 5, 4, 1],
    [2, 0, 4, INF, 5, INF],
    [7, 4, 0, 3, INF, INF],
    [5, INF, 3, 0, INF, 3],
    [4, 5, INF, INF, 0, 6],
    [1, INF, INF, 3, 6, 0]]


n = len(G)

dp = [[[INF for i in range(n)] for j in range(n)] for k in range(n)]

dp[0] = G

for k in range(1, n):
    for i in range(n):
        for j in range(n):
            dp[k][i][j] = min(dp[k-1][i][j], dp[k-1][i][k] + dp[k-1][k][j])


print(dp[n-1])













