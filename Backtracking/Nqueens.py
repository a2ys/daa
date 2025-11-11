def isSafe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solveNQueens(n):
    board = [[0] * n for _ in range(n)]

    def solve(row):
        if row == n:
            for r in board:
                print(" ".join("Q" if x else "." for x in r))
            print()
            return
        
        for col in range(n):
            if isSafe(board, row, col, n):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)

solveNQueens(4)

