
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = dict()
        d['2'] = ['a','b','c']
        d['3'] = ['d','e','f']
        d['4'] = ['g','h','i']
        d['5'] = ['j','k','l']
        d['6'] = ['m','n','o']
        d['7'] = ['p','q','r','s']
        d['8'] = ['t','u','v']
        d['9'] = ['w','x','y','z']
        
        arr = list(digits)
        n = len(arr)
        if n == 0:
            return arr
        elif n == 1:
            return d[arr[0]]

        def comb(a:list[str], b:list[str]) -> list[str]:
            result = []
            for i in a:
                for j in b:
                    result.append(i+j)

            return result

        def recursive(m:int):
            if m <= 2:
                return comb(d[arr[n-m]], d[arr[n-m+1]])

            return comb(d[arr[n-m]], recursive(m-1))
                    
        return recursive(n)