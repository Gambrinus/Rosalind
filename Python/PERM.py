#!/usr/bin/env python

"""	Rosalind project - Problem: Enumerating Gene Orders
	A permutation of length n is some ordering of the positive
	integers {1,2,...,n}. For example, p=(5,3,2,1,4) is a permutation
	of length 5.
	
	Given: A positive integer n=7.
	Return: The total number of permutations of length n, followed
	by a list of all such permutations (in any order).
	
	Sample Dataset
	3
	Sample Output
	6
	1 2 3
	1 3 2
	2 1 3
	2 3 1
	3 1 2
	3 2 1
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

def permute(word):
	retList=[]
	if len(word) == 1:
		retList.append(word)
	else:
		for pos in range(len(word)):
			permuteList=permute(word[0:pos]+word[pos+1:len(word)])
			for item in permuteList:
				retList.append(word[pos]+item)
	return list(set(retList))

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('PERM_output.txt','w')

lines = filein.readlines()

seqlist = range(int(lines[0]))
seq = ''
for x in seqlist:
	seq += str(x+1)

perms = sorted(permute(seq))
print len(perms)
fileout.write(str(len(perms)))
formats = []
for y in perms:
	format = ''	
	for i in y:
		if i == y[0]:
			format = i
		else:
			format += ' ' + i
	formats.append(format)

for format in formats:
	print format
	fileout.write('\n')
	fileout.write(format)