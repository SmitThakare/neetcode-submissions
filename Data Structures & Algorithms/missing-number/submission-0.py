class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length=len(nums)
        sum=(length*(length+1))/2
        curr_sum=0
        for i in nums:
            curr_sum+=i
        result=int(sum-curr_sum)
        return result