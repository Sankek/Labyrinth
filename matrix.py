"""
This module contains main matrix classes and operations with them. Addition, subtraction, multiplication,
exponentiation and equality operators are defined for appropriate matices.

A mathematical matrix in this module is a list [row_1, row_2, ...], where row_i = [element_in_column_1_of_row_i, ...]

Reference to a matrix element in row 'm' and in column 'n' uses the standard notation A[m][n].
A[m] refers to the whole row m.
Note that a nubmer of row or a column starts from the zero.

There are some exmaples in the end of the module.
"""


class Matrix:
    def __init__(self, rows=0, columns=0, _list=None):
        self.size = str(rows)+'x'+str(columns)
        self.rows = rows
        self.cols = columns
        if _list is not None:
            self._list = _list
        else:
            self._list = []
            for r in range(rows):
                col = []
                for c in range(columns):
                    col.append(0)
                self._list.append(col)
            
    def __getitem__(self, row):
        return self._list[row]

    def __setitem__(self, row, new_row):
        self._list[row] = new_row

    def print(self):
        for i in self:
            print(i)

    def set(self, new_list_or_const):
        try:
            for r in range(self.rows):
                for c in range(self.cols):
                    self[r][c] = new_list_or_const[r][c]
        except TypeError:
            for r in range(self.rows):
                for c in range(self.cols):
                    self[r][c] = new_list_or_const

    def set_row(self, row, new_list_or_const):
        try:
            self[row] = list(new_list_or_const)
        except TypeError:
            for c in range(self.cols):
                self[row][c] = new_list_or_const

    def set_col(self, col, new_list_or_const):
        try:
            for r in range(self.rows):
                self[r][col] = new_list_or_const[r]
        except TypeError:
            for r in range(self.rows):
                self[r][col] = new_list_or_const

    def __eq__(self, other):
        for r in range(self.rows):
            for c in range(self.cols):
                if self[r][c] != other[r][c]:
                    return False
        return True

    def __add__(self, other):
        new_matr = Matrix(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                new_matr[r][c] = self[r][c]+other[r][c]
        return new_matr

    def __mul__(self, other_or_const):
        try:
            new_matr = Matrix(self.rows, other_or_const.cols)
            for r in range(self.rows):
                for c in range(other_or_const.cols):
                    for n in range(self.cols):
                        new_matr[r][c] += self[r][n]*other_or_const[n][c]
            return new_matr
        except AttributeError:
            new_matr = Matrix(self.rows, self.cols)
            for r in range(self.rows):
                new_matr[r] = [i*other_or_const for i in self[r]]
            return new_matr

    def __sub__(self, other):
        new_matr = self+other*-1
        return new_matr

    def __pow__(self, power):
        if power == 0:
            new_matr = matr_E(self.rows)
            return new_matr
        new_matr = self
        for i in range(power-1):
            new_matr *= self
        return new_matr

    def transpose(self):
        new_matr = Matrix(self.cols, self.rows)
        for c in range(self.cols):
            for r in range(self.rows):
                new_matr[c][r] = self[r][c]
        return new_matr

    def row(self, row):
        return self[row]

    def col(self, col):
        return self.transpose()[col]


def matr_E(n):
    new_matr = Matrix(n, n)
    for i in range(n):
        new_matr[i][i] = 1
    return new_matr


if __name__ == '__main__':
    print('--- setting a matrix and its size ---')
    A = Matrix(4, 3)
    A.print()
    print('--- setting its values ---')
    A[0][1] = 5
    A.set_row(1, [1, 2, 3])
    A.print()
    print('--- changing rows ---')
    A[0], A[1] = A[1], A[0]
    A.print()
    print('--- changing elements ---')
    A[0][2], A[0][0] = A[0][0], A[0][2]
    A.print()
    print('--- example of matrix operations ---')
    A = Matrix(2, 2, [[1, 2], [2, 3]])
    B = Matrix(2, 2, [[-1, -2], [2, 1]])
    print('A =')
    A.print()
    print('B =')
    B.print()
    print('\nA+B =')
    (A+B).print()
    print('\n3A*2B =')
    ((A*3)*(B*2)).print()  # note that to multiply matrix by a constant you have to write A*c not c*A
