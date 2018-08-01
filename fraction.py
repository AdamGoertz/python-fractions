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
        assert (isinstance(numer, int) and isinstance(denom, int))

        if (denom == 0):
            raise ValueError("denominator cannot be 0.")
        else:
            self.numer = numer
            self.denom = denom

    def __repr__(self):
        return f'fraction({self.numer}, {self.denom})'


    def __str__(self):
        return f'{self.numer}/{self.denom}'

    # Auiliary Methods =========================================================
    @staticmethod
    def to_fraction(decimal):
        """Converts decimal values into 'fraction' objects."""

        magnitude = 1
        while (decimal // 1) != decimal:
            decimal *= 10
            magnitude *= 10
        return fraction(int(decimal), magnitude).simplify()

    @staticmethod
    def to_float(frac):
        """Converts fraction object to floating-point representation."""

        if isinstance(fracion, frac):
            return frac.numer / frac.denom
        else:
            raise TypeError("argument must be of type 'fraction'.")

    @staticmethod
    def _gcd(n1, n2):
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
    def _lcm(n1, n2):
        """Returns the least common multiple of two integers."""

        return (n1 // fraction._gcd(n1, n2)) * n2


    def reciprocal(self):
        return fraction(self.denom, self.numer)


    def simplify(self):
        gcd = fraction._gcd(self.numer, self.denom)

        return fraction(self.numer // gcd, self.denom // gcd)


    def get_proper(self):
        """Returns the fraction as a tuple containing an integer and a proper fraction."""

        coeff = self.numer // self.denom
        pfrac = self.numer % self.denom

        return (coeff, fraction(pfrac, abs(self.denom)).simplify())


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
        self = self + other

    # Subtraction ==============================================================

    def __sub__(self, other):
        return self + (other * -1)

    def __rsub__(self, other):
        return (self * -1) + other

    def __isub__(self, other):
        self = self - other

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
        self = self * other

    # Division =================================================================

    def __truediv__(self, other):
        return self * other.reciprocal()

    def __rtruediv__(self, other):
        return self.reciprocal() * other

    def __itruediv__(self, other):
        self = self / other

    # Other ====================================================================

    def __neg__(self):
        return self * -1

    def __abs__(self):
        return fraction(abs(self.numer), abs(self.denom))

    def __float__(self):
        return self.numer / self.denom

    def __int__(self):
        return self.numer // self.denom

    def __round__(self):
        return int(self)

    def __ceil__(self):
        if self.numer % self.denom == 0:
            return int(self)
        else:
            return int(self) + 1

    def __floor__(self):
        return int(self)

    # Comparisons ==============================================================
    # It isn't strictly necessary to implement ALL of these methods, as some
    # will be defined automatically, for example x < y <==> y > x

    def __eq__(self, other):
        if isinstance(other, fraction):
            return (self.numer * other.denom) == (self.denom * other.numer)
        elif isinstance(other, int):
            return (self.numer // self.denom) == other
        else:
            raise TypeError("operands must be of type 'fraction' or 'int'.")

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if isinstance(other, fraction):
            return (self.numer * other.denom) < (self.denom * other.numer)
        elif isinstance(other, int):
            return (self.numer // self.denom) < other
        else:
            raise TypeError("operands must be of type 'fraction' or 'int'.")

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        if isinstance(other, fraction):
            return (self.numer * other.denom) > (self.denom * other.numer)
        elif isinstance(other, int):
            return (self.numer // self.denom) > other
        else:
            raise TypeError("operands must be of type 'fraction' or 'int'.")

    def __ge__(self, other):
        return self > other or self == other

    def __bool__(self):
        return self.numer != 0
