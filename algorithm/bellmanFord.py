def bellman_ford(vertices, edges, source):
    """
    vertices: iterable of vertex ids (e.g., ['s','a','b'])
    edges: iterable of (u, v, w) directed edges with weight w
    source: start vertex
    returns: (dist, parent, has_negative_cycle)
    """
    INF = 10**15
    dist = {v: INF for v in vertices}
    parent = {v: None for v in vertices}
    dist[source] = 0

    # Relax all edges V-1 times
    for _ in range(len(vertices) - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:
            break  # Early stop if no changes

    # One more pass: if we can still relax, there is a negative cycle
    has_negative_cycle = False
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            has_negative_cycle = True
            break

    return dist, parent, has_negative_cycle