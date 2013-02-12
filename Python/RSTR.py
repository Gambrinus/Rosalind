#!/usr/bin/env python

""" Rosalind project - Problem: Matching Random Motifs
Problem
Our aim in this problem is to determine the probability with which a given motif (a known promoter, say)
occurs in a randomly constructed genome. Unfortunately, finding this probability is tricky; instead of
forming a long genome, we will form a large collection of smaller random strings having the same length
as the motif; these smaller strings represent the genome's substrings, which we can then test against our
motif.
Given a probabilistic event A, the complement of A is the collection Ac of outcomes not belonging to A.
Because Ac takes place precisely when A does not, we may also call Ac "not A."
For a simple example, if A is the event that a rolled die is 2 or 4, then Pr(A)=13. Ac is the event that
the die is 1, 3, 5, or 6, and Pr(Ac)=23. In general, for any event we will have the identity that
Pr(A)+Pr(Ac)=1.

Given: A positive integer N<=100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.
Return: The probability that if N random DNA strings having the same length as s are constructed with
GC-content x (see "Introduction to Random Strings"), then at least one of the strings equals s. We allow
for the same random string to be created more than once.

Sample Dataset
90000 0.6
ATAGCCGA
Sample Output
0.689
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import sys
import math

if len(sys.argv) >= 2 and sys.argv[1] == "-t":
	filein = open('test_input.txt', 'r')
	lines = filein.read().splitlines()
	filein.close
else:
	filein = open('rosalind_rstr.txt', 'r')
	lines = filein.read().splitlines()
	filein.close

N,x = lines[0].split()
N,x = float(N),float(x)
seq = lines[1]

prob = 1.0
for i in seq:
	if i in 'GC':
		prob = prob * x / 2
	else:
		prob = prob * (1 - x) / 2
prob = 1 - (1 - prob) ** N

out = str(round(prob,3))

fileout = open('RSTR_output.txt','w')
fileout.write(out)						# writes to file, closes file, and rereads file
fileout.close 							# to make sure the output is correct in the file
fileout = open('RSTR_output.txt','r')
print fileout.read()
fileout.close