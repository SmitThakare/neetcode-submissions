class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        first=0
        last=len(cleaned)-1
        while last>first:
            if cleaned[first]==cleaned[last]:
                first+=1
                last-=1
            else: 
                return False
        return True