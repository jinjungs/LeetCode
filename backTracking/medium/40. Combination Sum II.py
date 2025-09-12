from collections import deque
from typing import List
class Solution:
    
    # bfs
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        q = deque([[-1,0,[]]])
        while q:
            for _ in range(len(q)):
                i, num, l = q.popleft()
                for j in range(i+1, n):
                    if j > i+1 and candidates[j-1] == candidates[j]:
                        continue
                    if num + candidates[j] > target:
                        break

                    l_copy = l.copy()
                    l_copy.append(candidates[j])
                    if num + candidates[j] < target:
                        q.append([j, num + candidates[j], l_copy])
                    else:
                        res.append(l_copy)

        return res
    
    # dfs
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        path = []

        
        def dfs(start: int, remain: int) -> None:
            if remain == 0:
                res.append(path[:])
                return
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > remain:
                    break

                path.append(candidates[i])
                dfs(i+1, remain-candidates[i])
                path.pop()
                
        dfs(0,target)
        return res
