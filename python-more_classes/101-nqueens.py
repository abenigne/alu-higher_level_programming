#!/usr/bin/python3
"""Solves the N queens puzzle.

Determines all possible solutions to placing N non-attacking
queens on an N×N chessboard.

Usage:
    nqueens N

N must be an integer greater than or equal to 4.
"""
import sys


def init_board(n):
    """Initialize an empty NxN board represented as a list of lists."""
    return [[0 for _ in range(n)] for _ in range(n)]


def board_deepcopy(board):
    """Return a deep copy of the board."""
    return [row[:] for row in board]


def get_solution(board):
    """Convert the board into the [row, col] solution format."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 1:
                solution.append([r, c])
    return solution


def xout(board, row, col):
    """Mark all spaces that are threatened by a queen at row, col."""
    n = len(board)
    for c in range(n):
        board[row][c] = 1
    for r in range(n):
        board[r][col] = 1

    r = row - 1
    c = col - 1
    while r >= 0 and c >= 0:
        board[r][c] = 1
        r -= 1
        c -= 1

    r = row + 1
    c = col + 1
    while r < n and c < n:
        board[r][c] = 1
        r += 1
        c += 1

    r = row - 1
    c = col + 1
    while r >= 0 and c < n:
        board[r][c] = 1
        r -= 1
        c += 1

    r = row + 1
    c = col - 1
    while r < n and c >= 0:
        board[r][c] = 1
        r += 1
        c -= 1

    board[row][col] = 2


def recursive_solve(board, row, queens, solutions):
    """Recursively attempt to place a queen in every row."""
    n = len(board)
    if row == n:
        if queens == n:
            solutions.append(get_solution(board))
        return

    for col in range(n):
        if board[row][col] == 0:
            board_copy = board_deepcopy(board)
            xout(board_copy, row, col)
            recursive_solve(board_copy, row + 1, queens + 1, solutions)


def nqueens(n):
    """Set up the board and run the backtracking solver."""
    board = init_board(n)
    solutions = []
    recursive_solve(board, 0, 0, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
