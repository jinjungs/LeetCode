from typing import List


class Solution:

    # dp
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return True

        # visited
        visited = [False for _ in range(len(nums))]

        def dfs(i: int) -> bool:
            if visited[i]:
                return False
            if i + nums[i] >= (len(nums) -1):
                return True
            if nums[i] == 0:
                visited[i] = True
                return False

            for j in range(1, nums[i]+1):
                if dfs(i+j):
                    return True

            visited[i] = True
            return False

        return dfs(0)


    # simple solution
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return True

        maxIndex = 0
        for i in range(len(nums)):
            num = nums[i]
            if i + num >= len(nums) -1:
                return True
            maxIndex = max(i + num, maxIndex)
            if maxIndex == i:
                return False
            
    # 25/06/23 Greedy
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0