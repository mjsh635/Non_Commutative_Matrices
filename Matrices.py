
import random
import numpy as np

class Matrix:
    """create a matrix of size row/columns
        create and return all the random values for the matrix
        populate that matrix with random values
        return the matrix
    """
    def _create_matrix(self, rows:int, columns:int):
        pass
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


m1 = Matrix()