import heapq

def dijkstra(graph, s):
    INF = 10**15
    dist = {v: INF for v in graph}
    dist[s] = 0
    pq = [(0, s)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited: 
            continue
        visited.add(u)              # Mark u as visited (distance d is now 'finalized')

        for v, w in graph[u]:       # Explore all outgoing edges from u
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist