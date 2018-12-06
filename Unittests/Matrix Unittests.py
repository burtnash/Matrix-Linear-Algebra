"""
Unittests for the matrix class.
"""

import unittest
from Matrix import Matrix


class TestMatrix(unittest.TestCase):

    # Various Simple Tests
    def test_string(self):
        m = Matrix(2, 2)
        m.set_board([[1, 2], [3, 4]])
        n = "|1 2|\n|3 4|"
        self.assertEqual(n, m.__str__())

    def test_equals(self):
        m = Matrix(2, 2)
        m.set_board([[1, 2], [3, 4]])
        n = Matrix(2, 2)
        n.set_board([[1, 2], [3, 4]])
        self.assertEqual(m, n)

    def test_copy(self):
        m = Matrix(2, 2)
        m.set_board([[1, 2], [3, 4]])
        n = m.copy()
        self.assertEqual(m, n)
        self.assertFalse(m is n)

    def test_i_matrix_size3(self):
        m = Matrix.get_i_matrix(3)
        n = Matrix(3, 3)
        n.set_entry(0, 0, 1)
        n.set_entry(1, 1, 1)
        n.set_entry(2, 2, 1)
        self.assertEqual(m, n)

    def test_set_entries(self):
        m = Matrix(2, 3)
        m.set_entries([0, 1, 2, 3, 4, 5])
        n = "|0 1 2|\n|3 4 5|"
        self.assertEqual(n, m.__str__())

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

    def test_is_ref_6(self):
        m = Matrix(2, 3)
        m.set_entries([1, 0, 0, 0, 0, 1])
        self.assertTrue(m.in_row_echelon_form())

    def test_isnt_ref_9(self):
        m = Matrix(3, 3)
        m.set_entries([0, 1, 2, 0, 0, 0, 0, 0, 1])
        self.assertFalse(m.in_row_echelon_form())

    def test_isnt_ref_10(self):
        m = Matrix(3, 4)
        m.set_entries([2, 1, 3, 7, 0, 1, 1, 0, -1, 4, 0, 3])
        self.assertFalse(m.in_row_echelon_form())

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

    def test_is_not_rref(self):
        m = Matrix(2, 2)
        m.set_entries([1, 2, 0, 1])
        self.assertFalse(m.in_reduced_ref())

    def test_is_not_rref_3(self):
        m = Matrix(2, 3)
        m.set_entries([0, 1, 0, 1, 0, 1])
        self.assertFalse(m.in_reduced_ref())

    def test_is_not_rref_11(self):
        m = Matrix(4, 4)
        m.set_entries([1, 2, 0, 0, 0, 0, 1, 11, 0, 0, 0, 1, 0, 0, 0, 0])
        self.assertFalse(m.in_reduced_ref())

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
