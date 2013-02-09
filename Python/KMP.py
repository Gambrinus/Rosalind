#!/usr/bin/env python

"""	Rosalind project - Problem: Shortening the Motif Search
	Problem
	A prefix of a string s having length n is a substring s[1:j]; a suffix of
	s is a substring s[k:n].
	The failure array of s is an array P of length n for which P[k] is the
	length of the longest substring s[j:k] that is equal to some prefix s[1:k-j+1],
	where j cannot equal 1 (otherwise, P[k] would always equal k). By convention,
	P[1]=0.
	
	Given: A DNA string s (of length at most 100 kbp).
	Return: The failure array of s.
	
	Sample Dataset
	CAGTAAGCAGGGACTG
	Sample Output
	0 0 0 0 0 0 0 1 2 3 0 0 0 1 0 0
	
	Extra Information
	If you would like a more precise technical explanation of the Knuth-Morris-Pratt
	algorithm, please take a look at this site
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import re

def compute_prefix_function(p):
    m = len(p)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and p[k] != p[q]:
            k = pi[k - 1]
        if p[k] == p[q]:
            k = k + 1
        pi[q] = k
    return pi
    
filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('KMP_output.txt','w')

lines = filein.read().splitlines()

fail = compute_prefix_function(lines[0])

out = " ".join(str(x) for x in fail)
print out
fileout.write(out.rstrip())