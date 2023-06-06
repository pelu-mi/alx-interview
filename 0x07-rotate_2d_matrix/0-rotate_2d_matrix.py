#!/usr/bin/python3
""" Module to rotate 2-d matrix clockwise by 90 degrees
"""


def rotate_2d_matrix(matrix):
    """ Function to rotate the matrix
    """
    '''
    # Long method
    size = len(matrix)
    new = []
    for i in range(size):
        row = []
        for j in range(size):
            row.insert(0, matrix[j][i])
        new.append(row)
    del matrix[:]
    matrix.extend(new)
    '''
    # Short method
    new_list = list(zip(*matrix[::-1]))
    new_list = list(map(lambda x: list(x), new_list))
    # Store new list in original matrix
    del matrix[:]
    matrix.extend(new_list)
