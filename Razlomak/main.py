from razlomak import Razlomak

def main():
	r1 = Razlomak(1, 2)
	r2 = Razlomak(2, 4)
	print(r1 + r2)
	print(r1 - r2)
	print(r1*r2)
	print(r1/r2)
	print(r1 == r2)
	print(r1 < r2)
	print(r1 > r2)

if __name__ == '__main__':
	main()