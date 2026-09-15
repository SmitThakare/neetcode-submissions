class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for i in nums:
            seen[i]=seen.get(i, 0)+1
        sorted_seen=sorted(seen, key=lambda x:seen[x], reverse=True)

        return sorted_seen[:k]