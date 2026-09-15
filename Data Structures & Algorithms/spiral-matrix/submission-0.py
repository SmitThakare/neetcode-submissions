class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows=len(matrix)
        cols=len(matrix[0])
        result=[]
        rows_up=0
        rows_down=rows-1
        cols_left=0
        cols_right=cols-1
        while rows_up<=rows_down and cols_left<=cols_right:
            for i in range(cols_left,cols_right+1):
                result.append(matrix[rows_up][i])
            rows_up+=1
            for i in range(rows_up,rows_down+1):
                result.append(matrix[i][cols_right])
            cols_right-=1
            if rows_up <= rows_down:
                for i in range(cols_right,cols_left-1,-1):
                    result.append(matrix[rows_down][i])
                rows_down-=1
            if cols_left <= cols_right:
                for i in range(rows_down,rows_up-1,-1 ):
                    result.append(matrix[i][cols_left])
                cols_left+=1
        return result 
            
            
            