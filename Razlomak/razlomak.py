from fractions import gcd

class Razlomak:
	def __init__(self, a, b = 1):
		self.razlomak = [a, b]

	def __add__(self, other):
		if not isinstance(other, Razlomak):
			other = Razlomak(other)
		a = self.razlomak[0]*other.razlomak[1] + self.razlomak[1]*other.razlomak[0]
		b = self.razlomak[1]*other.razlomak[1]
		d = gcd(a, b)
		return Razlomak(int(a/d), int(b/d))

	def __sub__(self, other):
		if not isinstance(other, Razlomak):
			other = Razlomak(other)
		a = self.razlomak[0]*other.razlomak[1] - self.razlomak[1]*other.razlomak[0]
		b = self.razlomak[1]*other.razlomak[1]
		d = gcd(a, b)
		return Razlomak(int(a/d), int(b/d))

	def __mul__(self, other):
		if not isinstance(other, Razlomak):
			other = Razlomak(other)
		a = self.razlomak[0]*other.razlomak[0]
		b = self.razlomak[1]*other.razlomak[1]
		d = gcd(a, b)
		return Razlomak(int(a/d), int(b/d))

	def __truediv__(self, other):
		if not isinstance(other, Razlomak):
			other = Razlomak(other)
		return self.__mul__(Razlomak(other.razlomak[1], other.razlomak[0]))

	def __lt__(self, other):
		if not isinstance(other, Razlomak):
			other = Razlomak(other)
		a = float(self.razlomak[0])/self.razlomak[1]
		b = float(other.razlomak[0])/other.razlomak[1]
		if a < b:
			return True
		return False

	def __gt__(self, other):
		if not isinstance(other, Razlomak):
			other = Razlomak(other)
		a = float(self.razlomak[0])/self.razlomak[1]
		b = float(other.razlomak[0])/other.razlomak[1]
		if a > b:
			return True
		return False

	def __eq__(self, other):
		return not (self < other or self > other)

	def __str__(self):
		if self.razlomak[0] == 0:
			return '0'
		if self.razlomak[1] == 1:
			return str(self.razlomak[0])
		return str(self.razlomak[0]) + '/' + str(self.razlomak[1])