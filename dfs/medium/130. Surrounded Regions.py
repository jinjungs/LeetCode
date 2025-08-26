from ast import List


# original solution
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        HOR = len(board)
        VER = len(board[0])
        dx, dy = [0,1,0,-1], [1,0,-1,0]

        def isEdge(x,y):
            return x < 0 or y < 0 or x >= HOR or y >= VER

        # mark symbols and return if it is surrounded
        # surrounded: surround by 'O' or 'X' or '#'
        # you can mark with '#': visited , OR 'X'
        # have to mark back '#' -> 'O' befor return
        def dfs(x, y, origin, change) -> bool:
            isSurrounded = True
            board[x][y] = change
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if isEdge(nx,ny):
                    isSurrounded = False
                    continue
                if board[nx][ny] == origin:
                    if not dfs(nx,ny,origin,change):
                        isSurrounded = False

            return isSurrounded
        
        # in for loop, check if is surrounded
        markback = False
        for i in range(HOR):
            for j in range(VER):
                if board[i][j] == 'O':
                    surrounded = dfs(i,j,'O','#')
                    if surrounded:
                        dfs(i,j,'#','X')
                    else:
                        markback = True
                    
        # have to mark back '#' -> 'O' before return
        if markback:
            for i in range(HOR):
                for j in range(VER):
                    if board[i][j] == '#':
                        dfs(i,j,'#','O')


# border flood-fill solution
class Solution:
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        HOR = len(board)
        VER = len(board[0])
        dx, dy = [0,1,0,-1], [1,0,-1,0]

        def isEdge(x,y):
            return x < 0 or y < 0 or x >= HOR or y >= VER

        # mark symbols and return if it is surrounded
        # surrounded: surround by 'O' or 'X' or '#'
        # you can mark with '#': visited , OR 'X'
        # have to mark back '#' -> 'O' befor return
        def dfs(x, y, origin, change) -> bool:
            isSurrounded = True
            board[x][y] = change
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if isEdge(nx,ny):
                    isSurrounded = False
                    continue
                if board[nx][ny] == origin:
                    if not dfs(nx,ny,origin,change):
                        isSurrounded = False

            return isSurrounded
        
        # in for loop, check if is surrounded
        markback = False
        for i in range(HOR):
            for j in range(VER):
                if board[i][j] == 'O':
                    surrounded = dfs(i,j,'O','#')
                    if surrounded:
                        dfs(i,j,'#','X')
                    else:
                        markback = True
                    
        # have to mark back '#' -> 'O' before return
        if markback:
            for i in range(HOR):
                for j in range(VER):
                    if board[i][j] == '#':
                        dfs(i,j,'#','O')
