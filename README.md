# N-Queens Algorithm

This project implements the **N-Queens problem** using a **Depth-First Search (DFS)** approach with backtracking.

## Problem

The N-Queens problem requires placing `N` queens on an `N × N` chessboard so that no two queens can attack each other.

Queens must not share:

* The same row
* The same column
* The same diagonal

Each solution is represented as a list where the value at index `i` represents the column position of the queen in row `i`.

For example, one solution for a 4 × 4 board is:

```text
[1, 3, 0, 2]
```

This represents:

```text
. Q . .
. . . Q
Q . . .
. . Q .
```

## Algorithm

The solution uses DFS with backtracking:

1. Start from the first row.
2. Try placing a queen in each available column.
3. Check whether the position is safe.
4. If it is safe, continue to the next row.
5. If all queens are placed, store the solution.
6. If no valid position is available, backtrack and try another position.

## Function

```python
dfs_n_queens(n)
```

### Parameters

* `n` — The size of the chessboard and the number of queens.

### Returns

A list containing all valid N-Queens solutions.

If `n < 1`, the function returns an empty list.

## Example

```python
print(dfs_n_queens(4))
```

Output:

```text
[[1, 3, 0, 2], [2, 0, 3, 1]]
```

## Technologies

* Python
* Depth-First Search (DFS)
* Backtracking
* Recursion
* Algorithmic problem solving
