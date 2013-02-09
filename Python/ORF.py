#!/usr/bin/env python

"""	Rosalind project - Problem: Open Reading Frames
	Problem
	Either strand of a DNA double helix can serve as the coding strand for RNA
	transcription. Hence, a given DNA string implies six total reading frames,
	or ways in which the same region of DNA can be translated into amino acids:
	three reading frames result from reading the string itself, whereas three
	more result from reading its reverse complement.
	An open reading frame (ORF) is one in which we have encountered a start
	codon but have not yet reached a stop codon. Thus, a candidate protein string
	is derived by translating an open reading frame into amino acids until a stop
	codon is reached.
	
	Given: A DNA string s of length at most 1 kbp.
	Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
	
	Sample Dataset
	AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
	Sample Output
	MLLGSFRLIPKETLIQVAGSSPCNLS
	M
	MGMTPRLGLESLLE
	MTPRLGLESLLE
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import re

def split(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ]
    
def revc(str):
	rev = {'A':'U','U':'A','C':'G','G':'C'}
	seqstr = ''
	for letter in str:
		seqstr += rev[letter]	
	revseq = seqstr[::-1]	#reverses the string using extended splice method s[begin:end:step]
	return revseq

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('ORF_output.txt','w')

lines = filein.readlines()
dna = lines[0].rstrip()
rna = dna.replace('T','U')
orf1 = rna
orf2 = rna[1:]
orf3 = rna[2:]
revrna = revc(rna)
orf4 = revrna
orf5 = revrna[1:]
orf6 = revrna[2:]

orfs = [split(orf1,3),split(orf2,3),split(orf3,3),split(orf4,3),split(orf5,3),split(orf6,3)]

bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
aa = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, aa))

matches = []
for orf in orfs:
	trans = ''
	for cod in orf:
		if len(cod) == 3:
			trans += codon_table[cod]
		else:
			break
	i=0
	while i<len(trans):
		if trans[i:].count('M') and trans[i:].count('*'):
			matches.append(re.findall('M[A-Z]*\*',trans[i:]))
		i += 1
		
format = []
for match in matches:
	for x in match:
		if x:
			format.append(x.replace('*',''))

format = list(set(format))

for y in format:
	print y
	if y == format[0]:
		fileout.write(y)
	else:
		fileout.write('\n')
		fileout.write(y)