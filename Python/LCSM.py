#!/usr/bin/env python

"""	Rosalind project - Problem: Finding a Shared Motif
	Problem
	A common substring of a collection of strings is a substring of every member of
	the collection. We say that a common substring is a longest common substring if a
	longer common substring of the collection does not exist. For example, CG is a common
	substring of ACGTACGT and AACCGGTATA, whereas GTA is a longest common substring. Note
	that multiple longest common substrings may exist.
	
	Given: A collection of k DNA strings (of length at most 1 kbp each; k=100).
	Return: A longest common substring of the collection. (If multiple solutions exist,
	you may return any single solution.)
	
	Sample Dataset
	GATTACA
	TAGACCA
	ATACA
	Sample Output
	AC
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('LCSM_output.txt','w')

lines = filein.readlines()
first = lines[0].rstrip()

i=0
chunks = []
while (i <= len(first)):
	k = 1
	while k <= len(first):
		j = i + k
		if j <= len(first):
			chunks.append(first[i:j])
		k += 1
	i += 1

chunks = set(chunks)
chunks = list(chunks)
chunks.sort(key=len,reverse=True)
chunks = list(chunks)

stop = 0
for chunk in chunks:
	m = 1
	while m < len(lines) and stop == 0:
		if lines[m].count(chunk):
			if m == len(lines)-1:
				consensus = chunk
				fileout.write(chunk)
				stop += 1
			m += 1
		else:
			m = len(lines)
			
print len(chunks), 'chunks'
print consensus, len(consensus), 'bp'