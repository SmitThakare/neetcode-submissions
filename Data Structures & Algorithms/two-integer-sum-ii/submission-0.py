class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left]+numbers[right]  # calculate the sum
            
            if current_sum == target:
                # Found it! But remember: return 1-indexed!
                return [left + 1, right + 1]
            elif current_sum < target:
                left+=1  # move which pointer?
            else:
                right-=1  # move which pointer?