class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            leftar = [1] * len(nums)
            rightar = [1] * len(nums)
            output = [1] * len(nums)
            for i in range(1,len(nums)):
                leftar[i]=leftar[i-1]*nums[i-1]
            for i in range(len(nums)-2,-1,-1):
                rightar[i]=rightar[i+1]*nums[i+1]
            for i in range(len(nums)):
                output[i] = leftar[i] * rightar[i]
            return output
