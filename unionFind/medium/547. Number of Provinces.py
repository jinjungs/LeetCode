from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]

        def find(x):
            if x!= parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i,j)
        
        return len(set(find(i) for i in range(n)))
