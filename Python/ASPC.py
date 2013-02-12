#!/usr/bin/env python

""" Rosalind project - Problem: Introduction to Alternative Splicing
Problem
In "Counting Subsets", we saw that the total number of subsets of a set S containing n elements is equal
to 2n.
However, if we intend to count the total number of subsets of S having a fixed size k, then we use the
combination statistic C(n,k), also written (nk).

Given: Positive integers n and m with 0<=m<=n<=2000.
Return: The sum of combinations C(n,k) for all k satisfying m<=k<=n, modulo 1,000,000. In shorthand,
Sigmank=m(nk).

Sample Dataset
6 3
Sample Output
42
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
	filein = open('rosalind_aspc.txt', 'r')
	lines = filein.read().splitlines()
	filein.close

n,m = [int(x) for x in lines[0].split()]

comb_sum = 0
for k in range(m,(n+1)):
	comb_sum += math.factorial(n)/(math.factorial(n-k)*math.factorial(k))

out = str(comb_sum % 1000000)

fileout = open('ASPC_output.txt','w')
fileout.write(out)						# writes to file, closes file, and rereads file
fileout.close 							# to make sure the output is correct in the file
fileout = open('ASPC_output.txt','r')
print fileout.read()
fileout.close