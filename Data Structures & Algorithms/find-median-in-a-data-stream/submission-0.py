class MedianFinder:

    def __init__(self):
        self.lo=[]
        self.high=[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)

        if self.lo and self.high and (-self.lo[0] > self.high[0]):
            val = -heapq.heappop(self.lo)
            heapq.heappush(self.high, val)
        
        if len(self.lo) > len(self.high) + 1:
            val = -heapq.heappop(self.lo)
            heapq.heappush(self.high, val)
        
        if len(self.high) > len(self.lo):
            val = heapq.heappop(self.high)
            heapq.heappush(self.lo, -val)


    def findMedian(self) -> float:
            if len(self.lo) == len(self.high):
                return (-self.lo[0] + self.high[0]) / 2.0
            # Otherwise, lo has one more element
            else:
                return float(-self.lo[0])