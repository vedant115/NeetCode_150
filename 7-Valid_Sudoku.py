# 36. Valid Sudoku

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

# method 1
import collections
def isValidSudoku(board):
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    sqrs = collections.defaultdict(set)
        
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (
                board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in sqrs[(r//3, c//3)]
            ):
                return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            sqrs[(r//3, c//3)].add(board[r][c])
    return True

# method 2
def isValidSudoku(board):
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        squareSet = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": 
                    continue
                    
                sr, sc = r // 3, c // 3
                sPos = sr * 3 + sc
                
                if (
                    board[r][c] in rowSet[r] or 
                    board[r][c] in colSet[c] or 
                    board[r][c] in squareSet[sPos]
                ):
                    return False

                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                squareSet[sPos].add(board[r][c])

        return True