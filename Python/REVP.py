#!/usr/bin/env python

"""	Rosalind project - Problem: Locating Restriction Site
	Problem
	A DNA string is a reverse palindrome if it is equal to its reverse complement.
	For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC.
	
	Given: A DNA string of length at most 1 kbp.
	Return: The position and length of every reverse palindrome in the string having
	length between 4 and 8.
	
	Sample Dataset
	TCAATGCATGCGGGTCTATATGCAT
	Sample Output
	4 6
	5 4
	6 6
	7 4
	17 4
	18 4
	20 6
	21 4
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import re

def revc(str):
	rev = {'A':'T','T':'A','C':'G','G':'C'}
	seqstr = ''
	for letter in str:
		seqstr += rev[letter]	
	revseq = seqstr[::-1]	#reverses the string using extended splice method s[begin:end:step]
	return revseq
	
def slide(str, num):
	retlist = []
	i=0
	while i<=len(str)-num:
		j = i + num
		retlist.append(str[i:j])
		i += 1
	return retlist

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('REVP_output.txt','w')

lines = filein.readlines()

chunks = []
i=4
while i<=8:
	for chunk in slide(lines[0],i):
		if chunk == revc(chunk):
			for loc in [m.start() for m in re.finditer(chunk, lines[0])]:
				chunks.append([(loc+1),len(chunk)])
	i+=1

chunks = dict((x[0], x) for x in chunks).values()
	
for chunk in chunks:
	line = ''
	for x in chunk:
		line += str(x) + ' '
	print line.rstrip()
	if chunk == chunks[0]:
		fileout.write(line.rstrip())
	else:
		fileout.write('\n')
		fileout.write(line.rstrip())