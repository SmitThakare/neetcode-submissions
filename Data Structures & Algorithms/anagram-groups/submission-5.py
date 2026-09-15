class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final=defaultdict(list)
        for i in strs:
            sorted_char=sorted(i)
            sorted_str="".join(sorted_char)
            if sorted_str not in final:
                final[sorted_str]=[i]
            else:
                final[sorted_str].append(i)
        return list(final.values())
            