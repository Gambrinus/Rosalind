#!/usr/bin/env python

"""	Rosalind project - Problem: DNA
	Counting Nucleotide
	Given: A DNA string s of length at most 1000 nucleotides.
	Return: Four integers corresponding to the number of times that the symbols A, C, G, and T occur in s.
	Sample Dataset: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
	Sample Output: 20 12 17 21
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

seq = raw_input("Enter the sequence: ")

a=0
c=0
g=0
t=0

for letter in seq:
	if letter in ['A','a']:
		a = a + 1
	if letter in ['C','c']:
		c = c + 1
	if letter in ['G','g']:
		g = g + 1
	if letter in ['T','t']:
		t = t + 1

print a,c,g,t