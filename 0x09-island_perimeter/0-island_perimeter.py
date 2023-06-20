#!/usr/bin/python3
""" Module For Island perimeter
"""


def island_perimeter(grid):
    """ Function to return the perimeter of the island in grid
    """
    perimeter = 0
    no_of_boxes = 0
    sides = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                no_of_boxes += 1
                # Check left and up for connected sides
                if (i > 0) and (grid[i - 1][j] == 1):
                    sides += 1
                if (j > 0) and (grid[i][j - 1] == 1):
                    sides += 1
    # Calculate perimeter based on the formula below
    perimeter = (no_of_boxes * 4) - (sides * 2)
    return perimeter
