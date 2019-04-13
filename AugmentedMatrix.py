"""Class for augmented matrix"""

from Matrix import Matrix
from typing import List, Union
from InvalidMatrixException import InvalidMatrixException
from Rational import Rational


class AugmentedMatrix(Matrix):
    """
    m: number of rows
    n: number of columns including solutions column
    board: mxn board containing the entry values.
    """

    def __init__(self, m: int, n: int, board: Union[List[Union[int, Rational]], None] = None):
        """
        Initializes a matrix of size m x n filled with 0's.
        :param m: Number of rows
        :param n: Number of columns. Must be at least 2.
        """
        if n < 2:
            raise InvalidMatrixException("Not a valid augmented matrix")
        super().__init__(m, n, board)

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

    def set_coefficients(self, coefficients: List[List[Union[int, Rational]]]) -> None:
        """
        Sets the coefficients of the augmemted matrix.
        Precondition: len(coefficients) = num rows
        Precondition: len(coefficients[i]) = num cols - 1
        :param coefficients: The coefficients, as a list of the rows.
        """
        for i in range(len(coefficients)):
            for j in range(len(coefficients[i])):
                self.set_entry(i, j, coefficients[i][j])

    def set_constants(self, solutions: List[Union[int, Rational]]) -> None:
        """
        Sets the constants of the augmemted matrix.
        Precondition: len(solutions) = num rows
        :param solutions: The solutions from top to bottom
        """
        for i in range(len(solutions)):
            self.set_entry(i, self.n-1, solutions[i])

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

    def has_unique_solution(self) -> bool:
        """
        Returns true if self has a unique solution.
        :return: Whether self has a unique solution.
        """
        if not self.exists_valid_solution():
            return False
        return self.rank() == self.n - 1

    def get_unique_solutions(self):
        """
        Returns a list of the solutions of self.
        :return:
        """
        if not self.has_unique_solution():
            raise InvalidMatrixException("This matrix has more than one unique solution")
        rows = []
        for i in range(self.m):
            rows.append(self.board[i])
        solutions = [0 for _ in range(self.n-1)]
        rows.reverse()
        for row in rows:
            constants = row[-1]
            coefficients = row[:-1]
            print(coefficients)
            print(solutions)



if __name__ == '__main__':
    ag = AugmentedMatrix(2, 3, [1, 1, 2, 0, 1, 1])
    ag.get_unique_solutions()
