"""
Unittests for the rational class.
"""

import unittest
from Rational import Rational


class TestRational(unittest.TestCase):

    def test_str(self):
        self.assertEqual("3/2", Rational(3, 2).__str__())

    def test_simplify_simple(self):
        self.assertEqual("2/3", Rational(4, 6).simplify().__str__())

    def test_simplify_complex(self):
        self.assertEqual("45/32", Rational(270, 192).simplify().__str__())

    def test_eq_literal(self):
        self.assertEqual(Rational(6, 7), Rational(6, 7))

    def test_eq_equivalent(self):
        self.assertEqual(Rational(4, 5), Rational(8, 10))

    def test_not_eq(self):
        self.assertNotEqual(Rational(1, 2), Rational(2, 2))

    def test_not_eq_rat_int(self):
        self.assertFalse(Rational(1, 2) == 1)

    def test_add_rational_1(self):
        self.assertEqual(Rational(4, 5) + Rational(8, 10), Rational(8, 5))

    def test_add_rational_2(self):
        self.assertEqual(Rational(2, 3) + Rational(4, 5), Rational(22, 15))

    def test_add_int_1(self):
        self.assertEqual(Rational(2, 3) + 2, Rational(8, 3))

    def test_add_int_2(self):
        self.assertEqual(Rational(2, 3) + 2, Rational(8, 3))

    def test_radd_int_1(self):
        self.assertEqual(2 + Rational(2, 3), Rational(8, 3))

    def test_sub_1(self):
        self.assertEqual(Rational(3, 2) - Rational(2, 2), Rational(1, 2))

    def test_sub_int_1(self):
        self.assertEqual(Rational(7, 3) - 2, Rational(1, 3))

    def test_rsub_1(self):
        self.assertEqual(1 - Rational(4, 3), Rational(-1, 3))

    def test_mul(self):
        self.assertEqual(Rational(2, 3) * Rational(3, 4), Rational(1, 2))

    def test_rmul(self):
        self.assertEqual((3 * Rational(1, 3)), 1)

    def test_rtruediv(self):
        self.assertEqual(2 / Rational(1, 3), Rational(6, 1))


if __name__ == "__main__":
    unittest.main()
