#!/usr/bin/env python

"""	Rosalind project - Problem 16: RNA Splicing
	Problem
	After identifying the exons and introns of an RNA string, we only need to delete the introns and
	concatenate the exons to form a new string ready for translation.
	
	Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns.
	Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only
	one solution will exist for the dataset provided.)
	
	Sample Dataset
	ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
	ATCGGTCGAA
	ATCGGTCGAGCGTGT
	Sample Output
	MVYIADKQHVASREAYGHMFKVCA
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

def split(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ]

def trans(rna):
	bases = ['U', 'C', 'A', 'G']
	codons = [a+b+c for a in bases for b in bases for c in bases]
	aa = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
	codon_table = dict(zip(codons, aa))
	orf = split(rna,3)
	prot = ''
	for cod in orf:
		if len(cod) == 3:
			prot += codon_table[cod]
		else:
			break
	return prot

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('p16_SPLC_output.txt','w')

lines = filein.readlines()

seq = lines[0].rstrip()
for x in lines:
	if x != lines[0]:
		seq = seq.replace(x.rstrip(),'')

rna = seq.replace('T','U')

prot = trans(rna)
prot = prot.replace('*','')

print prot
fileout.write(prot)