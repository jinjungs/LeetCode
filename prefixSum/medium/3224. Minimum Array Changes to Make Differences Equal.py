from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # change times could be 0,1,2
        change_count = [0] * (k+2) # 0~k (k+1), and we need one more, r+1 when calculate [l,r]
        change_count[0] = n//2 # default consider change 1 time

        # in each pair, mark start, end point in difference array
        for i in range(n//2):
            left = nums[i]
            right = nums[n-1-i]
            curr_diff = abs(left-right)
            max_diff = max(left, right, k-left, k-right)

            change_count[curr_diff] -= 1
            change_count[curr_diff+1] += 1
            change_count[max_diff+1] += 1
            
        # prefix sum
        min_change = n
        curr = 0
        for i in range(k+2):
            curr += change_count[i]
            min_change = min(min_change, curr)

        return min_change

        
