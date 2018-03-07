from math import pi, sqrt, factorial

class Elipsa():
	def __init__(self, centar = (0, 0), a = 1, b = 1):
		self.centar = tuple(centar)
		self.a = a
		self.b = b
		self.povrsina = a*b*pi
		self.c = sqrt(a**2 - b**2)
		self.zize = [(-self.c, centar[0]), (self.c, centar[0])]

	def transliraj(self, vektor):
		self.centar = (self.centar[0] + vektor[0], self.centar[1] + vektor[1])

	def __str__(self):
		return self.__class__.__name__ + ' | Centar: ' + str((round(self.centar[0]), round(self.centar[1]))) + \
			'. Poluose: a = ' + str(round(self.a), 2) + ', b = ' + str(round(self.b), 2) + \
			'. Povrsina: ' + str(round(self.povrsina, 2)) + '.'

class Krug(Elipsa):
	def __init__(self, centar = (0, 0), r = 1):
		super().__init__(centar, r, r)
		self.obim = r*2*pi

	def __str__(self):
		return self.__class__.__name__ + ' | Centar: ' + str((round(self.centar[0]), round(self.centar[1]))) + \
			'. Obim: ' + str(round(self.obim, 2)) + '. Povrsina: ' + str(round(self.povrsina, 2)) + '.'

class BezijerovaKriva():
	def __init__(self, tacke):
		self.tacke = list(tacke)

	def func(self, t):
		if t < 0 or t > 1:
			print('Pogresno t')
			sys.exit(1)
		x = 0
		y = 0
		n = len(self.tacke)
		for i in range(0, n):
			x += (factorial(n - 1)/(factorial(i)*factorial(n - i - 1)))*t**i*(1 - t)**(n - i - 1)*self.tacke[i][0]
			y += (factorial(n - 1)/(factorial(i)*factorial(n - i - 1)))*t**i*(1 - t)**(n - i - 1)*self.tacke[i][1]
		return 'Tacke za t = ' + str(t) + ' je ' + str((x, y)) + '.'

	def __str__(self):
		return str(self.__class__.__name__) + ' | Kontrolne tacke: ' + \
			str([(round(x, 2), round(y, 2)) for (x, y) in self.tacke]) + '.'
	