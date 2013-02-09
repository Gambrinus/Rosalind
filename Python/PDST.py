#!/usr/bin/env python

""" Rosalind project - Problem: Creating a Distance Matrix
Problem
For two strings s1 and s2 of equal length, the p-distance between them, denoted p(s1,s2), is
the proportion of corresponding symbols that differ between s1 and s2.
For a distance function d on n taxa s1,s2,...,sn (taxa are often represented by genetic strings),
we may encode the distances between pairs of taxa via a distance matrix D in which Di,j=d(si,sj).

Given: A collection of n (n<=10) DNA strings s1,...,sn of equal length (at most 1 kbp). Strings are
given in FASTA format.
Return: The matrix D corresponding to the p-distance on the given strings. All entries of D should
be given to an accuracy of 2 decimal places.

Sample Dataset
>Rosalind_9499
TTTCCATTTA
>Rosalind_0942
GATTCATTTC
>Rosalind_6568
TTTCCATTTT
>Rosalind_1833
GTTCCATTTA
Sample Output
0.0 0.4 0.1 0.1
0.4 0.0 0.4 0.3
0.1 0.4 0.0 0.2
0.1 0.3 0.2 0.0
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import sys
import types
import operator

def parse_fasta(lines):
	seqnum = 0
	for line in lines:
		if line.count('>'):
			seqnum += 1
	lineeach = [str]*(seqnum *2)
	i = 0
	for line in lines:
		if line.count('>'):
			if i > 0:
				i += 1
			line = line.replace('>','')
			lineeach[i] = line.rstrip()
			i += 1
		else:
			if isinstance(lineeach[i], types.StringTypes):
				lineeach[i] = lineeach[i] + line.rstrip()
			else:
				lineeach[i] = line.rstrip()
	ret = [str]*((len(lineeach)/2))
	i = 0
	j = 0
	while i < len(lineeach):
		ret[j] = [lineeach[i],lineeach[i+1]]
		i += 2
		j += 1
	return ret

def HAMM(seq1,seq2):
	return map(operator.eq, seq1, seq2).count(False)

filein = open(sys.argv[1], 'r')
lines = filein.read().splitlines()
filein.close
fileout = open('PDST_output.txt','w')

seqs = parse_fasta(lines)

i = 0
matrix = [int] * len(seqs)
for x in seqs:
	matrix[i] = []
	for y in seqs:
		dist = str(round(float(HAMM(x[1],y[1]))/float(len(x[1])),3))
		matrix[i].append(dist)
	i += 1

for x in matrix:
	out = " ".join(x)
	print out
	fileout.write(str(out))
	fileout.write('\n')