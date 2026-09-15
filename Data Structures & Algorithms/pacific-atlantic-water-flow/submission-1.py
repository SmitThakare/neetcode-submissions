class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row,col=len(heights),len(heights[0])
        direction=[[0,1],[1,0],[-1,0],[0,-1]]
        pacific=set()
        atlantic=set()
        def dfs(r,c,visited):
            visited.add((r,c))
            for dr,dc in direction:
                nr,nc=dr+r,dc+c
                if nr<0 or nc<0 or nc>=col or nr>=row:
                    continue
                if (nr,nc) in visited:
                    continue
                if heights[r][c]>heights[nr][nc]:
                    continue
                dfs(nr,nc,visited)

        for r in range(row):
            dfs(r,0,pacific)
        for c in range(col):
            dfs(0,c,pacific)
        for r in range(row):
            dfs(r,col-1,atlantic)
        for c in range(col):
            dfs(row-1,c,atlantic)
        result=pacific.intersection(atlantic)
        return[[r,c] for r,c in result]