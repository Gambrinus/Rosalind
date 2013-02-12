#!/usr/bin/env python

""" Rosalind project - Problem: Interleaving Two Motifs
Problem
A string s is a supersequence of another string t if s contains t as a subsequence.
A common supersequence of strings s and t is a string that serves as a supersequence of both s and t.
For example, "GACCTAGGAACTC" serves as a common supersequence of "ACGTC" and "ATAT". A shortest common
supersequence of s and t is a supersequence for which there does not exist a shorter common
supersequence. Continuing our example, "ACGTACT" is a shortest common supersequence of "ACGTC" and 
"ATAT".

Given: Two DNA strings s and t.
Return: A shortest common supersequence of s and t. If multiple solutions exist, you may output
any one.

Sample Dataset
ATCTGAT
TGCATA
Sample Output
ATGCATGAT
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import sys

def shortest_common_superseq(s,t):
	s,t = min(s,t), max(s,t)

	if (s,t) in scs_dict:
		return scs_dict[(s,t)]
	else:
		if s == '':
			scs = t
		elif t == '':
			scs = s
		else:
			s_char = s[-1]
			t_char = t[-1]
			if s_char == t_char:
				scs = shortest_common_superseq(s[:-1],t[:-1]) + s_char
			else:
				s2 = shortest_common_superseq(s + t[-1],t)
				t2 = shortest_common_superseq(s,t + s[-1])
				scs = min([(len(s2),s2),(len(t2),t2)])[1]

	scs_dict[(s,t)] = scs
	return scs

if len(sys.argv) >= 2 and sys.argv[1] == "-t":
	filein = open('test_input.txt', 'r')
	lines = filein.read().splitlines()
	filein.close
else:
	filein = open('rosalind_scsp.txt', 'r')
	lines = filein.read().splitlines()
	filein.close

s,t = lines[0],lines[1]

scs_dict = {}
out = str(shortest_common_superseq(s,t))

fileout = open('SCSP_output.txt','w')
fileout.write(out)						# writes to file, closes file, and rereads file
fileout.close 							# to make sure the output is correct in the file
fileout = open('SCSP_output.txt','r')
print fileout.read()
fileout.close