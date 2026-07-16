
def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):

    if row == n:
        print(f"\nSolution {solve.count}:")
        solve.count += 1

        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        return

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = 1

            solve(board, row + 1, n)

            # Backtrack
            board[row][col] = 0


# Driver Code
n = 4
board = [[0] * n for _ in range(n)]

solve.count = 1
solve(board, 0, n)
