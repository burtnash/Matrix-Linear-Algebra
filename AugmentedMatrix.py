"""Class for augmented matrix"""

from Matrix import Matrix
from typing import List, Union
from InvalidMatrixException import InvalidMatrixException


class AugmentedMatrix(Matrix):
    """
    m: number of rows
    n: number of columns including solutions column
    board: mxn board containing the entry values.
    """

    def __init__(self, m: int, n: int):
        """
        Initializes a matrix of size m x n filled with 0's.
        :param m: Number of rows
        :param n: Number of columns. Must be at least 2.
        """
        if n < 2:
            raise InvalidMatrixException("Not a valid augmented matrix")
        super().__init__(m, n)

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
                if j == self.n - 2:
                    string += "|"
            string = string[:len(string) - 1]
            string += "|\n"
        string = string[:len(string) - 1]
        return string

    @staticmethod
    def is_invalid_row(row: List[Union[int, float]]) -> bool:
        """
        Returns true if row is an invalid row in a row reduced augmented matrix.
        :param row: A row of an augmented matrix.
        :return: Whether row is valid.
        """
        for i in range(len(row)-1):
            if row[i] != 0:
                return False
        # row[0:-1] are all zeroes
        return row[-1] != 0

    def exists_valid_solution(self) -> bool:
        """
        Returns true if self is a valid augmented matrix with proper solutions.
        :return: Whether self is valid.
        """
        ag = self.copy()
        ag.row_reduce()
        for row in ag.board:
            if AugmentedMatrix.is_invalid_row(row):
                return False
        return True

    def is_valid_solution(self, solutions: List[Union[int, float]]) -> bool:
        """
        Returns true if solutions are valid solutions to augmented matrix self.
        Precondition: len(solutions) == self.n-1
        :param solutions: The solutions in proper order.
        :return: Whether solutions are valid solutions.
        """
        if len(solutions) != self.n-1:
            raise InvalidMatrixException("There are not the right number of solutions for this matrix")
        for row in self.board:
            val = 0
            for i in range(self.n-1):
                val += row[i] * solutions[i]
            if val != row[-1]:
                return False
        return True

    # TODO: fix this, it is wrong
    def has_unique_solution(self) -> bool:
        """
        Returns true if self has a unique solution.
        :return: Whether self has a unique solution.
        """
        if not self.exists_valid_solution():
            return False
        return self.rank() == self.m == self.n
