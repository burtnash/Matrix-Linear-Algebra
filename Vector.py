"""A vector by the linear algebra definition"""

from typing import Union, List
from Matrix import Matrix


class Vector(Matrix):
    """
    A vector ala linear algebra

    m: The number of rows
    n: The number of columns (always 1)
    board: The values of vector
    """

    def __init__(self, size: int) -> None:
        """
        Initializes a new vector
        :param size: The size of the vector
        """
        self.m = size
        self.n = 1
        self.board = []
        for i in range(size):
            self.board.append([])
            self.board[i].append(0)

    def __eq__(self, other) -> bool:
        """
        Returns true if self is equal to other
        :param other: The other vector
        :return: Whether or not self equals other
        """
        if type(self) != type(other):
            return False
        if self.size != other.size:
            return False
        for i in range(self.size):
            if self.get_entry(i) != other.get_entry(i):
                return False
        return True

    def __str__(self) -> str:
        """
        Returns string representation of self
        :return: String representation of self
        """
        return str(self.board)

    def get_entry(self, i: int) -> Union[int, float]:
        """
        Returns the entry of self at i
        :param i: The index of the value
        :return: The value at i
        """
        return self.board[i][0]

    def set_entry(self, i: int, value: Union[int, float]) -> None:
        """
        Sets the entry at index i to value
        :param i: The index of the value being set
        :param value: The new value
        """
        self.board[i][0] = value

    def set_vector(self, vector: List[Union[int, float]]) -> None:
        """
        Sets all values of self to those of list, in matching order.
        Precondition: len(vector) = self.size
        :param vector: The list of new values
        """
        self.board = vector.copy()

    def copy(self) -> "Vector":
        """
        Returns a copy of self
        :return: A shallow copy of self
        """
        temp_vector = Vector(self.size)
        for i in range(self.size):
            temp_vector.set_entry(i, self.get_entry(i))
        return temp_vector

    def is_zero_vector(self) -> bool:
        """
        Returns true if self is vector of all zeroes
        :return: Whether self is a zero vector
        """
        for i in range(self.size):
            if self.get_entry(i) != 0:
                return False
        return True


if __name__ == "__main__":
    pass
