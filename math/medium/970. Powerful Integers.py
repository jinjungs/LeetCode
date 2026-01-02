class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        n = 20

        for i in range(n):
            num = x**i
            if num > bound:
                break
            for j in range(n):
                total = num + y**j
                if total > bound:
                    break
                if total not in res:
                    res.add(total)

        return list(res)
    
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()

        xs = [1]
        if x != 1:
            while xs[-1] * x <= bound:
                xs.append(xs[-1] * x)
        
        ys = [1]
        if y != 1:
            while ys[-1] * y <= bound:
                ys.append(ys[-1] * y)

        for a in xs:
            for b in ys:
                if a + b <= bound:
                    res.add(a+b)

        return list(res)