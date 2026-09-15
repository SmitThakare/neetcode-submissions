class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        hashmap_s1={}
        for right in range(len(s1)):
            hashmap_s1[s1[right]]=hashmap_s1.get(s1[right],0)+1
        right=0
        while right + len(s1) <= len(s2):
            hashmap={}
            
            for i in range(right, right+len(s1)):
                hashmap[s2[i]]=hashmap.get(s2[i],0)+1
            right=right+1
            if hashmap==hashmap_s1:
                return True 
        else:
                return False    
            