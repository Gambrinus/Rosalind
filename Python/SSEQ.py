#!/usr/bin/env python

"""	Rosalind project - Problem: Finding a Spliced Motif
	Problem
	A subsequence of a string is a collection of symbols contained in order
	(though not necessarily contiguously) in the string (e.g., ACG is a subsequence
	of TATGCTAAGATC). The indices of a subsequence are the positions in the string
	at which the symbols of the subsequence appear; thus, the indices of ACG in
	TATGCTAAGATC can be represented by (2, 5, 9).
	As a substring can have multiple locations, a subsequence can have multiple
	collections of indices, and the same index can be reused in more than one
	appearance of the subsequence; for example, ACG is a subsequence of AACCGGTT
	in 8 different ways.
	
	Given: Two DNA strings s and t (each of length at most 1 kbp).
	Return: One collection of indices of s in which the symbols of t appear as a
	subsequence of s. If multiple solutions exist, you may return any one.
	
	Sample Dataset
	ACGTACGTGACG
	GTA
	Sample Output
	3 8 10
	
	Extra Information
	For the mathematically inclined, we may equivalently say that t=t1t2...tm is
	a subsequence of s=s1s2...sn if the characters of T appear in some order within
	S. Even more formally, a subsequence of s is a string si1si2...sik, where
	1=i1<i2...<ik<n.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import re

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('SSEQ_output.txt','w')

lines = filein.readlines()

pos =[]
for x in lines[1]:
	pos.append([m.start()+1 for m in re.finditer(x,lines[0])])

minpos = [min(pos[0])]
i=1
while i < len(pos):
	j=i-1
	for x in pos[i]:
		if x > minpos[j]:
			minpos.append(x)
			break
	i+=1

out = ''
for x in minpos:
	out += str(x) + ' '

out = out.rstrip()
fileout.write(out)
print out