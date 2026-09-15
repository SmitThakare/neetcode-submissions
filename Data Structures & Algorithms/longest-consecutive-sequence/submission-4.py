class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        final_num=set(nums)
        longest=0
        for i in nums:
            if i-1 not in  final_num:
                current_num=i
                current=1
                while current_num+1 in final_num:
                    current_num+=1
                    current+=1
                longest=max(longest,current)
        return longest
