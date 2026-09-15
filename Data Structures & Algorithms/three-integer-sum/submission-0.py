class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the array
        nums.sort()
        result = []
        
        # Step 2: Loop through each number as the first element
        for i in range(len(nums)):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Step 3: Use two pointers to find the other two
            left = i + 1
            right = len(nums) - 1
            target = -nums[i]  # We need b + c = -a
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    # Found a triplet!
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # But wait - we need to skip duplicates here too!
                    # Move left forward, but skip duplicates
                    # Move right backward, but skip duplicates
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                # Skip right duplicates  
                    while left < right and nums[right] == nums[right+1]:
                          right -= 1
                                    
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result