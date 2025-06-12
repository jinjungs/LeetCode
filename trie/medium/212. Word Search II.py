from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # Store full word at the end node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def out(x,y) -> bool:
            return x<0 or y<0 or x>=HOR or y>=VER

        root = TrieNode()

        # Build Trie
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = word

        HOR, VER = len(board), len(board[0])
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        res = []

        def dfs(x,y,node):
            char = board[x][y]
            if char not in node.children:
                return
            next_node = node.children[char]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None # Avoid duplicates
            
            board[x][y] = '#' # Mark visited
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not out(nx,ny) and board[nx][ny] != '#':
                    dfs(nx,ny,next_node)
            board[x][y] = char # Restore
            
        for x in range(HOR):
            for y in range(VER):
                dfs(x,y,root)
        return res
    