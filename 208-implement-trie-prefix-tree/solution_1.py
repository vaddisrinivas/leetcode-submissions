# https://leetcode.com/problems/implement-trie-prefix-tree
# https://leetcode.com/problems/208-implement-trie-prefix-tree
class Node:
    def __init__(self,val=None):
        self.val = val
        self.children = {}
    

class Trie:

    def __init__(self):
        self.trie = Node()

    def insert(self, word: str) -> None:
        word+=";"
        l = len(word)
        def dfs(node,x):
            if x==l:
                return 
            if word[x] not in node.children:
                node.children[word[x]]=Node(word[x])
            return dfs(node.children[word[x]],x+1)
        return dfs(self.trie,0)
        

    def search(self, word: str) -> bool:
        word+=";"
        l = len(word)
        def dfs(node,x):
            if x==l:
                return True
            if word[x] not in node.children:
                return False
            return dfs(node.children[word[x]],x+1)
        return dfs(self.trie,0)


    def startsWith(self, prefix: str) -> bool:
        l = len(prefix)
        def dfs(node,x):
            if x==l:
                return True
            if prefix[x] not in node.children:
                return False
            return dfs(node.children[prefix[x]],x+1)
        return dfs(self.trie,0)
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)