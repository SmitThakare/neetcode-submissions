class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        res=nums[0]
        while start<=end:
            if nums[start]<nums[end]:
                res=min(res, nums[start])
                break
            middle=(start+end)//2
            res=min(res, nums[middle])
            if nums[middle]>=nums[end]:
                start=middle+1
            else:
                end=middle-1
        return res