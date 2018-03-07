from poligoni import *
from krive import *

def main():
	X = Kvadrat([(-1, -1), (1, -1), (1, 1), (-1, 1)])
	Y = Poligon([(-1, -1), (1, -1), (1, 1)])
	Z = Trougao([(0, 0), (1, 0), (0, 1)])
	K = Krug((0, 0), 5)
	R = BezijerovaKriva([(0, 0), (1, 1), (0, 2)])
	X.rotiraj(180)
	print(K)
	print(X)
	print(Y)
	print(Z)
	print(R)
	print(R.func(0.5))

if __name__ == '__main__':
	main()