class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preNum={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preNum[crs].append(pre)
        visited=set()
        def dfs(crs):
            if crs in visited:return False
            if preNum[crs]==[]:return True
            visited.add(crs)
            for pre in preNum[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            preNum[crs]=[]
            return True 

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True 