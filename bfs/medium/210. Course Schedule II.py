from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            degree[a] += 1

        q = deque()
        for course in range(numCourses):
            if degree[course] == 0:
                q.append(course)

        res = []
        while q:
            for _ in range(len(q)):
                course = q.popleft()
                res.append(course)
                for nei in graph[course]:
                    degree[nei] -= 1
                    if degree[nei] == 0:
                        q.append(nei)

        return res if len(res) == numCourses else []