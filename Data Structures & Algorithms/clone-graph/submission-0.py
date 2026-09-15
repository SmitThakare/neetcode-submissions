"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldtonew={}
        q=deque([node])
        oldtonew[node]=Node(node.val)
        while q:
            cur=q.popleft()
            for neighbour in cur.neighbors:
                if neighbour not in oldtonew:
                    oldtonew[neighbour]=Node(neighbour.val)
                    q.append(neighbour)
                oldtonew[cur].neighbors.append(oldtonew[neighbour])
        return oldtonew[node]
