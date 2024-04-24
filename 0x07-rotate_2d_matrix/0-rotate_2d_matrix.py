#!/usr/bin/python3
""" 0-rotate_2d_matrix.py """


def rotate_2d_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        """ Step 1: Transpose the matrix """
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        """  Reverse each row """
        matrix[i] = matrix[i][::-1]
