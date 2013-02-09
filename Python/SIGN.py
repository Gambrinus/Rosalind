#!/usr/bin/env python

"""	Rosalind project - Problem: Enumerating Oriented Gene Orderings
	Problem
	A signed permutation of length n is some ordering of the positive integers {1,2,...,n}
	in which each integer is then provided with either a positive or negative sign (for the
	sake of simplicity, we omit the positive sign). For example, p=(5,-3,-2,1,4) is a signed
	permutation of length 5.
	
	Given: A positive integer n<=6.
	Return: The total number of signed permutations of length n, followed by a list of all such
	permutations (you may list the signed permutations in any order).
	
	Sample Dataset
	2
	Sample Output
	8
	-1 -2
	-1 2
	1 -2
	1 2
	-2 -1
	-2 1
	2 -1
	2 1
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import itertools

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('SIGN_output.txt','w')

lines = filein.readlines()

seqlist = range(int(lines[0]))
seq =[]
for x in seqlist:
	x+=1
	seq.append(x)
	seq.append(-x)
	
perms = list(itertools.permutations(seq, int(lines[0])))  #gets all permutations with no repeats

final = []
for perm in perms:
	i = 0
	for x in perm:
		i += perm.count(x*-1)		#removing perms where x and -x are together
	if i == 0:
		string = ''
		for x in perm:
			string += str(x) + ' '
		final.append(string.rstrip())
		
final.sort()

print len(final)
fileout.write(str(len(final)))
for perm in final:
	print perm
	fileout.write('\n')
	fileout.write(perm)