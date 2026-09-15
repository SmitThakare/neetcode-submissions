class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows//2):
            matrix[i],matrix[rows-i-1]=matrix[rows-i-1],matrix[i]
        for i in range(rows):
            for j in range(i+1,rows):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]