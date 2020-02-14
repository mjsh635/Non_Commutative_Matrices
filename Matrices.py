# required for the operation of this class
import random
import numpy as np
# used in the printing
import time
import os


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
            m1_row = 0  # mat row
            m1_column = 0  # mat col
            m2_row = 0  # mat2 row
            m2_column = 0  # mat2 col
            for row in range(self.rows):
                for col in range(other.columns):
                    for _ in range(self.columns):
                        new_matrix[row, col] += round(self.matrix[m1_row, m1_column]
                                                      * other.matrix[m2_row, m2_column], 2,)
                        m1_column += 1
                        m2_row += 1
                    m2_column += 1
                    m1_column = 0
                    m2_row = 0
                m1_row += 1
                m2_column = 0
            return new_matrix
        else:
            return "The number of columns in the first matrix\
            should match the rows in the second"


# Clear the terminal before printing
os.system('cls||clear')


print("#################################################################")
print("#################################################################")

print("""\nWhen multiplying matrices, they are not commutative,
this means that when you multiply two matrices together A, B in
the order A * B you receive a matrix C. However when you multiply
these same matrices in the order B * A, you dont receive C.

The orders that the matrices are multiplied in matter! \n
""",)

time.sleep(5)

print(""" Here is an example. Using 2 randomly populated matrices:
""")

print("Matrix 1")
m1 = Matrix(3, 3)
m1.print_matrix()

print("Matrix 2")
m2 = Matrix(3, 3)
m2.print_matrix()

time.sleep(5)

print("""\n When multiplied in the order Matrix 1 * Matrix 2
they produce a matrix with the values:""")

print(m1*m2)

time.sleep(5)

print("""\n However when multiplied in the order Matrix 2 * Matrix 1
they produce a totally different matrix with the values:""")

print(m2*m1)

time.sleep(5)

print("""\n In this case 2 square matrices were used, if the same test
is done with matrices of different sizes such as these:""")

print("Matrix 3")
m3 = Matrix(3, 1)
m1.print_matrix()

print("Matrix 4")
m4 = Matrix(1, 4)
m4.print_matrix()

time.sleep(5)

print("""\n When multiplied in the order Matrix 3 * Matrix 4
they produce a matrix with the values:""")

print(m3*m4)

time.sleep(5)

print("""\n However When multiplied in the order Matrix 4 * Matrix 3
they cannot be multiplied as they don't meet the rules for matrix
multiplication:\n""")

print(m4*m3)

print("\n#################################################################")
print("#################################################################")
