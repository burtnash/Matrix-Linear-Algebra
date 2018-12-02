"""Linear Algebra Helper"""


class Matrix:
    """
    A Matrix ala Liner Algebra.

    m: Number of rows
    n: Number of columns
    board: All matrix values
    """

    def __init__(self, m: int, n: int) -> None:
        self.m = m
        self.n = n
        self.board = []
        for i in range(m):
            self.board.append([])
            for j in range(n):
                self.board[i].append(0)

    def __str__(self) -> str:
        """
        Returns a string representation of self.
        """

        string = ""
        for i in range(self.m):
            for j in range(self.n):
                string += str(self.board[i][j]) + " "
            string += "\n"
        return string

    def __eq__(self, other):
        """
        Returns whether or not self and other are equal.
        """
        if type(self) != type(other):
            return False
        if self.m != other.m or self.n != other.n:
            return False
        ret = True
        for i in range(self.m):
            for j in range(self.n):
                if self.get_entry(i, j) != other.get_entry(i, j):
                    ret = False
        return ret

    def set_entry(self, row: int, col: int, value: int) -> None:
        """
        Sets the entry and row row and column col to value.
        """
        self.board[row][col] = value

    def get_entry(self, i: int, j: int) -> int:
        """
        Returns the value at row i and col j.
        """

        return self.board[i][j]

    def set_board(self, board) -> None:
        """
        Sets the board.
        """
        self.board = board

    def copy(self):
        """
        Returns a copy of self.
        """
        temp_matrix = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                temp_matrix.set_entry(i, j, self.get_entry(i, j))
        return temp_matrix

    @staticmethod
    def is_zero_row(row):
        """
        Returns two iff row is all zeroes
        """
        for item in row:
            if item != 0:
                return False
        return True

    def is_square(self) -> bool:
        """
        Returns true iff self is a square matrix
        """
        return self.m == self.n

    def is_zero_matrix(self) -> bool:
        """
        Returns true iff self is the zero matrix.
        """
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] != 0:
                    return False
        return True

    def scale(self, scalar: float):
        """
        Scales self by scalar.
        """

        for i in range(self.m):
            for j in range(self.n):
                self.board[i][j] *= scalar

    def add_matrix(self, other: "Matrix"):
        """
        Returns matrix equivalent to self + other
        """
        if self.m != other.m or self.n != other.n:
            raise Exception
        a = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                a.set_entry(i, j, self.get_entry(i, j) + other.get_entry(i, j))
        return a

    def swap_rows(self, row_1: int, row_2: int):
        """
        Swaps row_1 and row_2
        """
        self.board[row_1], self.board[row_2] = self.board[row_2], self.board[row_1]

    def scale_row(self, row: int, scalar: float):
        """
        Scales row by scalar
        """
        for i in range(self.n):
            self.board[row][i] *= scalar

    def add_scaled_row(self, row1: int, row2: int, scalar: float):
        """
        Adds row2's values to row1 where each value is scaled by scalar
        """
        temp_row = []
        for num in self.board[row2]:
            temp_row.append(num * scalar)
        for i in range(len(self.board[row1])):
            self.board[row1][i] += temp_row[i]

    def in_row_echelon_form(self) -> bool:
        """
        Returns true iff self is in row echelon form
        """
        leading_ones = []
        # Test 1: Are all first entries leading ones
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    leading_ones.append((i, j))
                    break
                elif self.board[i][j] != 0:
                    return False

        # Test 2: Are all entries below leading 1's zeroes
        for leader in leading_ones:
            row = leader[0]
            col = leader[1]
            for i in range(row+1, self.m):
                if self.board[i][col] != 0:
                    return False

        # Test 3: All leading ones in rows lower down are to the right
        for i in range(1, len(leading_ones)):
            if leading_ones[i][1] <= leading_ones[i-1][1]:
                return False

        # Test 4: All zero rows are at the bottom
        zero_row_found = False
        for item in self.board:
            if Matrix.is_zero_row(item):
                zero_row_found = True
            if zero_row_found:
                if not Matrix.is_zero_row(item):
                    return False

        return True

    def row_reduce(self) -> None:
        """
        Row reduces self by gaussian elimination.
        """
        current_row = 0
        current_col = 0
        while not self.in_row_echelon_form():
            # Find leading 1
            leading_one_row = -1
            for i in range(current_row, self.m):
                if self.get_entry(i, current_col) != 0:
                    leading_one_row = i
                    break

            # Use leading one, make all lower entries 0
            if leading_one_row == -1:
                current_col += 1
            else:
                self.swap_rows(current_row, leading_one_row)
                for i in range(current_row + 1, self.m):
                    entry = self.get_entry(i, current_col)
                    if entry != 0:
                        self.add_scaled_row(i, current_row, -entry)
                current_row += 1
                current_col += 1



    def multiply(self, other):
        """
        Multiples self and other together.
        """

        if self.n != other.m:
            raise Exception
        m = self.m
        n = other.n
        o = self.n
        temp_matrix = Matrix(m, n)
        for i in range(m):
            for j in range(n):
                num = 0
                for k in range(o):
                    num += self.get_entry(i, k) * other.get_entry(k, j)
                temp_matrix.set_entry(i, j, num)
        return temp_matrix

    def power(self, exponent: int):
        """
        Returns matrix equivalent to self multiplied by itself exponent times
        """
        if exponent < 1:
            raise Exception("Invalid exponent")
        elif exponent == 1:
            return self.copy()
        elif self.m != self.n:
            raise Exception("Cannot be raised to power")
        temp_matrix = self.copy()
        temp_matrix2 = self.copy()
        for _ in range(exponent-1):
            temp_matrix2 = temp_matrix.multiply(temp_matrix2)
        return temp_matrix2

    def determinant(self) -> float:
        """
        Returns the determinant of a 2x2 matrix
        """

        if not self.is_square():
            raise Exception("Matrix is not square")
        size = self.m
        if size == 1:
            raise Exception("Cannot have determinant for 1x1 matrix")
        elif size == 2:
            a = self.get_entry(0, 0)
            b = self.get_entry(0, 1)
            c = self.get_entry(1, 0)
            d = self.get_entry(1, 1)
            return a*d - b*c
        else:
            det = 0
            for j in range(size):
                det += (-1)**j * self.get_entry(0, j) * self.matrix_sub_two(0, j).determinant()
            return det

    def inverse2(self):
        """
        Returns a matrix equal to the inverse of self if self is 2x2 and invertible
        """
        if self.n != 2 or self.m != 2:
            raise Exception("Not 2x2")
        elif self.determinant() == 0:
            raise Exception("Not invertible")
        temp_matrix = self.copy()
        temp_matrix.board[0][0] = self.board[1][1]
        temp_matrix.board[0][1] *= -1
        temp_matrix.board[1][0] *= -1
        temp_matrix.board[1][1] = self.board[0][0]
        scalar = 1 / temp_matrix.determinant()
        temp_matrix.scale(scalar)
        return temp_matrix

    def matrix_sub_two(self, row: int, column: int):
        """
        Returns the matrix minus row row and column column.
        """
        passed_row = 0
        new_matrix = Matrix(self.m-1, self.n-1)
        for i in range(len(self.board)):
            passed_col = 0
            if i == row:
                passed_row = 1
            else:
                for j in range(len(self.board)):
                    if j == column:
                        passed_col = 1
                    else:
                        new_matrix.set_entry(i-passed_row, j-passed_col, self.get_entry(i, j))
        return new_matrix

    @staticmethod
    def get_i_matrix(size: int):
        """
        Returns the matrix I that is size x size.
        """
        i_matrix = Matrix(size, size)
        for i in range(size):
            for j in range(size):
                if i == j:
                    i_matrix.set_entry(i, j, 1)
        return i_matrix

    def invertible(self) -> bool:
        """
        Returns true iff sef is invertible.
        """
        if not self.is_square():
            return False
        return self.determinant() != 0

    def is_eigenvalue(self, eigenvalue: int) -> bool:
        """
        Returns true iff eigenvalue is an eigenvalue for self.
        """
        if not self.is_square():
            raise Exception
        i = Matrix.get_i_matrix(self.m)
        i.scale(eigenvalue * -1)
        a = self.add_matrix(i)
        return a.determinant() == 0


if __name__ == '__main__':
    pass
