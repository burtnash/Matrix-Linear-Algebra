"""
Unittests for the rational class.
"""

import unittest
from Rational import Rational


class TestRational(unittest.TestCase):

    def test_str(self):
        r = Rational(3, 2)
        self.assertEqual("3/2", r.__str__())

    def test_simplify_simple(self):
        r = Rational(4, 6).simplify()
        self.assertEqual("2/3", r.__str__())

    def test_simplify_complex(self):
        r = Rational(270, 192).simplify()
        self.assertEqual("45/32", r.__str__())

    def test_eq(self):
        r1 = Rational(4, 5)
        r2 = Rational(8, 10)
        self.assertEqual(r1, r2)

    def test_add_eq(self):
        r1 = Rational(4, 5)
        r2 = Rational(8, 10)
        r3 = Rational(8, 5)
        self.assertEqual(r1 + r2, r3)


if __name__ == "__main__":
    unittest.main()
