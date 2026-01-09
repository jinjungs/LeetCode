from heapq import heappush, heappop
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # greedy
        h = []
        if a > 0: heappush(h, (-a, 'a'))
        if b > 0: heappush(h, (-b, 'b'))
        if c > 0: heappush(h, (-c, 'c'))

        res = []
        while h:
            val, ch = heappop(h)
            if len(res) >= 2 and res[-2] == res[-1] == ch:
                if not h:
                    break
                val2, ch2 = heappop(h)
                res.append(ch2)
                val2 += 1
                if val2 < 0:
                    heappush(h, (val2, ch2))
            else:
                res.append(ch)
                val += 1

            if val < 0:
                heappush(h, (val, ch))

        return ''.join(res)

        