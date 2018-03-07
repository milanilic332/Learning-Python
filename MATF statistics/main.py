import urllib.request as urlr
import sys, re
import numpy as np
import matplotlib.pyplot as plt

def main():
	with urlr.urlopen("http://www.matf.bg.ac.rs/svo-osoblje/") as response:
		html = str(response.read().decode('utf-8'))
		emp = re.compile(r'<h4><a[^>]+>([^<]+)')
		names = findNames(emp, html)

		firstLetterDist(names)
		letterDist(names)

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
	
	plt.bar(sortedFirstLetters.keys(), sortedFirstLetters.values())
	plt.ylabel('Broj pojavljivanja')
	plt.xlabel('Slova')
	plt.title('Raspodela pocetnih slova u imenu')
	plt.show()

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
	
	plt.bar(sortedLetters.keys(), sortedLetters.values())
	plt.ylabel('Broj pojavljivanja')
	plt.xlabel('Slova')
	plt.title('Raspodela svih slova u imenu i prezimenu')
	plt.show()	

if __name__ == '__main__':
	main()