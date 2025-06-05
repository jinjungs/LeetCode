from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def out(x: int, y:int) -> bool:
            return x <0 or x>=len(board) or y<0 or y>=len(board[0])
            
        def dfs(w:str, x:int, y:int) -> bool:
            if w == "":
                return True
            if out(x,y) or w[0] != board[x][y]:
                return False
            temp = board[x][y]    
            board[x][y] = '#' # visited

            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if dfs(w[1:], nx, ny):
                    return True

            board[x][y] = temp # restore
            return False

        d = [(0,1), (0,-1), (1,0), (-1,0)]

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    if dfs(word, x, y):
                        return True
        return False
