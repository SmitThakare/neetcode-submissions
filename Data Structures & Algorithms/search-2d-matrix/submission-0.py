class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        start=0
        end=rows-1
        while start<=end:
            middle=(start+end)//2
            if matrix[middle][0] <=target<=matrix[middle][cols-1]:
                s1=0
                e1=cols-1
                while s1<=e1:
                    m1=(s1+e1)//2
                    if matrix[middle][m1]==target:
                        return True 
                    elif matrix[middle][m1]<target:
                        s1=m1+1
                    else:
                        e1=m1-1
                return False
            elif matrix[middle][0] >=target:
                end=middle-1
            else:
                start=middle+1
        return False
                    
