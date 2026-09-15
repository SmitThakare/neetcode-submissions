class Node:
    def __init__(self):
        self.children = {}
        self.isend = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = Node()
            current = current.children[ch]
        current.isend = True

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.root)

    def _dfs(self, word, index, node):
        if index == len(word):
            return node.isend

        ch = word[index]

        if ch == ".":
            for child in node.children.values():
                if self._dfs(word, index + 1, child):
                    return True
            return False

        if ch not in node.children:
            return False

        return self._dfs(word, index + 1, node.children[ch])
