from copy import copy, deepcopy
import sys

class Dimacs:
	def __init__(self, str):
		self.formula = str
		self.answer = False
		self.clauses = []
		self.startClauses = []
		self.valuations = {}

	def parse(self):
		'''
			Parsing input formula
		'''
		lines_raw = self.formula.split('\n')
		lines = list(filter(lambda x: x!= '' and (x[0] == 'p' or x[0] == '-' or x[0].isdigit()), lines_raw))
		self.numLiterals = int(lines[0].strip().split(' ')[3])
		for i in range(1, len(lines)):
			tmpList = []
			for word in lines[i].strip().split(' '):
				if word != '' and int(word) != 0:
					tmpList.append(word)
			if tmpList != []:
				self.clauses.append(tmpList)
				self.startClauses.append(tmpList)

	def changeTF(self):
		'''
			Changing -T to F and -F to T
		'''
#		print('changeTF')
#		print(self.clauses)
		for i in range(len(self.clauses)):
			for j in range(len(self.clauses[i])):
				if '-T' == self.clauses[i][j]:
					self.clauses[i][j] = 'F'
				if '-F' == self.clauses[i][j]:
					self.clauses[i][j] = 'T'

	def removeF(self):
		'''
			Removing F-s from clauses
		'''
#		print('removeF')
#		print(self.clauses)
		currentClauses = []
		for i in range(len(self.clauses)):
			tmpCurrentClauses = []
			for j in range(len(self.clauses[i])):
				if self.clauses[i][j] != 'F':
					tmpCurrentClauses.append(self.clauses[i][j])
			currentClauses.append(tmpCurrentClauses)
		self.clauses = currentClauses

	def checkEmpty(self):
		'''
			If there is an empty clause return False
		'''
#		print('checkEmpty')
#		print(self.clauses)
		for clause in self.clauses:
			if len(clause) == 0:
				return False
		return True

	def tautology(self):
		'''
			Removing clauses containing T-s or variable and it's negation
		'''
#		print('tautology')
#		print(self.clauses)
		currentClauses = []
		for i in range(len(self.clauses)):
			hasT = False
			if 'T' in self.clauses[i]:
				hasT = True
			for j in range(1, self.numLiterals + 1):
				if str(j) in self.clauses[i] and str(-j) in self.clauses[i]:
					hasT = True
			if not hasT:
				currentClauses.append(self.clauses[i])
		self.clauses = currentClauses

	def setValuation(self, var):
		'''
			Setting valuation of var
		'''
		if int(var) < 0:
			self.valuations[-int(var)] = False
		else:
			self.valuations[int(var)] = True

	def changeClauses(self, var):
		'''
			Changing clauses after set valuation
		'''
		for i in range(len(self.clauses)):
			for j in range(len(self.clauses[i])):
				if self.clauses[i][j] == str(var):
					self.clauses[i][j] = 'T'
				elif self.clauses[i][j] == str(-int(var)):
					self.clauses[i][j] = 'F'

	def unitPropagation(self):
		'''
			Finding clauses containing one variable and setting its valuation
		'''
#		print('unitPropagation')
#		print(self.clauses)
		for i in range(len(self.clauses)):
			if len(self.clauses[i]) == 1:
				self.setValuation(self.clauses[i][0])
				self.changeClauses(self.clauses[i][0])
				return self.dimacs()

	def pureLiteral(self):
		'''
			Setting valuation of variables which are pure or pure negation
		'''
#		print('pureLiteral')
#		print(self.clauses)
		mapLiterals = {}
		for i in range(1, self.numLiterals + 1):
			mapLiterals[i] = [0, 0]

		for i in range(len(self.clauses)):
			for j in range(len(self.clauses[i])):
				if int(self.clauses[i][j]) in mapLiterals.keys():
					mapLiterals[int(self.clauses[i][j])][1] = 1
				else:
					mapLiterals[-int(self.clauses[i][j])][0] = 1

		for k, v in mapLiterals.items():
			if v == [0, 1]:
				self.setValuation(k)
				self.changeClauses(k)
				return self.dimacs()
			elif v == [1, 0]:
				self.setValuation(-k)
				self.changeClauses(-k)
				return self.dimacs()

	def split(self):
		'''
			Splitting on minimum variable which doesn't have its valuation set
		'''
		splitVar = min(list(filter(lambda x: x not in self.valuations, range(1, self.numLiterals + 1))))

		savedClauses = deepcopy(self.clauses)
		savedValuations = deepcopy(self.valuations)

#		print('split: ' + str(splitVar))
#		print(self.clauses)
		self.setValuation(splitVar)
		self.changeClauses(splitVar)

		if self.dimacs():
			return True
		else:
			self.changeTF()
#			print('split: ' + str(-splitVar))
#			print(self.clauses)
			self.clauses = deepcopy(savedClauses)
			self.valuations = deepcopy(savedValuations)

			self.setValuation(-splitVar)
			self.changeClauses(-splitVar)
			return self.dimacs()

	def dimacs(self):
		if len(self.clauses) == 0:
			return True

		self.changeTF()

		self.removeF()

		if False == self.checkEmpty():
			return False

		self.tautology()

		if len(self.clauses) == 0:
			return True

		if False == self.unitPropagation():
			return False

		if len(self.clauses) == 0:
			return True

		if False == self.pureLiteral():
			return False

		if len(self.clauses) == 0:
			return True

		return self.split()

	def doIt(self):
		self.parse()
		self.answer = self.dimacs()
		#print(self.startClauses)
		print(self.answer)
		if self.answer:
			print(self.valuations)

def main():
	if len(sys.argv) != 2:
		exit(1)
	with open(sys.argv[1], 'r') as f:
		text = str(f.read())
		dim = Dimacs(text)
		dim.doIt()

if __name__ == '__main__':
	main();
