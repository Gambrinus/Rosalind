#!/usr/bin/env python

""" Rosalind project - Problem: Introduction to Random Strings
Problem
An array is a structure containing an ordered collection of objects (numbers, strings, other arrays, etc.).
We let A[k] denote the k-th value in array A. You may like to think of an array as simply a matrix having
only one row.
A random string is constructed so that the probability of choosing each subsequent symbol is based on a
fixed underlying symbol frequency.
GC-content offers us natural symbol frequencies for constructing random DNA strings. If the GC-content is
x, then we set the symbol frequencies of C and G equal to x2 and the symbol frequencies of A and T equal
to 1-x2. For example, if the GC-content is 40%, then as we construct the string, the next symbol is 'G'/'C'
with probability 0.2, and the next symbol is 'A'/'T' with probability 0.3.
In practice, many probabilities wind up being very small. In order to work with small probabilities, we may
plug them into a function that "blows them up" for the sake of comparison. Specifically, the common logarithm
of x (defined for x>0 and denoted log10(x)) is the exponent to which we must raise 10 to obtain x.
See Figure 1 for a graph of the common logarithm function y=log10(x). In this graph, we can see that the
logarithm of x-values between 0 and 1 always winds up mapping to y-values between -infinity and 0: x-values near
0 have logarithms close to -infinity, and x-values close to 1 have logarithms close to 0. Thus, we will select
the common logarithm as our function to "blow up" small probability values for comparison.

Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.
Return: An array B having the same length as A in which B[k] represents the common logarithm of the
probability that a random string constructed with the GC-content found in A[k] will match s exactly.

Sample Dataset
ACGATACAA
0.129 0.287 0.423 0.476 0.641 0.742 0.783
Sample Output
-5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009

Hint
One property of the logarithm function is that for any positive numbers x and y,
log10(x-y)=log10(x)+log10(y).
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
	filein = open('rosalind_prob.txt', 'r')
	lines = filein.read().splitlines()
	filein.close

seq = lines[0]
gc_content = [float(x) for x in lines[1].split()]

out = []
for gc in gc_content:
	prob_gc = gc / 2.0
	prob_at = (1 - gc) / 2.0
	probs = {'A':prob_at,'T':prob_at,'G':prob_gc,'C':prob_gc}
	out.append(str(round(sum(math.log10(probs[x]) for x in seq),3)))

out = ' '.join(out)

fileout = open('PROB_output.txt','w')
fileout.write(out)						# writes to file, closes file, and rereads file
fileout.close 							# to make sure the output is correct in the file
fileout = open('PROB_output.txt','r')
print fileout.read()
fileout.close