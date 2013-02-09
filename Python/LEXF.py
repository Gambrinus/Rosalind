#!/usr/bin/env python

"""	Rosalind project - Problem: Enumerating k-mers Lexicographically
	Problem
	Assume that an alphabet A has a predetermined order; that is, we write
	the alphabet as a permutation A=(a1,a2,...,ak), where a1<a2<?<ak. For instance,
	the English alphabet is organized as (A,B,...,Z).
	Given two strings s=s1s2?sn and t=t1t2?tn of the same length, we say that s precedes
	t in the lexicographic order (and write s<Lext) if the first symbol s[j] that doesn't
	match t[j] satisfies sj<tj in A.
	
	Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n=10).
	Return: All strings of length n that can be formed from the alphabet, ordered lexicographically.
	
	Sample Dataset
	T A G C
	2
	Sample Output
	TT
	TA
	TG
	TC
	AT
	AA
	AG
	AC
	GT
	GA
	GG
	GC
	CT
	CA
	CG
	CC
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import itertools

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('LEXF_output.txt','w')

lines = filein.readlines()

symlist = "".join(lines[0].split())
reps = int(lines[1])

lexlist = list(itertools.product(symlist, repeat=reps))

kmer = []
for sym in lexlist:
	y = ''
	for x in sym:
		y += x
	kmer.append(y)

for k in kmer:
	print k
	if k == kmer[0]:
		fileout.write(k)
	else:
		fileout.write('\n')
		fileout.write(k)

print len(symlist)**reps, 'expected kmers'
print len(kmer), 'generated kmers'