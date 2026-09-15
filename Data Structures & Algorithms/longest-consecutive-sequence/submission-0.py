class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        # Step 1: Create the set
        num_set = set(nums)
        
        max_length = 0
        
        # Step 2: Loop through each number
        for num in num_set:
            # Step 3: Is this a sequence start?
            if (num - 1) not in num_set:
                # Step 4: Count the sequence length
                current = num
                length = 1
                
                # Keep checking num+1, num+2, ...
                while (current + 1) in num_set:
                    current+=1
                    length+=1
                
                # Step 5: Update max_length
                max_length = max(length,max_length)
        
        return max_length