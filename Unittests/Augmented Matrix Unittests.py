"""
Unittests for the matrix class.
"""

import unittest
from AugmentedMatrix import AugmentedMatrix


class TestAugmentedMatrix(unittest.TestCase):

    def test_is_valid_solution__true(self):
        m = AugmentedMatrix(2, 3)
        m.set_entries([1, 1, 2, 2, -1, 1])
        self.assertTrue(m.is_valid_solution())


if __name__ == "__main__":
    unittest.main()
