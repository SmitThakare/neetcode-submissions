class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for num in nums:
            if num in map:
                map[num]+=1
            else:
                map[num]=1
        sorted_items = sorted(map.items(), key=lambda x: x[1], reverse=True)
        top_k_items = sorted_items[:k]
        result = [item[0] for item in top_k_items]
        return result