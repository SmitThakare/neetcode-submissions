class Node:
    def __init__(self):
        self.children={}
        self.isendofword=False

class PrefixTree:

    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        currentnode=self.root
        for i in word:
            if i not in currentnode.children:
                currentnode.children[i]=Node()
            currentnode=currentnode.children[i]
        currentnode.isendofword=True

    def search(self, word: str) -> bool:
        currentnode=self.root
        for i in word:
            if i not in currentnode.children:
                return False
            currentnode=currentnode.children[i]
        return currentnode.isendofword


    def startsWith(self, prefix: str) -> bool:
        currentnode=self.root
        for i in prefix:
            if i not in currentnode.children:
                return False
            currentnode=currentnode.children[i]
        return True
        
        