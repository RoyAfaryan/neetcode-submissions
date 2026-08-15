class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Logic:
        # 1. Create 3 hashmaps: row, column, square
        # 2. Iterate through board and place each number (key) with its position with respect to the hashmap its going into (value). 
        # 3. If any duplicate exists, return false
        # 4. If no duplicates, return true

        row, col, square = defaultdict(int), defaultdict(int), defaultdict(int)
        
        for i in range(9):

            for j in range(9):
                if board[i][j] != '.':
                    
                    if row.get(board[i][j]) == i: 
                        return False
                    if col.get(board[i][j]) == j:
                        return False
                    if square.get(board[i][j]) == int((i // 3) * 3 + (j // 3)):
                        return False
                
                    row[board[i][j]] = i
                    col[board[i][j]] = j
                    square[board[i][j]] = int((i // 3) * 3 + (j // 3))

        return True


