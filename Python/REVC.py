#!/usr/bin/env python

"""	Rosalind project - Problem: REVC
	Reverse Complement
	In a DNA string, the complement of A is T, and the complement of C is G.
	The reverse complement of a DNA string s is the string sc formed by reversing
	the symbols of s, then taking the complement of each symbol (e.g., the reverse
	complement of GTCA is TGAC).

	Given: A DNA string s of length at most 1000 bp.
	Return: The reverse complement of s.

	Sample Dataset	AAAACCCGGT
	Sample Output	ACCGGGTTTT
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

seq = raw_input("Enter the sequence: ")

seqstr = ''
for letter in seq:
	if letter in ['A','a']:
		seqstr = seqstr + 'T'
	elif letter in ['T','t']:
		seqstr = seqstr + 'A'
	elif letter in ['C','c']:
		seqstr = seqstr + 'G'
	elif letter in ['G','g']:
		seqstr = seqstr + 'C'

revseq = seqstr[::-1]	#reverses the string using extended splice method s[begin:end:step]
print revseq