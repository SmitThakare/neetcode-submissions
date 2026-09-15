class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        
        index=0
        final=[0]*length
        while index<=length-1:
            left_product=1
            right_product=1
            for i in range(index):
                left_product=left_product*nums[i]
            for i in range(index+1,length):
                right_product=right_product*nums[i]
            final[index]=left_product*right_product
            index+=1
        return final            
        