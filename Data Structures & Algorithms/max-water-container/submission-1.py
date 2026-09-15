class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        height1 = 0
        height2 = len(heights)-1
        maxwater=0
        while height1<height2:
            distance =height2-height1
            min_height=min(heights[height1],heights[height2])
            wateramt=distance*min_height
            
            maxwater=max(maxwater,wateramt)

            if heights[height1]<heights[height2]:
                height1 += 1
            else:
                height2 -= 1
    
        return maxwater