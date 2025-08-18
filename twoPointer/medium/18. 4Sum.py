from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-3):
            # Skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Prune by minimal possible sum with current i
            min_sum = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
            if min_sum > target:
                break  # further i only increases the sum

            # Prune by maximal possible sum with current i
            max_sum = nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3]
            if max_sum < target:
                continue

            for j in range(i+1, n-2):
                # Skip duplicate j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Prune by minimal/maximal possible sum with current (i, j)
                min_sum_j = nums[i] + nums[j] + nums[j + 1] + nums[j + 2]
                if min_sum_j > target:
                    break  # increasing j will only increase min_sum_j
                max_sum_j = nums[i] + nums[j] + nums[n - 1] + nums[n - 2]
                if max_sum_j < target:
                    continue

                l, r = j+1, n-1
                while l < r:
                    fourSum = nums[i] + nums[j] + nums[l] + nums[r]
                    if fourSum == target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif fourSum > target:
                        r -= 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    else:
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1

        return res