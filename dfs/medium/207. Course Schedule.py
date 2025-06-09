from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Graph to store the adjacency list of courses
        graph = defaultdict(list)

        # Build the graph from prerequisites
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # States: 0 = unvisited, 1 = visiting, 2 = visited
        visit = [0] * numCourses

        # Helper function to perform DFS
        def dfs(course):
            if visit[course] == 1:  # Cycle detected
                return False
            if visit[course] == 2:  # Already visited, no need to process again
                return True

            # Mark as visiting
            visit[course] = 1

            # Visit all the neighbors (prerequisite courses)
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            # Mark as visited
            visit[course] = 2
            return True

        # Check each course
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

# Solved: 25/06/08
class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites or not numCourses:
            return True

        # make map: key: course value: list of prerequisites
        d = defaultdict(list)
        for pre in prerequisites:
            d[pre[0]].append(pre[1])

        # detect cycle
        visited = set()
        def dfs(course: int) -> bool:
            if course in visited:
                return False
            if len(d[course]) == 0:
                return True

            visited.add(course)
            for pre in d[course]:
                if not dfs(pre):
                    return False
            d[course] = []
            visited.remove(course)
            return True
            
        k = list(d.keys())
        for course in k:
            if not dfs(course):
                return False
        return True
        