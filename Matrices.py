
import random
import numpy as np

class Matrix:
    """create a matrix of size row/columns
        create and return all the random values for the matrix
        populate that matrix with random values
        return the matrix
    """
    def __init__(self, rows, columns, seed = 1):
        self.columns = columns
        self.seed = seed
        self.rows = rows
        self.matrix = self._create_empty_matrix(self.rows,self.columns)
        
    
    def _create_empty_matrix(self, rows, columns):
        return np.zeros((rows,columns), dtype=float)

    def _random_matrix_values(self):
        """ return a string of random data to be entered into the maxtrix
        """
        random.seed(self.seed)
        data = []
        for _ in range(self.rows*self.columns):
            data.append(round(random.random(), 2)+random.randint(0,5))
        return data

    def _populate_matrix(self, matrix, data):
        """vPopulate the matrix with the data
        """
        i = 0
        for row in range(self.rows):
            for col in range(self.columns):
                matrix[row,col] = data[i]
                i+=1
        return matrix

    def get_matrix(self):
        """ Return the matrix filled out
        """
        return self._populate_matrix(self.matrix,self._random_matrix_values())

    def __add__(self, other):
        if ((self.rows == other.rows) and (self.columns == other.columns)):
            new_matrix = self._create_empty_matrix(self.rows,self.columns)
            for row in range(self.rows):
                for col in range(self.columns):
                    new_matrix[row,col] = (self.matrix[row,col] + other.matrix[row,col])
            return new_matrix
        else:
            return "Matrices sizes don't match"

        
    def __sub__(self,other):
        if ((self.rows == other.rows) and (self.columns == other.columns)):
            new_matrix = self._create_empty_matrix(self.rows,self.columns)
            for row in range(self.rows):
                for col in range(self.columns):
                    new_matrix[row,col] = (self.matrix[row,col] - other.matrix[row,col])
            return new_matrix
        else:
            return "Matrices sizes don't match"

    def __mul__(self,other):
        """ 23.86  26.77
            6.97   21.63 AB

            need if cases for breaking and setting indexers to 0
        """
        if (self.columns == other.rows):
            new_matrix = self._create_empty_matrix(self.rows,other.columns)
            m = 0 #mat row
            n = 0 #mat col
            p = 0 #mat2 row
            q = 0 #mat2 col
            for row in range(self.rows):
                for col in range(other.columns):
                    for _ in range(self.columns):
                        new_matrix[row,col] += round(self.matrix[m,n] * other.matrix[p,q],2,)
                        n += 1
                        p += 1
                    q += 1
                    n = 0
                    p = 0
                m+=1
                q = 0
            return new_matrix
        else:
            return "The number of columns in the first matrix should match the rows in the second"


m1 = Matrix(2,1)
m2 = Matrix(1,4,2)
print(m1.get_matrix())
print(m2.get_matrix())
print(m1*m2)
print(m2*m1)


