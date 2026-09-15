class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        ordered = sorted(count.items(), key=lambda pair: pair[1], reverse=True)
        arr=[]
        for i in range(k):
            arr.append(ordered[i][0])
        return arr
            
