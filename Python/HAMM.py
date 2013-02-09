#!/usr/bin/env python

"""	Rosalind project - Problem: HAMM
	Counting Point Mutations
	Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.
	
	Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
	Return: The Hamming distance dH(s,t).
	
	Sample Dataset
	GAGCCTACTAACGGGAT
	CATCGTAATGACGGCCT
	Sample Output
	7
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import operator

seq1 = raw_input("Enter sequence 1: ")
seq2 = raw_input("Enter sequence 2: ")

print map(operator.eq, seq1, seq2).count(False)