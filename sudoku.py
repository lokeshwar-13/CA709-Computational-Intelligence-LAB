def solve_sudoku(board):

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
              
                for num in range(1, 10):

                    valid = True

                    for j in range(9):
                        if board[row][j] == num:
                            valid = False
                            break
                          
                    if valid:
                        for i in range(9):
                            if board[i][col] == num:
                                valid = False
                                break
                              
                    if valid:
                        start_row = (row // 3) * 3
                        start_col = (col // 3) * 3

                        for i in range(start_row, start_row + 3):
                            for j in range(start_col, start_col + 3):
                                if board[i][j] == num:
                                    valid = False

                    if valid:
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        # Backtrack
                        board[row][col] = 0

                return False

    return True


def print_board(board):
    for row in board:
        print(*row)


# solve karne ke liye
board = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 9, 8, 0, 0, 0, 3, 6],
    [0, 0, 0, 3, 0, 6, 0, 9, 0]
]


print("Original Sudoku:")
print_board(board)

if solve_sudoku(board):
    print("\nSolved Sudoku:")
    print_board(board)
else:
    print("No solution exists.")
