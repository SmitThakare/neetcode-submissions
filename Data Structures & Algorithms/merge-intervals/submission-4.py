class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        merged=[intervals[0]]
        n=len(intervals)
        for i in range(1,n):
            current=intervals[i]
            prev=merged[-1]
            if current[0]<=prev[1]:
                prev[1]=max(current[1],prev[1])
            else:
                merged.append(current)
        return merged


