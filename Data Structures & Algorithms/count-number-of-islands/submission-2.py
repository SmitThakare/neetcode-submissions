class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island=0
        direction=[[0,1],[1,0],[-1,0],[0,-1]]
        rows,cols=len(grid),len(grid[0])
        seen=set()
        def dfs(r,c):
            seen.add((r,c))
            grid[r][c]=="0"
            for dr,dc in direction:
                nr,nc=dr+r,dc+c
                if nr<0 or nc<0 or nc>=cols or nr>=rows or grid[nr][nc]=="0":
                    continue
                if (nr,nc) in seen:
                    continue
                dfs(nr,nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in seen:
                    dfs(r,c)
                    island+=1
        return island