class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=len(board)
        col=len(board[0])
        for i in range(row):
            seen=set()
            for j in range(col):
                value= board[i][j]
                if value=='.':
                    continue
                if value in seen:
                    return False
                else:
                    seen.add(value)

        for i in range(col):
            seen=set()
            for j in range(row):
                value= board[j][i]
                if value=='.':
                    continue
                if value in seen:
                    return False
                else:
                    seen.add(value)
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen=set()
                for i in range(box_row, box_row+3):
                    for j in range(box_col, box_col+3):
                        value= board[i][j]
                        if value=='.':
                            continue
                        if value in seen:
                            return False
                        else:
                            seen.add(value)
        return True
                
                



        