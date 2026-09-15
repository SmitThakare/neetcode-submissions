class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for word in strs:
            s = ''.join(sorted(word))
            if s in hashmap:
                hashmap[s].append(word)
            else:
                hashmap[s]=[]
                hashmap[s].append(word)
        return list(hashmap.values())