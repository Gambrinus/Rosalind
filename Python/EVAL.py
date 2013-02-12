#!/usr/bin/env python

""" Rosalind project - Problem: Expected Number of Restriction Sites
Problem
Say that you place a number of bets on your favorite sports teams. If their chances of winning are 0.3,
0.8, and 0.6, then you should expect on average to win 0.3 + 0.8 + 0.6 = 1.7 of your bets (of course,
	you can never win exactly 1.7!)
More generally, if we have a collection of events A1,A2,...,An, then the expected number of events
occurring is Pr(A1)+Pr(A2)+...+Pr(An) (consult the note following the problem for a precise explanation
	of this fact). In this problem, we extend the idea of finding an expected number of events to
finding the expected number of times that a given string occurs as a substring of a random string.

Given: A positive integer n (n<=1,000,000), a DNA string s of even length at most 10, and an array
A of length at most 20, containing numbers between 0 and 1.
Return: An array B having the same length as A in which B[i] represents the expected number of times
that s will appear as a substring of a random DNA string t of length n, where t is formed with GC-content
A[i] (see "Introduction to Random Strings").

Sample Dataset
10
AG
0.25 0.5 0.75
Sample Output
0.422 0.563 0.422

The Mathematical Details
In this problem, we are speaking of an expected number of events; how can we tie this into to the
definition of expected value that we already have from "Calculating Expected Offspring"?
The answer relies on a slick mathematical trick. For any event A, we can form a random variable for
A, called an indicator random variable IA. For an outcome x, IA(x)=1 when x belongs to A and IA(x)=0
when x belongs to Ac.
For an indicator random variable IA(x)=1, verify that E(IA)=Pr(A).
You should also verify from our original formula for expected value that for any two random variables
X and Y, E(X+Y) is equal to E(X)+E(Y). As a result, the expected number of events A1,A2,...,Am
occurring, or E(IA1+IA2+...+IAm, reduces to Pr(A1)+Pr(A2)+...+Pr(Am).
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import sys

if len(sys.argv) >= 2 and sys.argv[1] == "-t":
	filein = open('test_input.txt', 'r')
	lines = filein.read().splitlines()
	filein.close
else:
	filein = open('rosalind_eval.txt', 'r')
	lines = filein.read().splitlines()
	filein.close

n = float(lines[0])
seq = lines[1]
gcs = [float(x) for x in lines[2].split()]

probs = []
for gc in gcs:
	prob = 1.0
	for x in seq:
		if x in 'GC':
			prob = prob * gc / 2
		else:
			prob = prob * (1 - gc) / 2
	probs.append(str(round(prob * (n-1),3))) 

out = ' '.join(probs)

fileout = open('EVAL_output.txt','w')
fileout.write(out)						# writes to file, closes file, and rereads file
fileout.close 							# to make sure the output is correct in the file
fileout = open('EVAL_output.txt','r')
print fileout.read()
fileout.close