from math import sqrt, sin, cos, radians
import sys

class Poligon():
	def __init__(self, tacke):
		self.tacke = list(tacke)
		x = 0
		y = 0
		for (i, j) in self.tacke:
			x += i
			y += j
		self.centar = (x/len(self.tacke), y/len(self.tacke))

	@property
	def obim(self):
		length = 0
		for i in range(0, len(self.tacke) - 1):
			length += sqrt((self.tacke[i][0] - self.tacke[i + 1][0])**2 + (self.tacke[i][1] - self.tacke[i + 1][1])**2)
		length += sqrt((self.tacke[-1][0] - self.tacke[0][0])**2 + (self.tacke[-1][1] - self.tacke[0][1])**2)
		return length

	def __str__(self):
		return  str(self.__class__.__name__) + ' | '+ str([(round(x, 2), round(y, 2)) for (x, y) in self.tacke]) + \
			'. Centar je u: ' + str((round(self.centar[0]), round(self.centar[1]))) + \
			'. Obim je ' +  str(round(self.obim, 2)) + '.'

	def transliraj(self, vektor):
		self.centar = (self.centar[0] + vektor[0], self.centar[1] + vektor[1])

	def rotiraj(self, ugao):
		l = []
		for x in range(0, len(self.tacke)):
			lst = list(self.tacke[x])
			lst[0] = (cos(radians(ugao))*lst[0] + (-sin(radians(ugao)))*lst[1])
			lst[1] = (sin(radians(ugao))*lst[0] + cos(radians(ugao))*lst[1])
			t = tuple(lst)
			l.append(t)
		self.tacke = l

class Pravougaonik(Poligon):
	def __init__(self, tacke):
		super().__init__(tacke)

	@property
	def povrsina(self):
		a = sqrt((self.tacke[0][0] - self.tacke[1][0])**2 + (self.tacke[0][1] - self.tacke[1][1])**2)
		b = sqrt((self.tacke[1][0] - self.tacke[2][0])**2 + (self.tacke[1][1] - self.tacke[2][1])**2)
		return a*b

	def __str__(self):
		return super().__str__() + ' Povrsina je ' + str(round(self.povrsina, 2)) + '.'

class Kvadrat(Pravougaonik):
	def __init__(self, tacke):
		a = sqrt((tacke[0][0] - tacke[1][0])**2 + (tacke[0][1] - tacke[1][1])**2)
		b = sqrt((tacke[1][0] - tacke[2][0])**2 + (tacke[1][1] - tacke[2][1])**2)
		c = sqrt((tacke[2][0] - tacke[3][0])**2 + (tacke[2][1] - tacke[3][1])**2)
		d = sqrt((tacke[3][0] - tacke[0][0])**2 + (tacke[3][1] - tacke[0][1])**2)
		if 4*a != a + b + c + d:
			print('Niste uneli pravilan kvadrat')
			sys.exit(1)
		super().__init__(tacke)

class Trougao(Poligon):
	def __init__(self, tacke):
		if len(tacke) != 3:
			print('Niste uneli 3 temena')
			sys.exit(1)
		super().__init__(tacke)

	@property
	def povrsina(self):
		a = sqrt((self.tacke[0][0] - self.tacke[1][0])**2 + (self.tacke[0][1] - self.tacke[1][1])**2)
		b = sqrt((self.tacke[1][0] - self.tacke[2][0])**2 + (self.tacke[1][1] - self.tacke[2][1])**2)
		c = sqrt((self.tacke[2][0] - self.tacke[0][0])**2 + (self.tacke[2][1] - self.tacke[0][1])**2)
		s = self.obim/2
		return sqrt(s*(s - a)*(s - b)*(s - c))

	def __str__(self):
		return super().__str__() + ' Povrsina je ' + str(round(self.povrsina, 2)) + '.'