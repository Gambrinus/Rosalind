#!/usr/bin/env python

"""	Rosalind project - Problem: Introduction to Probability
Problem
An array is a matrix A having only one row; A[k] represents the k-th value of A.
In a random string, each symbol is selected randomly from an alphabet based on
some underlying distribution in which every symbol has a symbol frequency, or its
own fixed chance of being drawn at any time.
GC-content gives us a natural way to form a realistic random DNA string for a given
species. If the GC-content is x, then we make the symbol frequencies of C and G equal
to x2 and set the symbol frequencies of A and T equal to 1-x2. In other words, if the
GC-content is 40%, then as we construct the string, we have a 20% chance of the next
added symbol being 'C', a 20% chance that it is 'G', a 30% chance that it is 'A', and
a 30% chance that it is 'T'.

Given: An array A containing at most 20 real numbers between 0 and 1, inclusively.
Return: An array B in which B[i] represents the probability (with a precision of three decimal places) that for the GC-content in A[i], two randomly chosen symbols will be the same.

Sample Dataset
0.23 0.31 0.75
Sample Output
0.323 0.286 0.312
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

filename = raw_input("Enter input path: ")

filein = open(filename,'r')
fileout = open('PROB_output.txt','w')

lines = filein.read().split()	#gets rid of \n at the end of each line and spilts into a list

probs = []
for gc in lines:
	probgc = float((float(gc)/2)**2)			#probability of getting 2 G's or C's 
	probat = float(((1-float(gc))/2)**2)		#probability of getting 2 A's or T's 
	probs.append(str((probat*2)+(probgc*2)))	#combined probability of duplicates

out=''	
for x in probs:
	x = str(round(float(x),3))
	out += ' ' + x
	
print out.lstrip()
fileout.write(out.lstrip())