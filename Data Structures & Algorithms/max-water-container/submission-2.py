class Solution:
    def maxArea(self, heights: List[int]) -> int:
        height1=0
        height2=len(heights)-1
        length=0
        breadth=0
        vol=0
        max_vol=0
        while height1<height2:
            length=height2-height1
            breadth=min(heights[height2],heights[height1])
            vol=length*breadth
            max_vol=max(max_vol,vol)
            if breadth==heights[height1]:
                height1 += 1
            else:
                height2 -= 1
        return max_vol