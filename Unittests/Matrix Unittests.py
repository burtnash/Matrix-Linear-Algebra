"""
Unittests for the matrix class.
"""

import unittest
from Matrix import Matrix


class TestMatrix(unittest.TestCase):

    # In Row Echelon Form tests
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

    # In Reduced REF tests
    def test_is_rref(self):
        m = Matrix(3, 3)
        m.set_board([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertTrue(m.in_reduced_ref())

    def test_is_rref_2(self):
        m = Matrix(3, 3)
        m.set_board([[1, 0, 1], [0, 1, 1], [0, 0, 0]])
        self.assertTrue(m.in_reduced_ref())

    def test_is_ref_not_rref(self):
        m = Matrix(3, 3)
        m.set_board([[1, 1, 1], [0, 1, 1], [0, 0, 1]])
        self.assertFalse(m.in_reduced_ref())

    def test_is_rref_3(self):
        m = Matrix(4, 4)
        m.set_board([[1, 2, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]])
        self.assertTrue(m.in_reduced_ref())

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
        self.assertTrue(m.in_row_echelon_form())

    def test_reduce_ref(self):
        m = Matrix(3, 3)
        m.set_board([[0, 1, 2], [1, 2, 3], [2, 3, 4]])
        m.row_reduce()
        m.reduced_row_reduce()
        self.assertTrue(m.in_reduced_ref())

    def test_reduce_ref_2(self):
        m = Matrix(3, 4)
        m.set_board([[0, 1, 2, 3], [1, 2, 3, 5], [2, 3, 4, 7]])
        m.row_reduce()
        m.reduced_row_reduce()
        self.assertTrue(m.in_reduced_ref())

    def test_reduce_ref_3(self):
        m = Matrix(4, 6)
        m.set_board([[1, 2, 3, 4, 5, 6], [0, 0, 1, 0, 2, 8], [0, 0, 0, 1, 2, 5], [0, 0, 0, 0, 0, 0]])
        m.row_reduce()
        m.reduced_row_reduce()
        self.assertTrue(m.in_reduced_ref())


if __name__ == "__main__":
    unittest.main()
