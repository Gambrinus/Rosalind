#!/usr/bin/env python

"""	Rosalind project - Error Correction in Reads
	Problem
	As is the case with point mutations, the most common type of sequencing
	error occurs when a single nucleotide from a read is interpreted incorrectly.
	
	Given: A collection of up to 1000 reads of equal length (at most 50 bp). Some
	of these reads were generated with a single-nucleotide error. For each read s in
	the dataset, one of the following applies:
	1. s was correctly sequenced and appears in the dataset at least twice
	(possibly as a reverse complement);
	2. s is incorrect, it appears in the dataset exactly once, and its Hamming
	distance is 1 with respect to exactly one correct read in the dataset (or its
	reverse complement).
	Return: A list of all corrections in the form [old read]->[new read].
	(Each correction must be a single symbol substitution, and you may return the
	corrections in any order.)
	
	Sample Dataset
	TCATC
	TTCAT
	TCATC
	TGAAA
	GAGGA
	TTTCA
	ATCAA
	TTGAT
	TTTCC
	Sample Output
	TTCAT->TTGAT
	GAGGA->GATGA
	TTTCC->TTTCA
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import operator

def error_correct(seqs):
	correct = []
	incorrect = []
	x=0
	print len(seqs),"total sequences"
	while x < len(seqs):
		i=0
		y=0
		while y < len(seqs):	#find seqs with matches in the list
			if x != y:
				if seqs[x] == seqs[y] or seqs[x] == revc(seqs[y]):
					i+=1
			y+=1
		if i:
			correct.append(seqs[x])	#append correct matches to list
		else:
			incorrect.append(seqs[x])	#put unique seqs in incorrect list
		x+=1
	correct = list(set(correct)) #removes dups
	i=0
	while i < len(correct):
		for seq in correct:
			if correct[i] == revc(seq) and correct[i] != seq:
				correct.pop(i)	#removes seqs who have common rev com making a truly unique list 
		i+=1
	print len(correct),"correct sequences"
	print len(incorrect),"incorrect sequences"
	for seq1 in incorrect:
		for seq2 in correct:
			if HAMM(seq1,seq2)==1:	#if there is a monoerror, HAMM = 1 so yield both seqs incorr and corr
				yield seq1,seq2
				break
			elif HAMM(seq1,revc(seq2))==1: #not sure if this is necessary
				yield seq1,revc(seq2)
				break
def revc(str):
	rev = {'A':'T','T':'A','C':'G','G':'C'}
	seqstr = ''
	for letter in str:
		seqstr += rev[letter]	
	revseq = seqstr[::-1]
	return revseq
	
def HAMM(seq1,seq2):
	return map(operator.eq, seq1, seq2).count(False)

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('CORR_output.txt','w')

lines = filein.read().splitlines()

corrections = list(error_correct(lines))

out=''
for corr in corrections:
	out += corr[0]+'->'+corr[1]+'\n'

print len(corrections),"corrections made"
fileout.write(out.rstrip())