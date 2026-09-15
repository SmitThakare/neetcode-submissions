class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(start,path,cur_sum):
            if cur_sum==target:
                result.append(path[:])
            if cur_sum>target:
                return 
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path, cur_sum+nums[i])
                path.pop()
        backtrack(0,[],0)
        return result