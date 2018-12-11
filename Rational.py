"""A Rational number"""

from typing import Union


class Rational:
    """
    A number that can be represented as a fraction of two integers.

    p: The numberator
    q: The denominator
    """

    def __init__(self, num: int, denom: int=1) -> None:
        """
        Initializes a new rational number
        Precondition: num and denom must be ints, denom can't be zero
        :param num: The numberator
        :param denom: The denominator, defaults to one.
        """
        if denom == 0:
            raise ZeroDivisionError("Cannot have rational with zero denominator.")
        self.p = num
        self.q = denom

    def __str__(self) -> str:
        """
        Gives self as a string
        :return: A string representation of self.
        """
        return "{}/{}".format(self.p, self.q)

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """
        Returns the greatest common denominator of a and b.
        :param a: The first integer
        :param b: The second integer
        :return: a and b's greatest common denominator
        """
        if a == 0:
            return b
        elif b == 0:
            return a
        return Rational.gcd(b, a % b)

    def simplify(self) -> "Rational":
        """
        Returns a new rational equivalent to self but with the lowest possible denominator
        :return: A rational equal to self but reduced
        """
        gcd = Rational.gcd(self.p, self.q)
        temp_rational = Rational(self.p//gcd, self.q//gcd)
        return temp_rational

    def __eq__(self, other) -> bool:
        """
        Returns whether self and other are equal
        :param other: The other object being compared.
        :return: Whether self and other are equal.
        """
        if type(self) != type(other):
            return False
        return self.simplify().p == other.simplify().p and self.simplify().q == other.simplify().q

    def get_numerator(self) -> int:
        """
        :return: The numerator of self.
        """
        return self.p

    def get_denominator(self) -> int:
        """
        :return: The denominator of self.
        """
        return self.q

    def scale(self, scalar: int) -> "Rational":
        """
        Returns scaled self but does not change underlying value. Ie, self = self.scale(m) for all m.
        :return: Scaled version of self.
        """
        return Rational(self.p * scalar, self.q * scalar)

    def __add__(self, other: "Rational"):
        """
        :return: The sum of self and other simplified.
        """
        denom_self = self.get_denominator()
        denom_other = other.get_denominator()
        a = self.scale(denom_other)
        b = other.scale(denom_self)
        r = Rational(a.p + b.p, a.q)
        return r.simplify()

    def __mul__(self, other: "Rational") -> "Rational":
        """
        Returns self times other in simplest terms.
        :param other: The number being multiplied to self
        :return: The rational equal to self multiplied by other
        """
        return Rational(self.p * other.p, self.q * other.q).simplify()

    def __rmul__(self, other: "Rational") -> "Rational":
        """
        Returns self times other in simplest terms.
        :param other: The number being multiplied to self
        :return: The rational equal to self multiplied by other
        """
        return self.__mul__(other)

    def to_float(self) -> float:
        """
        :return: A floating point equivalent to self
        """
        return self.p / self.q
