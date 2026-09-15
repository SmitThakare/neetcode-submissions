class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=defaultdict(int)
        for i in nums:
            hashmap[i]+=1
        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        arr=[]
        for i in range(k):
            arr.append(sorted_items[i][0])
        return arr