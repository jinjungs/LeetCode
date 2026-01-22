from collections import deque, defaultdict
from typing import List
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # connected graph - dfs, bfs
        # complete
        # connected verticles: total number of graph - 1
        # graph, key: verticle, value: the set of connected components
        
        # 2) how we detect each graphs? -> dfs -> collect nodes
        # connected = [[5], [0,1,2], [3,4]]
        # complete_connected -> in connected, count each node's is equal to len(connected[i])

        # 1) create graph
        graph = defaultdict(set)
        for s,e in edges:
            graph[s].add(e)
            graph[e].add(s)

        # 2) detect connection - BFS
        connected = []
        visited = [False] * n
        q = deque()

        for i in range(n):
            if visited[i]:
                continue

            visited[i] = True
            q.append(i)
            nodes = []

            while q:
                node = q.popleft()
                nodes.append(node)

                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)

            connected.append(nodes)

        # 3) complete connected
        res = 0
        for g in connected:
            complete = True
            nodeCount = len(g)
            # count of connected edges are equal to (node count - 1)
            for node in g:
                if len(graph[node]) != (nodeCount - 1):
                    complete = False
                    break
            
            if complete:
                res += 1

        return res
