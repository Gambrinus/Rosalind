#!/usr/bin/env python

"""	Rosalind project - Problem: RNA
	RNA Transcription
	An RNA string is formed from the alphabet containing A, C, G, and U.
	Given a DNA string t corresponding to a coding strand, its transcribed
	RNA string u is formed by replacing all occurrences of T with U.
	Given: A DNA string t of length at most 1000 nucleotides.
	Return: The transcribed RNA string of t.
	Sample Dataset: GATGGAACTTGACTACGTAAATT
	Sample Output: GAUGGAACUUGACUACGUAAAUU
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

seq = raw_input("Enter the sequence: ")

seqstr = ''
for letter in seq:
	if letter in ['T','t']:
		seqstr = seqstr + 'U'
	else:
		seqstr = seqstr + letter

print seqstr