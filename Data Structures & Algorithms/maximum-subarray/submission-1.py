class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        right=0
        maxSum=nums[0]
        cur_sum=0
        length=len(nums)-1
        while right<=length:
            cur_sum=cur_sum+nums[right]
            maxSum=max(maxSum,cur_sum)
            if cur_sum<0:
                cur_sum=0

            right=right+1
            
            
        return maxSum