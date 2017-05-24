from math import gcd


class Expression:
	def evaluate(self):
		pass


class Operation(Expression):
	def __init__(self, left_op, right_op):
		assert isinstance(left_op, Expression) and isinstance(right_op, Expression)

		self.left_op = left_op
		self.right_op = right_op


class Sum(Operation):
	def evaluate(self):
		return self.left_op.evaluate() + self.right_op.evaluate()


class Product(Operation):
	def evaluate(self):
		return self.left_op.evaluate() * self.right_op.evaluate()


class Difference(Operation):
	def evaluate(self):
		return self.left_op.evaluate() - self.right_op.evaluate()


class Quotient(Operation):
	def evaluate(self):
		return self.left_op.evaluate() // self.right_op.evaluate()


class Fraction(Expression):
	def __init__(self, numerator, denominator):
		if denominator == 0:
			raise ZeorDivisionError

		self.numerator = numerator
		self.denominator = denominator
		self.simplify()

	def __eq__(self, other):
		return self.numerator == other.numerator and self.denominator == other.denominator

	def __mul__(self, other):
		return self.product(other)

	def __add__(self, other):
		return self.add(other)

	def add(self, other):
		return Fraction(self.numerator * other.denominator + self.denominator * other.numerator,
						self.denominator * other.denominator)

	def evaluate(self):
		return self

	def simplify(self):
		divisor = gcd(self.numerator, self.denominator)
		self.numerator = self.numerator // divisor
		self.denominator = self.denominator // divisor

	def product(self, other):
		return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)