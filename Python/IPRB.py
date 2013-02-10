#!/usr/bin/env python

""" Rosalind project - Problem: Mendel's First Law
Problem
Probability is the mathematical study of randomly occurring phenomena. We will model such a
phenomenon with a random variable, which is simply a variable that can take a number of
different distinct outcomes depending on the result of an underlying random process.
For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X
represent the random variable corresponding to the color of a drawn ball, then the probability
of each of the two outcomes is given by Pr(X=red)=35 and Pr(X=blue)=25.
Random variables can be combined to yield new random variables. Returning to the ball example,
let Y model the color of a second ball drawn from the bag (without replacing the first ball).
The probability of Y being red depends on whether the first ball was red or blue. To represent all
outcomes of X and Y, we therefore use a probability tree diagram. This branching diagram represents
all possible individual probabilities for X and Y, with outcomes at the endpoints ("leaves") of the
tree. The probability of any outcome is given by the product of probabilities along the path from the
beginning of the tree; see Figure 2 for an illustrative example.
An event is simply a collection of outcomes. Because outcomes are distinct, the probability of
an event can be written as the sum of the probabilities of its constituent outcomes. For our
colored ball example, let A be the event "Y is blue." Pr(A) is equal to the sum of the
probabilities of two different outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or
310+110=25 (see Figure 2 above).

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual
possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two 
organisms can mate.

Sample Dataset
2 2 2
Sample Output
0.78333

Hint
Consider simulating inheritance on a number of small test cases in order to check your solution.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import sys
import math

if sys.argv[1] == "-i":
	filein = open(sys.argv[2], 'r')
	lines = filein.read().splitlines()
	filein.close
else:
	lines = sys.argv[1]

k,m,n = lines[0].split()

k = int(k)
m = int(m)
n = int(n)

# permutations calculated as n!/(n-r)!r! n is total and r is number of items being combined
total = float(math.factorial(k+m+n)/(math.factorial(k+m+n-2)*math.factorial(2)))

# calculates probs, k is homo dom so only includes kk,km, and kn in one
# nn is unnecessary for this exercise but whatever
prob_k = float(float((math.factorial(k)/(math.factorial(k-2)*math.factorial(2))+(k*m)+(k*n)))/total)
prob_mm = float(math.factorial(m)/(math.factorial(m-2)*math.factorial(2)))/total
prob_mn = float(m*n)/total
prob_nn = float(math.factorial(n)/(math.factorial(n-2)*math.factorial(2)))/total

# mm pairs produce 3/4 dominant mn produce 1/2 dominant
out = str(round(float(prob_k+(prob_mm*float(0.75))+(prob_mn*float(0.5))),5))

fileout = open('IPRB_output.txt','w')
fileout.write(out)						# writes to file, closes file, and rereads file
fileout.close 							# to make sure the output is correct in the file
fileout = open('IPRB_output.txt','r')
print fileout.read()
fileout.close