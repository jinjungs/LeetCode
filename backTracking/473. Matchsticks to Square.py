from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        
        side = s // 4
        matchsticks.sort(reverse=True)

        if matchsticks[0] > side:
            return False

        sides = [0,0,0,0]

        def dfs(i: int) -> bool:
            if i == len(matchsticks):
                return True

            used = set()
            for j in range(4):
                if sides[j] + matchsticks[i] > side:
                    continue
                if sides[j] in used:
                    continue
                
                used.add(sides[j])
                sides[j] += matchsticks[i]

                if dfs(i + 1):
                    return True

                sides[j] -= matchsticks[i]

                # 빈 변에 넣었다가 실패하면 다른 빈 변도 볼 필요 없음
                if sides[j] == 0:
                    break

            return False

        return dfs(0)
