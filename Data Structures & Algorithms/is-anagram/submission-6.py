class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1={}
        seen2={}
        for i in s:
            seen1[i]=seen1.get(i, 0)+1
        for j in t:
            seen2[j]=seen2.get(j, 0)+1
        if seen1==seen2:
            return True 
        else: 
            return False