class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col=len(grid), len(grid[0])
        direction=[[0,1],[1,0],[-1,0],[0,-1]]
        visited=set()
        island=0
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                rows,cols=q.popleft()
                for dr, dc in direction:
                    nr,nc=dr+rows,dc+cols
                    if nr<0 or nc<0  or nr>=row or nc>=col or grid[nr][nc]=="0" or ((nr,nc)) in visited:
                        continue 
                    q.append((nr,nc))
                    visited.add((r,c))
                    grid[nr][nc]="0"


        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    island+=1
        return island