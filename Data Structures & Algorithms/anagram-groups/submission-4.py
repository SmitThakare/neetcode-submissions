class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final={}
        for i in strs:
            key="".join(sorted(i))
            if key in final:
                final[key].append(i)
            else:
                final[key]=[i]
        return list(final.values())