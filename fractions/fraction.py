"""
Copyright (C) 2018  Adam Goertz

This program is free software: you may redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but without any guarantee of its fitness for any particular purpose. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
"""


class fraction:
    def __init__(self, numer, denom=1):
        """Instatiates a fraction object.

        Arguments:
            numerator : int, fraction
            denominator : int, fraction (default = 1)
        """

        if (denom == 0):
            raise ValueError("denominator cannot be 0.")

        if (isinstance(numer, int) and isinstance(denom, int)):
            self.numer = numer
            self.denom = denom

        elif (isinstance(numer, fraction) or isinstance(denom, fraction)):
            f = numer / denom
            self.numer = f.numer
            self.denom = f.denom

        else:
            raise TypeError("invalid argument type(s) in constructor: must be types 'int' or 'fraction'.")


    def __repr__(self):
        return f'fraction({self.numer}, {self.denom})'

    def __str__(self):
        return f'{self.numer}/{self.denom}'

    # Auiliary Methods =========================================================
    @staticmethod
    def to_fraction(decimal : float) -> 'fraction':
        """Converts a decimal value into a 'fraction' object."""

        magnitude = 1
        while (decimal // 1) != decimal:
            decimal *= 10
            magnitude *= 10

        return fraction(int(decimal), magnitude).simplify()


    def to_float(self) -> float:
        """Converts a fraction object to floating-point representation."""

        return self.numer / self.denom


    def get_proper(self):
        """Returns the fraction as a tuple containing an integer and a proper fraction."""

        coeff = self.numer // self.denom
        pfrac = self.numer % self.denom

        return (coeff, fraction(pfrac, abs(self.denom)).simplify())

    @staticmethod
    def _gcd(n1 : int, n2 : int) -> int:
        """Euclidean algorithm for finding greatest common divisor."""

        d1 = abs(n1)
        d2 = abs(n2)

        a = max(d1, d2)
        b = min(d1, d2)
        while True:
            if a == 0:
                return b
            elif b == 0:
                return a

            r = (a % b)
            a = max(b, r)
            b = min(b, r)


    @staticmethod
    def _lcm(n1 : int, n2 : int) -> int:
        """Returns the least common multiple of two integers."""

        return (n1 // fraction._gcd(n1, n2)) * n2


    def reciprocal(self) -> 'fraction':
        """Returns the reciprocal of a fraction object."""

        return fraction(self.denom, self.numer)


    def simplify(self) -> 'fraction':
        """Returns the calling fraction in its lowest terms."""

        gcd = fraction._gcd(self.numer, self.denom)

        return fraction(self.numer // gcd, self.denom // gcd)



    #Addition ==================================================================

    def __add__(self, other):
        if isinstance(other, fraction):
            d = fraction._lcm(self.denom, other.denom)
            n2 = (d // other.denom) * other.numer
        elif isinstance(other, int):
            d = self.denom
            n2 = other * d
        else:
            raise TypeError("operands must be of type 'fraction' or 'int'.")

        n1 = (d // self.denom) * self.numer

        return fraction((n1 + n2), d).simplify()

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    # Subtraction ==============================================================

    def __sub__(self, other):
        return self + (other * -1)

    def __rsub__(self, other):
        return (self * -1) + other

    def __isub__(self, other):
        return self - other

    # Multiplication ===========================================================

    def __mul__(self, other):
        if isinstance(other, fraction):
            return fraction(self.numer * other.numer, self.denom * other.denom).simplify()
        elif isinstance(other, int):
            return fraction(self.numer * other, self.denom).simplify()
        else:
            raise TypeError("operands must be of type 'fraction' or 'int'.")

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        return self * other


    # Division =================================================================

    def __truediv__(self, other):
        if (isinstance(other, fraction)):
            return self * other.reciprocal()
        elif (isinstance(other, int)):
            return self * fraction(1, other)
        else:
            raise TypeError("operands must be of type 'fraction' or 'int'.")

    def __rtruediv__(self, other):
        return self.reciprocal() * other

    def __itruediv__(self, other):
        return self / other

    # Other ====================================================================

    def __neg__(self):
        return self * -1

    def __abs__(self):
        return fraction(abs(self.numer), abs(self.denom))

    def __float__(self):
        return self.numer / self.denom

    def __int__(self):
        return self.numer // self.denom

    def __round__(self, numDigits=0):
        return round(self.numer / self.denom, numDigits)


    # Comparisons ==============================================================

    def __eq__(self, other):
        if isinstance(other, fraction):
            return (self.numer * other.denom) == (self.denom * other.numer)
        elif isinstance(other, int) or isinstance(other, float):
            return (self.numer / self.denom) == other
        else:
            raise TypeError("operands must be of type 'fraction', 'float', or 'int'.")

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if isinstance(other, fraction):
            return (self.numer * other.denom) < (self.denom * other.numer)
        elif isinstance(other, int) or isinstance(other, float):
            return (self.numer / self.denom) < other
        else:
            raise TypeError("operands must be of type 'fraction', 'float', or 'int'.")

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        if isinstance(other, fraction):
            return (self.numer * other.denom) > (self.denom * other.numer)
        elif isinstance(other, int) or isinstance(other, float):
            return (self.numer / self.denom) > other
        else:
            raise TypeError("operands must be of type 'fraction', 'float', or 'int'.")

    def __ge__(self, other):
        return self > other or self == other

    def __bool__(self):
        return self.numer != 0
