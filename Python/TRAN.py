#!/usr/bin/env python

""" Rosalind project - Problem: Transitions and Transversions
Problem
For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2)
is the ratio of the total number of transitions to the total number of transversions, where
symbol substitutions are inferred from mismatched corresponding symbols as when calculating
Hamming distance (see "Counting Point Mutations").

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
Return: The transition/transversion ratio R(s1,s2).

Sample Dataset
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT
Sample Output
1.21428571429
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import sys
import types

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

def trans_ratio(seq1,seq2):
	transitions = 0
	transversions = 0
	ition_def = ('AG','CT')
	version_def = ('AC','AT','CG','GT')
	for x in range(0,len(seq1)):
		pair = ''.join(sorted((seq1[x],seq2[x]), key=str.upper))
		if pair in ition_def:
			transitions += 1
		elif pair in version_def:
			transversions += 1
	return float(transitions)/float(transversions)

if len(sys.argv) >= 2 and sys.argv[1] == "-t":
	filein = open('test_input.txt', 'r')
	lines = filein.read().splitlines()
	filein.close
else:
	filein = open('rosalind_tran.txt', 'r')
	lines = filein.read().splitlines()
	filein.close

seqs = parse_fasta(lines)

out = str(trans_ratio(seqs[0][1],seqs[1][1]))

fileout = open('TRAN_output.txt','w')
fileout.write(out)						# writes to file, closes file, and rereads file
fileout.close 							# to make sure the output is correct in the file
fileout = open('TRAN_output.txt','r')
print fileout.read()
fileout.close