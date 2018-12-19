"""A Rational number"""

from typing import Union


class Rational:
    """
    A number that can be represented as a fraction of two integers.
    This type is immutable.

    p: The numberator
    q: The denominator
    """

    def __init__(self, num: int, denom: int = 1) -> None:
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

    def __eq__(self, other) -> bool:
        """
        :param other: The other object being compared.
        :return: Whether self and other are equal.
        """
        if type(other) == int:
            return self.simplify().get_numerator() == other
        elif type(self) != type(other):
            return False
        return self.simplify().p == other.simplify().p and self.simplify().q == other.simplify().q

    def __ne__(self, other) -> bool:
        """
        :param other: The other object being compared.
        :return: Whether self and other are not equal.
        """
        return not self == other

    def __gt__(self, other: Union[int, "Rational"]) -> bool:
        """
        :param other: The other object being compared
        :return: Whether self is greater than other
        """
        if type(other) == int:
            other = Rational(other)
        r1 = self.scale(other.get_denominator())
        r2 = other.scale(self.get_denominator())
        return r1.get_numerator() > r2.get_denominator()

    def __lt__(self, other: Union[int, "Rational"]) -> bool:
        """
        :param other: The other object being compared
        :return: Whether self is less than other
        """
        if type(other) == int:
            other = Rational(other)
        r1 = self.scale(other.get_denominator())
        r2 = other.scale(self.get_denominator())
        return r1.get_numerator() < r2.get_denominator()

    def __ge__(self, other: Union[int, "Rational"]) -> bool:
        """
        :param other: The other object being compared
        :return: Whether self is greater than or equal to other
        """
        return not self < other

    def __le__(self, other: Union[int, "Rational"]) -> bool:
        """
        :param other: The other object being compared
        :return: Whether self is less than or equal to other
        """
        return not self > other

    def __int__(self):
        if not self.is_integer():
            raise ArithmeticError("Cannot be converted to int")
        return self.simplify().get_numerator()

    def __float__(self) -> float:
        """
        :return: A floating point equivalent to self
        """
        return self.p / self.q

    def __str__(self) -> str:
        """
        Gives self as a string
        :return: A string representation of self.
        """
        return "{}/{}".format(self.p, self.q)

    def __add__(self, other: Union[int, "Rational"]):
        """
        :param other: The int/rational being added
        :return: The sum of self and other simplified.
        """
        if type(other) == int:
            other = Rational(other)
        denom_self = self.get_denominator()
        denom_other = other.get_denominator()
        a = self.scale(denom_other)
        b = other.scale(denom_self)
        r = Rational(a.p + b.p, a.q)
        return r.simplify()

    def __radd__(self, other: int) -> "Rational":
        """
        :param other: The int/rational being added
        :return: The sum of self and other simplified.
        """
        return self + other

    def __sub__(self, other: Union[int, "Rational"]):
        """
        :param other: The int/rational being subtracted
        :return: The difference of self and other
        """
        if type(other) == int:
            sub = Rational(-other)
        else:
            sub = Rational(-other.get_numerator(), other.get_denominator())
        return self + sub

    def __rsub__(self, other: int):
        """
        :param other: The int/rational being subtracted
        :return: The difference of self and other
        """
        other = Rational(other)
        return other - self

    def __mul__(self, other: Union[int, "Rational"]) -> "Rational":
        """
        Returns self times other in simplest terms.
        :param other: The number being multiplied to self
        :return: The rational equal to self multiplied by other
        """
        if type(other) == int:
            other = Rational(other)
        return Rational(self.p * other.p, self.q * other.q).simplify()

    def __rmul__(self, other: int) -> "Rational":
        """
        Returns self times other in simplest terms.
        :param other: The number being multiplied to self
        :return: The rational equal to self multiplied by other
        """
        return self * other

    def __truediv__(self, other: Union[int, "Rational"]) -> "Rational":
        """
        Returns the quotient of self and other in simplest terms
        :param other: The int/rational that is the divisor
        :return: The quotient of self divided by other.
        """
        if type(other) == int:
            other = Rational(other)
        other = other.inverse()
        return self * other

    def __rtruediv__(self, other: int) -> "Rational":
        """
        Returns the quotient of self and other in simplest terms
        :param other: The int/rational that is being divided.
        :return: The quotient of self divided by other.
        """
        other = Rational(other)
        return other / self

    def __floordiv__(self, other: Union[int, "Rational"]) -> int:
        """
        Returns the integer division of self divided by other.
        :param other: The divisor, either int or Rational
        :return: floor of self divided by other
        """
        r = self / other
        return r.get_numerator() // r.get_denominator()

    def __rfloordiv__(self, other: int) -> int:
        """
        Returns the integer division of other divided by self.
        :param other: The int or rational being divided
        :return: floor of other divided by self
        """
        other = Rational(other)
        return other // self

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

    def simplify(self) -> "Rational":
        """
        Returns a new rational equivalent to self but with the lowest possible denominator
        :return: A rational equal to self but reduced
        """
        gcd = Rational.gcd(self.p, self.q)
        temp_rational = Rational(self.p//gcd, self.q//gcd)
        if temp_rational.get_denominator() < 0:
            temp_rational = Rational(-self.p//gcd, -self.q//gcd)
        return temp_rational

    def inverse(self):
        """
        :return: The inverse of self.
        """
        return Rational(self.q, self.p)

    def scale(self, scalar: int) -> "Rational":
        """
        Returns scaled self but does not change underlying value. Ie, self = self.scale(m) for all m.
        :return: Scaled version of self.
        """
        return Rational(self.p * scalar, self.q * scalar)

    def is_integer(self) -> bool:
        """
        :return: Whether self can be represented as an integer without losing information.
        """
        return self.simplify().get_denominator() == 1
