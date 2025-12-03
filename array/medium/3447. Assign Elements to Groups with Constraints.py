from typing import List

class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        # 에라토스테네스의 체
        mg = max(groups)
        mark = [-1] * (mg+1)

        for i, ele in enumerate(elements):
            if ele > mg or mark[ele] != -1:
                continue
            for k in range(ele, mg+1, ele):
                if mark[k] == -1:
                    mark[k] = i
        
        n = len(groups)
        assigned = [-1] * n
        
        for i in range(n):            
            assigned[i] = mark[groups[i]]

        return assigned
