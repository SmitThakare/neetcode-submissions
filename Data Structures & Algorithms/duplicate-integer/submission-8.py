class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for i in range(len(nums)):
            seen.add(nums[i])
        if len(seen)==len(nums):
            return False
        else:
            return True 