class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj={i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visited=set()
        def dfs(cur, prev):
            if cur in visited:
                return False
            visited.add(cur)
            for i in adj[cur]:
                if i==prev:
                    continue
                if not dfs(i, cur):
                    return False
            return True
        return dfs(0,-1) and len(visited)==n