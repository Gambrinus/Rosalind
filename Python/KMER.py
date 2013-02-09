#!/usr/bin/env python

"""	Rosalind project - Problem: k-Mer Composition
	Problem
	For a fixed positive integer k, order all possible k-mers taken
	from an underlying alphabet lexicographically.
	Then the k-mer composition of a string s can be represented by an
	array A for which A[m] denotes the number of times that the mth k-mer
	(with respect to the lexicographic order) appears in s.
	
	Given: A DNA string s in FASTA format (having length at most 100 kbp).
	Return: The 4-mer composition of s.
	
	Sample Dataset
	>Rosalind_6431
	CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
	CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
	TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
	AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
	GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
	CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
	CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG
	Sample Output
	4 1 4 3 0 1 1 5 1 3 1 2 2 1 2 0 1 1 3 1 2 1 3 1 1 1 1 2 2 5 1 3 0 2 2 1 1 1 1 3 1 0 0 1 5 5 1 5 0 2 0 2 1 2 1 1 1 2 0 1 0 0 1 1 3 2 1 0 3 2 3 0 0 2 0 8 0 0 1 0 2 1 3 0 0 0 1 4 3 2 1 1 3 1 2 1 3 1 2 1 2 1 1 1 2 3 2 1 1 0 1 1 3 2 1 2 6 2 1 1 1 2 3 3 3 2 3 0 3 2 1 1 0 0 1 4 3 0 1 5 0 2 0 1 2 1 3 0 1 2 2 1 1 0 3 0 0 4 5 0 3 0 2 1 1 3 0 3 2 2 1 1 0 2 1 0 2 2 1 2 0 2 2 5 2 2 1 1 2 1 2 2 2 2 1 1 3 4 0 2 1 1 0 1 2 2 1 1 1 5 2 0 3 2 1 1 2 2 3 0 3 0 1 3 1 2 3 0 2 1 2 2 1 2 3 0 1 2 3 1 1 3 1 0 1 1 3 0 2 1 2 2 0 2 1 1
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import itertools
import re
import types

def pairwise(iterable):
    itnext = iter(iterable).next
    while True:
        yield itnext( ), itnext( )

def dictFromSequence(seq):
    return dict(pairwise(seq))

def fasta_parser(lines):
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
			lineeach[i] = line.rstrip()
			i += 1
		else:
			if isinstance(lineeach[i], types.StringTypes):
				lineeach[i] = lineeach[i] + line.rstrip()
			else:
				lineeach[i] = line.rstrip()
	
	return dictFromSequence(lineeach)

def kmer_lex(symlist,k):
	lex_list = list(itertools.product(symlist, repeat=k))
	ret = []
	for kmer in lex_list:
		ret.append(''.join(kmer))
	return ret
	
def count_overlapping(search,seq):
	i=0
	x=0
	while i < len(seq):
		j=i+len(search)
		if search == seq[i:j]:
			x+=1
		i+=1
	return x

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('KMER_output.txt','w')

lines = filein.readlines()

seqdict = fasta_parser(lines)

kmers = kmer_lex(['A','C','G','T'],4)

counts = []
for key in seqdict:
	for kmer in kmers:
		counts.append(str(count_overlapping(kmer,seqdict[key])))
		
out = ' '.join(counts)
print out
fileout.write(out.rstrip())