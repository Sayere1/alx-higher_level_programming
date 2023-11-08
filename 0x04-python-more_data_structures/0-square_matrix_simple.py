#!/usr/bin/python3

# function that computes the square value of all integers of a matrix
# args: Matrix: contain list of square
# Return: Matrix

def square_matrix_simple(matrix=[]):
    return ([list(map(lambda x: x * x, row)) for row in matrix])
