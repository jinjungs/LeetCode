import heapq

# Visited
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

# No Visited
def dijkstra2(graph, s):
    INF = 10**15
    dist = {v: INF for v in graph}
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)

        # Skip if we already found a shorter path to u
        if d > dist[u]:
            continue

        for v, w in graph[u]:  # Explore all outgoing edges from u
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist