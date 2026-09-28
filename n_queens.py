def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []
    board = []

    def dfs(row):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            # Check whether the column is already occupied.
            if col in board:
                continue

            # Check whether the diagonal is occupied.
            safe = True

            for previous_row, previous_col in enumerate(board):
                if abs(previous_row - row) == abs(previous_col - col):
                    safe = False
                    break

            if not safe:
                continue

            # Place the queen.
            board.append(col)

            # Continue searching the next row.
            dfs(row + 1)

            # Backtrack.
            board.pop()

    dfs(0)
    return solutions
