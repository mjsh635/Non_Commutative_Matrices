import random
import numpy as np


class Matrix:
    """create a matrix of size row/columns
        create and return all the random values for the matrix
        populate that matrix with random values
        return the matrix
    """

    def __init__(self, rows, columns):
        self.columns = columns
        self.rows = rows
        self.matrix = self._create_empty_matrix(self.rows, self.columns)
        self._populate_matrix(self.matrix, self._random_matrix_values())

    def _create_empty_matrix(self, rows, columns):
        """ Create a matrix of the desired size that is populated
        with zeros
        """
        return np.zeros((rows, columns), dtype=float)

    def _random_matrix_values(self):
        """ return a string of random data to be entered into the maxtrix
        """
        data = []
        for _ in range(self.rows*self.columns):
            data.append(round(random.random(), 2)+random.randint(0, 10))
        return data

    def _populate_matrix(self, matrix, data):
        """ Populate the matrix with the data
        """
        data_index = 0
        for row in range(self.rows):
            for col in range(self.columns):
                matrix[row, col] = data[data_index]
                data_index += 1

    def print_matrix(self):
        """ Returns the matrix
        """
        print(self.matrix)

    def __add__(self, other):
        """ Override the python method for the addition operator to perform
        the proper operations for matrix addition
        """
        if ((self.rows == other.rows) and (self.columns == other.columns)):
            new_matrix = self._create_empty_matrix(self.rows, self.columns)
            for row in range(self.rows):
                for col in range(self.columns):
                    new_matrix[row, col] = (
                        self.matrix[row, col] + other.matrix[row, col])
            return new_matrix
        else:
            return "Matrices sizes don't match"

    def __sub__(self, other):
        """Override the python method for the subtractions operator to perform
        the proper operations for matrix subtractions"""

        if ((self.rows == other.rows) and (self.columns == other.columns)):
            new_matrix = self._create_empty_matrix(self.rows, self.columns)
            for row in range(self.rows):
                for col in range(self.columns):
                    new_matrix[row, col] = (
                        self.matrix[row, col] - other.matrix[row, col])
            return new_matrix
        else:
            return "Matrices sizes don't match"

    def __mul__(self, other):
        """Override the python method for the multiplication operator to
        perform the proper operations for matrix multiplication
        """
        if (self.columns == other.rows):
            new_matrix = self._create_empty_matrix(self.rows, other.columns)
            matrix_one_row = 0  # mat row
            matrix_one_column = 0  # mat col
            matrix_two_row = 0  # mat2 row
            matrix_two_column = 0  # mat2 col
            for row in range(self.rows):
                for col in range(other.columns):
                    for _ in range(self.columns):
                        new_matrix[row, col] += round(self.matrix[matrix_one_row, matrix_one_column]
                                                      * other.matrix[matrix_two_row, matrix_two_column], 2,)
                        matrix_one_column += 1
                        matrix_two_row += 1
                    matrix_two_column += 1
                    matrix_one_column = 0
                    matrix_two_row = 0
                matrix_one_row += 1
                matrix_two_column = 0
            return new_matrix
        else:
            return "The number of columns in the first matrix\
            should match the rows in the second"


m1 = Matrix(2, 2)
m2 = Matrix(2, 2)
print("Matrix 1")
m1.print_matrix()
print("Matrix 2")
m2.print_matrix()
print("M1 * M2\n", m1 * m2)
print("M2 * M1\n", m2 * m1)
