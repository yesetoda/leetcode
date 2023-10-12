class Solution(object):
    def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        valids = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        # row check
        for row in range(9):
            for column in range(9):
                if board[row][column] in valids:
                    if board[row].count(board[row][column])>1:
                        return False
        # column check
        for column in range(9):
            col = []
            for row in range(9):
                if board[row][column] in valids:
                    if board[row][column] not in col:
                        col.append(board[row][column])
                    else:
                        return False
        # cell check
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                cell = []
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if board[x][y]!="."  and board[x][y] in cell:
                            return False
                        cell.append(board[x][y])
        return True
        
    print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))