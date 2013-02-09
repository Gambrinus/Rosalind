#!/usr/bin/env python

"""	Rosalind project - Problem: Ordering Strings of Varying Length Lexicographically
	Problem
	Say that we have strings s=s1s2...sm and t=t1t2...tn with m<n. Consider the substring t=t[1:m].
	We have two cases:
	If s=t, then we set s<Lext because s is shorter than t (e.g., APPLE<APPLET).
	Otherwise, s!=t. We define s<Lext if s<Lext and define s>Lext if s>Lext (e.g., APPLET<LexARTS
	because APPL<LexARTS).
	
	Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n<=12).
	Return: All strings of length at most n formed from A, ordered lexicographically. (Note: As
	in Enumerating k-mers Lexicographically, alphabet order is based on the order in which the symbols are given.)
	
	Sample Dataset
	D N A
	3
	Sample Output
	D
	DD
	DDD
	DDN
	DDA
	DN
	DND
	DNN
	DNA
	DA
	DAD
	DAN
	DAA
	N
	ND
	NDD
	NDN
	NDA
	NN
	NND
	NNN
	NNA
	NA
	NAD
	NAN
	NAA
	A
	AD
	ADD
	ADN
	ADA
	AN
	AND
	ANN
	ANA
	AA
	AAD
	AAN
	AAA
	
	Extra Information
	We can combine conditions (1) and (2) above into a single condition by adding a blank character " "
	to the beginning of our ordered alphabet. Then, if s is shorter than t, we simply add as many instances
	of " " as necessary to make s and t the same length.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import itertools

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('LEXFVoutput.txt','w')

lines = filein.readlines()

symlist = "".join(lines[0].split())
reps = int(lines[1])

lexlist = []

x=1
while x<=reps:
	lexlist.append(list(itertools.product(symlist, repeat=x)))
	x+=1

kmer = []
for x in lexlist:
	for y in x:
		kmer.append(y)

lex = lines[0].split()
def custom_key(word):
   numbers = []
   for letter in word:
      numbers.append(lex.index(letter))
   return numbers
   
kmer.sort(key=custom_key)

klist = []
for sym in kmer:
	y = ''
	for x in sym:
		y += x
	klist.append(y)

for k in klist:
	print k
	if k == klist[0]:
		fileout.write(k)
	else:
		fileout.write('\n')
		fileout.write(k)