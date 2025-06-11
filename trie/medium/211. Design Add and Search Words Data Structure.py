class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.head = Trie()
        
    def addWord(self, word: str) -> None:
        cur = self.head
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        def dfs(index, cur):
            if not cur:
                return False
            if len(word) - 1 < index:
                return cur.isWord
                
            c = word[index]
            if c == '.':
                for child in cur.children.values():
                    if dfs(index+1, child):
                        return True
                return False
            elif c not in cur.children:
                return False
            else:
                return dfs(index+1, cur.children[c])

        return dfs(0, self.head)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)