"""
Unittests for the matrix class.
"""

import unittest
from AugmentedMatrix import AugmentedMatrix


class TestAugmentedMatrix(unittest.TestCase):

    # Exists valid solution test
    def test_is_invalid_row(self):
        r = [0, 0, 0, 1]
        self.assertTrue(AugmentedMatrix.is_invalid_row(r))

    def test_exists_valid_solution_true(self):
        m = AugmentedMatrix(2, 3)
        m.set_entries([1, 1, 2, 2, -1, 1])
        self.assertTrue(m.exists_valid_solution())

    def test_exists_valid_solution_false(self):
        m = AugmentedMatrix(2, 3)
        m.set_entries([1, 1, 1, 1, 1, 2])
        self.assertFalse(m.exists_valid_solution())

    # Is valid solution tests
    def test_is_valid_solution_a(self):
        m = AugmentedMatrix(2, 3)
        m.set_entries([1, 1, 2, 2, -1, 1])
        self.assertTrue(m.is_valid_solution([1, 1]))

    def test_is_valid_solution_b(self):
        m = AugmentedMatrix(3, 3)
        m.set_entries([1, -1, 2, 3, 4, -8, 0, 2, -4])
        self.assertTrue(m.is_valid_solution([0, -2]))

    def test_is_valid_solution_c(self):
        m = AugmentedMatrix(2, 4)
        m.set_entries([1, 0, 1, 2, 1, 0, -1, 0])
        self.assertTrue(m.is_valid_solution([1, 0, 1]))

    def test_is_valid_solution_d(self):
        m = AugmentedMatrix(2, 5)
        m.set_entries([1, 1, 0, 0, 3, 1, 0, 2, -1, 2])
        self.assertFalse(m.is_valid_solution([1, 2, 3, 4]))

    # Exists unique solutions test
    def test_unique_solution(self):
        m = AugmentedMatrix(2, 3)
        m.set_entries([1, 0, 1, 0, 1, 1])
        self.assertTrue(m.has_unique_solution())

    def test_unique_solution_2(self):
        m = AugmentedMatrix(2, 4)
        m.set_entries([1, 0, 1, 2, 0, 1, 1, 1])
        b = m.has_unique_solution()
        self.assertFalse(m.has_unique_solution())


if __name__ == "__main__":
    unittest.main()
