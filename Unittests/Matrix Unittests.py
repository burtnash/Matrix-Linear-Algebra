"""
Unittests for the matrix class.
"""

import unittest
from Matrix import Matrix


class TestMatrix(unittest.TestCase):

    def test_is_ref(self):
        m = Matrix(3, 3)
        m.set_board([[1, 2, 3], [0, 1, 2], [0, 0, 1]])
        self.assertTrue(m.in_row_echelon_form())

    def test_is_ref_1(self):
        m = Matrix(3, 3)
        m.set_board([[2, 2, 3], [0, 1, 2], [0, 0, 1]])
        self.assertFalse(m.in_row_echelon_form())

    def test_is_ref_2(self):
        m = Matrix(3, 3)
        m.set_board([[1, 2, 3], [2, 1, 2], [0, 0, 1]])
        self.assertFalse(m.in_row_echelon_form())

    def test_is_ref_4(self):
        m = Matrix(3, 3)
        m.set_board([[1, 2, 3], [0, 0, 0], [0, 0, 1]])
        self.assertFalse(m.in_row_echelon_form())

    def test_is_ref_3(self):
        m = Matrix(3, 3)
        m.set_board([[0, 1, 3], [1, 0, 2], [0, 0, 1]])
        self.assertFalse(m.in_row_echelon_form())

    def test_is_ref_true_zero_row(self):
        m = Matrix(3, 3)
        m.set_board([[1, 1, 3], [0, 0, 1], [0, 0, 0]])
        self.assertTrue(m.in_row_echelon_form())

    def test_is_ref_true_m_not_n(self):
        m = Matrix(3, 4)
        m.set_board([[1, 1, 3], [0, 1, 1], [0, 0, 1], [0, 0, 0]])
        self.assertTrue(m.in_row_echelon_form())

    def test_is_ref_zero_matrix(self):
        m = Matrix(3, 3)
        m.set_board([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertTrue(m.in_row_echelon_form())

    # Row reduce tests
    def test_row_reduce_simple_matrix_23(self):
        m = Matrix(2, 3)
        m.set_board([[0, 1, 2], [1, 2, 3]])
        m.row_reduce()
        self.assertTrue(m.in_row_echelon_form())

    def test_row_reduce_simple_matrix_33(self):
        m = Matrix(3, 3)
        m.set_board([[0, 1, 2], [1, 2, 3], [2, 3, 4]])
        m.row_reduce()
        print(m)
        self.assertTrue(m.in_row_echelon_form())




if __name__ == "__main__":
    unittest.main()
