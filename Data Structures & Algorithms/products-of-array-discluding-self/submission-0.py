class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
        # Step 1
        leftProducts = [1] * n
        for i in range(1, n):
            leftProducts[i] = leftProducts[i-1] * nums[i-1]
        
        # Step 2
        rightProducts = [1] * n
        for i in range(n-2, -1, -1):
            rightProducts[i] = rightProducts[i+1] * nums[i+1]
        
        # Step 3
        output = []
        for i in range(n):
            output.append(leftProducts[i] * rightProducts[i])
        
        return output