class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            current_value = nums[i]
            complement = target - current_value
            if complement in hashmap:
                previous_index = hashmap[complement]
                return [previous_index, i]
            hashmap[current_value] = i