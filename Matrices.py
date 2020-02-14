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
        self.matrix = self._populate_matrix(
            self.matrix, self._random_matrix_values())

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
            data.append(round(random.random(), 2)+random.randint(0, 5))
        return data

    def _populate_matrix(self, matrix, data):
        """ Populate the matrix with the data
        """
        i = 0
        for row in range(self.rows):
            for col in range(self.columns):
                matrix[row, col] = data[i]
                i += 1
        return matrix

    def get_matrix(self):
        """ Return the matrix filled out
        """
        return self.matrix

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
            m = 0  # mat row
            n = 0  # mat col
            p = 0  # mat2 row
            q = 0  # mat2 col
            for row in range(self.rows):
                for col in range(other.columns):
                    for _ in range(self.columns):
                        new_matrix[row, col] += round(self.matrix[m, n]
                                                      * other.matrix[p, q], 2,)
                        n += 1
                        p += 1
                    q += 1
                    n = 0
                    p = 0
                m += 1
                q = 0
            return new_matrix
        else:
            return "The number of columns in the first matrix\
            should match the rows in the second"


m1 = Matrix(2, 2)
m2 = Matrix(2, 2)
# m1 = m1.get_matrix()
# m2 = m2.get_matrix()
# print("Matrix 1\n", m1)
# print("Matrix 2\n", m2)
print("Matrix 1\n", m1.get_matrix())
print("Matrix 2\n", m2.get_matrix())

print("M1 * M2\n", m1 * m2)
print("M2 * M1\n", m2 * m1)
