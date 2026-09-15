class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row,col=len(grid),len(grid[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        island=0
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            grid[r][c]="0"
            while q:
                curr_rows,curr_cols=q.popleft()
                for dr,dc in directions:
                    nr,nc=dr+curr_rows,dc+curr_cols
                    if nr<0 or nc<0 or nr>=row or nc>=col or grid[nr][nc]=="0":
                        continue 
                    q.append((nr,nc))
                    grid[nr][nc]="0"
                    

        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1" :
                    bfs(r,c)
                    island+=1
        return island