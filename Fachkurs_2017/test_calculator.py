from calculator import *

def test_trivial_example():
	assert 1 == 1

def test_fraction_init():
	frac = Fraction(3, 4)
	assert frac.numerator == 3
	assert frac.denominator == 4

def test_fraction_equate():
	assert Fraction(1, 2) == Fraction(1, 2)
	assert Fraction(1, 3) != Fraction(1, 2)

def test_fraction_simplify():
	assert Fraction(1, 3) == Fraction(2, 6)

def test_multiply():
	assert Fraction(1, 2) * Fraction(1, 2) == Fraction(1, 4)

def test_fraction_addition():
	assert Fraction(1, 2) + Fraction(1, 4) == Fraction(3, 4)

def test_sum():
	assert Sum(Fraction(1, 2), Fraction(1, 4)).evaluate() == Fraction(3, 4)

def test_product():
	assert Product(Fraction(1, 3), Fraction(1, 3)).evaluate() == Fraction(1, 9)