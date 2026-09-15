class TrieNode:
    def __init__(self):
        self.children={}
        self.isend=False
    def addword(self, word):
        cur=self
        for i in word:
            if i not in cur.children:
                cur.children[i]=TrieNode()
            cur=cur.children[i]
        cur.isend=True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for word in words:
            root.addword(word)
        row=len(board)
        col=len(board[0])
        res,visit=set(),set()

        def dfs(r,c,node,word):
            if (r<0 or c<0 or r>=row or c>=col or board[r][c] not in node.children or (r,c) in visit):
                return 
            visit.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.isend:
                res.add(word)
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)
            visit.remove((r,c))
        for r in range(row):
            for c in range(col):
                dfs(r,c,root,"")
        return list(res)



            
        