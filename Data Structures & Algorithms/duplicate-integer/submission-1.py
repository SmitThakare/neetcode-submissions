class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set=set(nums)

        num_len=len(nums)
        set_len=len(nums_set)
        if num_len==set_len:
            return False
        else:
            return True 