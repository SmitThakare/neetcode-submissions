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
            for neighbor in cur.neighbors:
                if neighbor not in oldtonew:
                    oldtonew[neighbor]=Node(neighbor.val)
                    q.append(neighbor)
                oldtonew[cur].neighbors.append(oldtonew[neighbor])
        return oldtonew[node]