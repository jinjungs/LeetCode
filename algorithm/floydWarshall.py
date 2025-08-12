def floyd_warshall(n, edges):
    """
    n: number of vertices (0..n-1)
    edges: list of (u, v, w) directed edges
    returns: dist (n x n)
    """
    INF = 10**15
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)  # handle multi-edges

    for k in range(n):
        for i in range(n):
            # small prune (optional)
            dik = dist[i][k]
            if dik == INF: 
                continue
            for j in range(n):
                if dik + dist[k][j] < dist[i][j]:
                    dist[i][j] = dik + dist[k][j]

    return dist