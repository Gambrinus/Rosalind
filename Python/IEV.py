#!/usr/bin/env python

""" Rosalind project - Problem: Calculating Expected Offspring
Problem
For a random variable X taking integer values between 1 and n, the expected value of X is
E(X)=SIGMAnk=1kxPr(X=k). The expected value offers us a way of taking the long-term average of
a random variable over a large number of trials.
As a motivating example, let X be the number on a six-sided die. Over a large number of rolls,
we should expect to obtain an average of 3.5 on the die (even though it's not possible to roll a 3.5).
The formula for expected value confirms that E(X)=SIGMA6k=1kxPr(X=k)=3.5.
More generally, a random variable for which every one of a number of equally spaced outcomes
has the same probability is called a uniform random variable (in the die example, this "equal spacing"
is equal to 1). We can generalize our die example to find that if X is a uniform random variable with
minimum possible value a and maximum possible value b, then E(X)=a+b2. You may also wish to verify that
for the dice example, if Y is the random variable associated with the outcome of a second die roll,
then E(X+Y)=7.

Given: Six positive integers, each of which does not exceed 20,000. The integers correspond to the
number of couples in a population possessing each genotype pairing for a given factor. In order, the
six given integers represent the number of couples having the following genotypes:
AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa
Return: The expected number of offspring displaying the dominant phenotype in the next generation,
under the assumption that every couple has exactly two offspring.

Sample Dataset
1 0 0 1 0 1
Sample Output
3.5
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

import sys

if sys.argv[1] == "-i":
	filein = open(sys.argv[2], 'r')
	lines = filein.read().splitlines()
	filein.close
else:
	lines = sys.argv[1]

dd,dh,dr,hh,hr,rr = lines[0].split()

dd,dh,dr,hh,hr,rr = int(dd),int(dh),int(dr),int(hh),int(hr),int(rr)

out = str(float((2*dd+2*dh+2*dr)+(2*hh*0.75)+(2*hr*0.5)+(2*rr*0)))

fileout = open('IEV_output.txt','w')
fileout.write(out)						# writes to file, closes file, and rereads file
fileout.close 							# to make sure the output is correct in the file
fileout = open('IEV_output.txt','r')
print fileout.read()
fileout.close