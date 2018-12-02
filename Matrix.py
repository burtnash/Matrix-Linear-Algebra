"""Linear Algebra Matrix"""

from typing import Union, List, Tuple


class Matrix:
    """
    A Matrix ala Liner Algebra.

    m: Number of rows.
    n: Number of columns.
    board: All matrix values.
    """

    def __init__(self, m: int, n: int) -> None:
        self.m = m
        self.n = n
        self.board = []
        for i in range(m):
            self.board.append([])
            for _ in range(n):
                self.board[i].append(0)

    def __str__(self) -> str:
        """
        Returns a string representation of self.
        :return: String representation of self.
        """

        string = ""
        for i in range(self.m):
            string += "|"
            for j in range(self.n):
                string += str(self.board[i][j]) + " "
            string = string[:len(string) - 1]
            string += "| \n"
        return string

    def __eq__(self, other: object) -> bool:
        """
        Returns whether or not self and other are equal.
        :param other: The object being compared to self.
        :return: Whether or not self and other are equal.
        """
        if type(self) != type(other):
            return False
        other: Matrix
        if self.m != other.m or self.n != other.n:
            return False
        for i in range(self.m):
            for j in range(self.n):
                if self.get_entry(i, j) != other.get_entry(i, j):
                    return False
        return True

    def set_entry(self, row: int, col: int, value: int) -> None:
        """
        Sets the entry and row row and column col to value.
        :param row: The row of the value being set.
        :param col: The column of the value being set.
        :param value: The new value.
        """
        self.board[row][col] = value

    def get_entry(self, row: int, col: int) -> Union[int, float]:
        """
        Returns the value at row i and col j.
        :param row: The row of the value being retrieved.
        :param col: The column of the value being retrieved.
        """
        return self.board[row][col]

    def set_board(self, board: List[List[Union[int, float]]]) -> None:
        """
        Sets the board to board, where the lists of board are the rows of the matrix.
        :param board: A list of list of values to be the new board.
        """
        self.board = board

    def copy(self) -> "Matrix":
        """
        Returns a shallow copy of self.
        :return: A copy of self.
        """
        temp_matrix = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                temp_matrix.set_entry(i, j, self.get_entry(i, j))
        return temp_matrix

    def round(self, digits: int) -> "Matrix":
        """
        Returns self with all entries rounded to digits decimal places.
        :param digits: The number of decimal places rounded to.
        :return: Matrix equivalent to self with each entry rounded.
        """
        temp_matrix = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                temp_matrix.set_entry(i, j, round(self.get_entry(i, j), digits))
        return temp_matrix

    @staticmethod
    def is_zero_row(row: List[Union[int, float]]) -> bool:
        """
        Returns true if row contains only 0's.
        :return: Whether or not row is a zero row.
        """
        for item in row:
            if item != 0:
                return False
        return True

    @staticmethod
    def get_i_matrix(size: int) -> "Matrix":
        """
        Returns the matrix I that is size: size x size.
        :param size: The size of the I matrix being returned.
        :return: The I matrix that is size x size.
        """
        i_matrix = Matrix(size, size)
        for i in range(size):
            for j in range(size):
                if i == j:
                    i_matrix.set_entry(i, j, 1)
        return i_matrix

    def is_square(self) -> bool:
        """
        Returns true iff self is a square matrix.
        :return: Whether or not self is square.
        """
        return self.m == self.n

    def is_vector(self) -> bool:
        """
        Returns true if self is a vector.
        :return: Whether or not self is a vector
        """
        return self.n == 1

    def is_zero_matrix(self) -> bool:
        """
        Returns true iff self is the zero matrix.
        :return: Whether or not self is a vector.
        """
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] != 0:
                    return False
        return True

    def is_invertible(self) -> bool:
        """
        Returns true iff sef is invertible.
        :return: Whether or not self is invertible.
        """
        if not self.is_square():
            return False
        return self.determinant() != 0

    def is_diagonal(self) -> bool:
        """
        Returns true if self is a diagonal matrix
        :return: Whether self is diagonal
        """
        for i in range(self.m):
            for j in range(self.n):
                if i != j and self.get_entry(i, j) != 0:
                    return False
        return True

    def is_equal_size(self, other: "Matrix") -> bool:
        """
        Returns true if self and other have equal size
        :param other: The matrix being compared to self
        :return: Whether or not self and other have equal size
        """
        return self.m == other.m and self.n == other.n

    def scale(self, scalar: float) -> None:
        """
        Scales self by scalar.
        :param scalar: The amount that self is being scaled by.
        """
        for i in range(self.m):
            for j in range(self.n):
                self.board[i][j] *= scalar

    def add_matrix(self, other: "Matrix") -> "Matrix":
        """
        Returns matrix equivalent to self + other
        :param other: The second matrix being added.
        :return: A new matrix equal to the sum of self and other.
        """
        if not self.is_equal_size(other):
            raise Exception
        a = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                a.set_entry(i, j, self.get_entry(i, j) + other.get_entry(i, j))
        return a

    def swap_rows(self, row_1: int, row_2: int) -> None:
        """
        Swaps row_1 and row_2.
        :param row_1: The first row being swaped.
        :param row_2: The second row being swaped.
        """
        self.board[row_1], self.board[row_2] = self.board[row_2], self.board[row_1]

    def scale_row(self, row: int, scalar: float) -> None:
        """
        Scales row by scalar.
        :param row: The row being scaled.
        :param scalar: The amount it is being scaled by.
        """
        for i in range(self.n):
            self.board[row][i] *= scalar

    def add_scaled_row(self, base_row: int, adder_row: int, scalar: float) -> None:
        """
        Adds row2's values to row1 where each value is scaled by scalar.
        :param base_row: The row being added onto.
        :param adder_row: The row being scaled and added to base_row.
        :param scalar: The amount that adder_row is scaled by.
        """
        temp_row = []
        for num in self.board[adder_row]:
            temp_row.append(num * scalar)
        for i in range(len(self.board[base_row])):
            self.board[base_row][i] += temp_row[i]

    def get_leading_ones(self) -> List[Tuple[int, int]]:
        """
        Returns a list of the coordinated of all the leading ones.
        Precondition: self is in ref.
        :return: List of leading one coordinates in the form (row, col).
        """
        leading_ones = []
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    leading_ones.append((i, j))
                    break
        return leading_ones

    def in_row_echelon_form(self) -> bool:
        """
        Returns true iff self is in row echelon form.
        :return: Whether or not self is in REF.
        """
        leading_ones = []
        # Test 1: Are all first entries leading ones.
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    leading_ones.append((i, j))
                    break
                elif self.board[i][j] != 0:
                    return False

        # Test 2: Are all entries below leading 1's zeroes.
        for leader in leading_ones:
            row = leader[0]
            col = leader[1]
            for i in range(row + 1, self.m):
                if self.board[i][col] != 0:
                    return False

        # Test 3: All leading ones in rows lower down are to the right.
        for i in range(1, len(leading_ones)):
            if leading_ones[i][1] <= leading_ones[i - 1][1]:
                return False

        # Test 4: All zero rows are at the bottom.
        zero_row_found = False
        for item in self.board:
            if Matrix.is_zero_row(item):
                zero_row_found = True
            elif zero_row_found:
                if not Matrix.is_zero_row(item):
                    return False
        return True

    def in_reduced_ref(self) -> bool:
        """
        Return true if self is in reduced row echelon form.
        :return: Whether or not self is in reduced REF.
        """
        if not self.in_row_echelon_form():
            return False
        leading_ones = self.get_leading_ones()
        for leader in leading_ones:
            for i in range(leader[0]):
                if self.get_entry(i, leader[1]) != 0:
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
                self.scale_row(current_row, 1/self.get_entry(current_row, current_col))
                for i in range(current_row + 1, self.m):
                    entry = self.get_entry(i, current_col)
                    if entry != 0:
                        self.add_scaled_row(i, current_row, -entry)
                current_row += 1
                current_col += 1

    def reduced_row_reduce(self) -> None:
        """
        Row reduces self to RREF.
        Precondition: self is in ref.
        """
        leading_ones = self.get_leading_ones()
        leading_ones.reverse()
        for leader in leading_ones:
            for i in range(leader[0] - 1, -1, -1):
                entry = self.get_entry(i, leader[1])
                if entry != 0:
                    self.add_scaled_row(i, leader[0], -entry)

    def transpose(self) -> "Matrix":
        """
        Returns the transpose of self.
        :return: The transpose of self.
        """
        temp_matrix = Matrix(self.n, self.m)
        for i in range(self.m):
            for j in range(self.n):
                temp_matrix.set_entry(j, i, self.get_entry(i, j))
        return temp_matrix

    def multiply(self, other: "Matrix") -> "Matrix":
        """
        Returns the product of self and other together.
        :param other: The right matrix being multiplied.
        :return: The matrix equal to the product of self and other.
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

    def power(self, exponent: int) -> "Matrix":
        """
        Returns matrix equivalent to self multiplied by itself exponent times.
        :param exponent: The exponent that self is raised to.
        :return: The matrix equal to self multiplied by itself exponent-1 times.
        """
        if exponent < 0:
            raise Exception("Invalid exponent")
        elif exponent == 1:
            return self.copy()
        elif not self.is_square():
            raise Exception("Cannot be raised to power")
        elif exponent == 0:
            return Matrix.get_i_matrix(self.m)
        temp_matrix = self.copy()
        temp_matrix2 = self.copy()
        for _ in range(exponent - 1):
            temp_matrix2 = temp_matrix.multiply(temp_matrix2)
        return temp_matrix2

    def matrix_sub_two(self, row: int, col: int) -> "Matrix":
        """
        Returns the matrix minus row row and column column.
        :param row: Row to be removed.
        :param col: Column to be removed.
        :return: The matrix equal to self without row row and column col.
        """
        passed_row = 0
        new_matrix = Matrix(self.m - 1, self.n - 1)
        for i in range(len(self.board)):
            passed_col = 0
            if i == row:
                passed_row = 1
            else:
                for j in range(len(self.board)):
                    if j == col:
                        passed_col = 1
                    else:
                        new_matrix.set_entry(i - passed_row, j - passed_col, self.get_entry(i, j))
        return new_matrix

    def determinant(self) -> float:
        """
        Returns the determinant of self.
        :return: The determinant of self.
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
            return a * d - b * c
        else:
            det = 0
            for j in range(size):
                det += (-1) ** j * self.get_entry(0, j) * self.matrix_sub_two(0, j).determinant()
            return det

    def inverse_size_2(self) -> "Matrix":
        """
        Returns a matrix equal to the inverse of self if self is 2x2 and invertible.
        Precondition: Self is 2x2 and invertible.
        :return: A 2x2 matrix equal to the inverse of self.
        """
        if self.n != 2 or self.m != 2:
            raise Exception("Not 2x2")
        elif not self.is_invertible():
            raise Exception("Not invertible")
        temp_matrix = self.copy()
        temp_matrix.set_entry(0, 0, self.get_entry(1, 1))
        temp_matrix.board[0][1] *= -1
        temp_matrix.board[1][0] *= -1
        temp_matrix.set_entry(1, 1, self.get_entry(0, 0))
        scalar = 1 / temp_matrix.determinant()
        temp_matrix.scale(scalar)
        return temp_matrix

    def inverse(self) -> "Matrix":
        """
        Returns the inverse of self.
        Precondition: Self is invertible.
        :return: The matrix equal to the inverse of self.
        """
        if not self.is_invertible():
            raise Exception
        size = self.m
        temp_matrix = Matrix(size, 2 * size)
        i_matrix = Matrix.get_i_matrix(size)
        for i in range(self.m):
            for j in range(self.n):
                temp_matrix.set_entry(i, j, self.get_entry(i, j))
        for i in range(self.m):
            for j in range(self.n):
                temp_matrix.set_entry(i, j + size, i_matrix.get_entry(i, j))
        temp_matrix.row_reduce()
        temp_matrix.reduced_row_reduce()
        temp_matrix_2 = Matrix(size, size)
        for i in range(self.m):
            for j in range(self.n):
                temp_matrix_2.set_entry(i, j, temp_matrix.get_entry(i, j - size))
        temp_matrix_3 = temp_matrix_2.round(3)
        return temp_matrix_3

    def is_eigenvalue(self, eigenvalue: int) -> bool:
        """
        Returns true if eigenvalue is an eigenvalue for self.
        :param eigenvalue: Value being checked.
        :return: Whether or not eigenvalue is an eigenvalue for self.
        """
        if not self.is_square():
            raise Exception
        i = Matrix.get_i_matrix(self.m)
        i.scale(eigenvalue * -1)
        a = self.add_matrix(i)
        return a.determinant() == 0


if __name__ == '__main__':
    pass
