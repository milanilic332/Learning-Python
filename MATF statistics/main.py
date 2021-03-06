import urllib.request as urlr
import sys, re, os
import numpy as np
import matplotlib.pyplot as plt

def main():
	with urlr.urlopen("http://www.matf.bg.ac.rs/svo-osoblje/") as response:
		html = str(response.read().decode('utf-8'))
		emp = re.compile(r'<h4><a[^>]+>([^<]+)')
		names = findNames(emp, html)

		firstLetterDist(names)
		letterDist(names)
		fullnamesAlas()

		plt.show()
		
def fullnamesAlas():
	with open('list.txt', 'r') as f:
		hypatia = f.read()
		Names = {}
		n = re.compile(r'[^\']+\'[^\']+\'[^\']+\'([^\']+)\'\]')
		for match in n.finditer(hypatia):
			lst = match.group(1).split(' ')
			for i in lst:
				if i in Names:
					Names[i] = Names[i] + 1
				else:
					Names[i] = 1

		sortedNamesLst = sorted(Names.items(), key=lambda x: x[1])[::-1]
		sortedNamesLst = sortedNamesLst[:40]
		sortedNamesLst = sortedNamesLst[::-1]
		sortedNamesMap = {}

		for ind, (i, j) in enumerate(sortedNamesLst):
			if ind != 39:
				sortedNamesMap[i] = j
			else:
				break

		pos = np.arange(len(sortedNamesMap.values())) + 0.5

		plt.figure(3)
		plt.barh(pos, list(sortedNamesMap.values()), align = 'center')
		plt.yticks(pos, sortedNamesMap.keys())
		plt.ylabel('Imena')
		plt.xlabel('Broj pojavljivanja')
		plt.title('Raspodela imena na alasu')

def findNames(emp, html):
	names = []
	for match in emp.finditer(html):
		if match.group(1)[2] != ' ':
			names.append(match.group(1).strip())
		else:
			names.append(match.group(1)[3:].strip())
	return names		
		
def firstLetterDist(names):
	firstLetters = {}
	for i in 'АБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЧЏШ':
		firstLetters[i] = 0
	
	for name in names:
		firstLetters[name[0]] = firstLetters.get(name[0], 0) + 1

	sortedFirstLettersList = sorted(firstLetters.items(), key=lambda x: x[1])[::-1]
	
	sortedFirstLetters = {}
	
	for (a, b) in sortedFirstLettersList:
		sortedFirstLetters[a] = b

	plt.figure(2)
	plt.bar(sortedFirstLetters.keys(), sortedFirstLetters.values())
	plt.ylabel('Broj pojavljivanja')
	plt.xlabel('Slova')
	plt.title('Raspodela pocetnih slova u imenu')

def letterDist(names):
	letters = {}
	for i in 'АБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЧЏШ':
		letters[i] = 0
	for name in names:
		for let in name:
			if let not in '.- ':
				let = let.upper()
				letters[let] = letters.get(let, 0) + 1
	
	sortedLettersList = sorted(letters.items(), key=lambda x: x[1])[::-1]
	sortedLetters = {}
	
	for (a, b) in sortedLettersList:
		sortedLetters[a] = b

	plt.figure(1)
	plt.bar(sortedLetters.keys(), sortedLetters.values())
	plt.ylabel('Broj pojavljivanja')
	plt.xlabel('Slova')
	plt.title('Raspodela svih slova u imenu i prezimenu')

if __name__ == '__main__':
	main()