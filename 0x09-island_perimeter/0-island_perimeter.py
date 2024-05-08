#!/usr/bin/python3
""" 0-island_perimeter.py """


def island_perimeter(grid):
    """ create method with the name island perimeter """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        """ iterate the row value """
        for j in range(cols):
            """ iterate ihe column value """
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
