class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, path, cur_sum):
            # BASE CASE 1: Found target!
            if cur_sum == target:
                result.append(path[:])  # Copy or reference?
                return
            
            # BASE CASE 2: Exceeded target (PRUNING!)
            if cur_sum > target:
                return 
            
            # RECURSIVE CASE: Try each number from start onwards
            for i in range(start, len(nums)):
                # CHOOSE
                path.append(nums[i])
                
                # EXPLORE (can reuse same number, so pass i not i+1!)
                backtrack(i, path, cur_sum + nums[i])
                
                # UNCHOOSE (backtrack!)
                path.pop()
        
        backtrack(0, [], 0)
        return result