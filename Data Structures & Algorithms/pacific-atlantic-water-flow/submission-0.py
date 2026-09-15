class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return 0
        pacific=set()
        atlantic=set()
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        row,col=len(heights),len(heights[0])
        def dfs(r,c,visited):
            visit=visited
            visit.add((r,c)) 
            for dr,dc in directions:
                nr,nc=dr+r,dc+c
                if nr<0 or nc<0 or nr>=row or nc>=col:
                    continue
                if (nr,nc) in visit:
                    continue
                if heights[r][c]>heights[nr][nc]:
                    continue
                dfs(nr,nc,visit)
                
        for r in range(row):
            dfs(r,0,pacific)
        for c in range(col):
            dfs(0,c,pacific)
        
        for r in range(row):
            dfs(r,col-1,atlantic)
        for c in range(col):
            dfs(row-1,c,atlantic)
        result=pacific.intersection(atlantic)

        return [[r, c] for r, c in result]
        
            