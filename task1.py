from typing import List
from copy import copy


class Matrix:

    def __init__(self, matrix: List[list]):
        self.matrix = matrix

    def __str__(self):
        m = ""
        for line in self.matrix:
            m = m + " ".join(list(map(str, line))) + "\n"
        return m

    def __add__(self, other: 'Matrix'):
        result = copy(self.matrix)
        for i in range(len(self.matrix)):
            for n in range(len(self.matrix[i])):
                result[i][n] = self.matrix[i][n] + other.matrix[i][n]
        return Matrix(result)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
print(m1)
print(m2)
print(m1 + m2)
