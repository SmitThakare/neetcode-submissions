class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr=[]
        right=0
        while right + k <= len(nums):
            max_num= float('-inf')
            for i in range(right, right+k):
                max_num=max(max_num,nums[i])
            right=right+1
            arr.append(max_num)
        return arr
            