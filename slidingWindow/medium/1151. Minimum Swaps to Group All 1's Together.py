from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # sliding window which has (total_ones) length
        total_ones = sum(data)
        window_ones = sum(data[:total_ones])
        max_ones = window_ones

        for r in range(total_ones, len(data)):
            window_ones = window_ones - data[r-total_ones] + data[r]
            max_ones = max(max_ones, window_ones)

        return total_ones - max_ones
