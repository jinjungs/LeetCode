from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}  # key: tuple(cells), value: day index
        states = []  # list of unique states (as tuple)

        for day in range(n):
            key = tuple(cells)
            if key in seen:
                # cycle detected
                cycle_len = day - seen[key]
                remaining = (n - seen[key]) % cycle_len
                return list(states[seen[key] + remaining])
            
            seen[key] = day
            states.append(key)

            new_cells = [0] * 8
            for i in range(1, 7):
                new_cells[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            cells = new_cells

        return cells