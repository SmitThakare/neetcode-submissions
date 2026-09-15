class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_length = 0
        
        for right in range(len(s)):
            # Add current character to count
            count[s[right]] = count.get(s[right], 0) + 1
            
            # Check if window is invalid
            window_size = right - left + 1
            max_count = max(count.values())
            replacements_needed = window_size - max_count
            
            while replacements_needed > k:
                count[s[left]] -= 1
                left += 1
                window_size = right - left + 1
                max_count = max(count.values())
                replacements_needed = window_size - max_count
            
            # Update max_length
            max_length = max(max_length, right - left + 1)
        
        return max_length