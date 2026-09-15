class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for word in strs:
            sortedWord= ''.join(sorted(word))
            if sortedWord in map:
                map[sortedWord].append(word)
            else:
                map[sortedWord] = [word]
        return list(map.values())