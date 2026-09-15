class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_duplicates(elements):
            seen=set()
            for num in elements:
                if num ==".":
                    continue
                if num in seen:
                    return True 
                seen.add(num)
            return False
        for row in board:
            if has_duplicates(row):
                return False
        for col in range(9):
            column=[]
            for row in range(9):
                column.append(board[row][col])
            if has_duplicates(column):
                return False
        for box_row in range(3):      # 0, 1, 2 (3 box rows)
            for box_col in range(3):  # 0, 1, 2 (3 box cols)
        # Now extract THIS specific box
                start_row = box_row * 3  # 0, 3, or 6
                start_col = box_col * 3  # 0, 3, or 6
        
                box_elements = []
                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                         box_elements.append(board[row][col])
        
                if has_duplicates(box_elements):
                     return False
            return True
            
