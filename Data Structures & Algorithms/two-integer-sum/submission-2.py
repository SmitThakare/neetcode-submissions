class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for n,i in enumerate(nums):
            if i in seen:
                return [seen[i],n]
            diff=target-i
            seen[diff]=n