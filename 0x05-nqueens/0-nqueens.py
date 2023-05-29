#!/usr/bin/python3
"""Program to solve the N queens problem
Place N non-attacking queens on an NxN chessboard
"""


import sys


def isValid(col_matrix):
    """
    Function to check if matrix is a valid solution

    Args:
        col_matrix (list): List of column values of matrix with each index
        as the corresponding row.

    Returns: True if valid else, False
    """
    posDiag = []
    negDiag = []
    cols = []
    for r in range(0, len(col_matrix)):
        c = col_matrix[r]
        if c in cols or (r + c) in posDiag or (r - c) in negDiag:
            return False
        posDiag.append(r + c)
        negDiag.append(r - c)
        cols.append(c)
    return True


def solveNQueens(n, row, col_matrix, result):
    """Function to solve for NQueens

    Args:
        n (int): Number of rows and columns
        row (int): Value of current row being examined
        col_matrix (list): List of column values of matrix with each index
        as the corresponding row.
        result (list): List of valid answers
    """
    if row == n:
        result.append(list(col_matrix))
    else:
        for col in range(0, n):
            col_matrix.append(col)
            if isValid(col_matrix):
                solveNQueens(n, row + 1, col_matrix, result)
            col_matrix.pop()


""" Command Line input constraints
"""
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    n = int(sys.argv[1])
except Exception as e:
    print("N must be a number")
    exit(1)


if not isinstance(n, int):
    print("N must be a number")
    exit(1)
if n < 4:
    print("N must be at least 4")
    exit(1)

""" Driver Code
"""
res = []
solveNQueens(n, 0, list(), res)
for item in res:
    print("[", end="")
    for i in range(0, len(item)):
        print("[{}, {}]".format(i, item[i]), end="")
        if i != len(item) - 1:
            print(", ", end="")
    print("]")
